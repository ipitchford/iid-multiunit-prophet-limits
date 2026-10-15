"""Portable clean certificate replay. Requires a NEW output directory; no overwrites."""
import argparse, datetime, hashlib, json, os, platform, subprocess, sys, time
from pathlib import Path
import flint
ROOT=Path(__file__).resolve().parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,value):
    with p.open('x') as f:json.dump(value,f,indent=2);f.write('\n')
def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('output',type=Path);args=parser.parse_args()
    if flint.__version__!='0.9.0':raise RuntimeError('python-flint 0.9.0 required')
    out=args.output.resolve();out.mkdir(parents=False,exist_ok=False)
    sources=['code/cert_lower_mix.py','code/cert_upper2.py','code/certify_single.py','code/theta_cert.py','code/test_certifiers.py','code/replay.py','data/mix_fine.json','data/inst_do450.json','data/policy_k2_T24.json']
    hashes={p:sha(ROOT/p) for p in sources}
    write(out/'environment.json',{'python':platform.python_version(),'python_implementation':platform.python_implementation(),'python_flint':flint.__version__,'platform':platform.platform(),'bytecode_disabled':True,'thread_limit':1,'scope':'numerical certificates and regression tests only; not analytic proof or final release approval'})
    cases=[('mixture',['code/cert_lower_mix.py','data/mix_fine.json','40']),('upper',['code/cert_upper2.py','data/inst_do450.json','80000']),('theta',['code/theta_cert.py','2000']),('single',['code/certify_single.py','data/policy_k2_T24.json','400']),('regression',['code/test_certifiers.py'])]
    rows=[]
    for optimized in [False,True]:
        for name,argv in cases:
            label=name+('-optimized' if optimized else '-normal');flags=(['-O'] if optimized else [])+['-B']
            tick=time.monotonic();start=datetime.datetime.now(datetime.timezone.utc).isoformat()
            with (out/(label+'.stdout')).open('x') as stdout,(out/(label+'.stderr')).open('x') as stderr:
                p=subprocess.run([sys.executable,*flags,*argv],cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1'),stdout=stdout,stderr=stderr,timeout=600)
            elapsed=time.monotonic()-tick;valid=False;reason='nonzero exit'
            if p.returncode==0:
                try:
                    text=(out/(label+'.stdout')).read_text();r=json.loads(text.splitlines()[-1] if name=='regression' else text)
                    valid={'mixture':lambda:r['ok'] is True and (r['c'],r['k'],r['T'],r['n_policies'])==('0.83695',2,64,36),
                           'upper':lambda:r['below_claim'] is True and r['claimed_upper']=='0.8372914' and r['M']==41 and r['steps']==80000,
                           'theta':lambda:r['theta2_bracket_certified'] is True and r['r_star_gt_r_lo_certified'] is True and r['sum_theta_lt_0.835590'] is True and r['barrier_steps']==2000,
                           'single':lambda:r['ok'] is True and (r['c'],r['k'],r['T'])==('0.8365',2,24),
                           'regression':lambda:r['tests_passed']>=110 and r['optimized']==optimized and r['flint']=='0.9.0'}[name]()
                    reason='expected checks passed' if valid else 'output semantics mismatch'
                except (ValueError,KeyError,TypeError):reason='unreadable expected result'
            row={'label':label,'command':['python',*flags,*argv],'started_utc':start,'elapsed_seconds':elapsed,'exit_code':p.returncode,'passed':valid,'reason':reason,'stdout_sha256':sha(out/(label+'.stdout')),'stderr_sha256':sha(out/(label+'.stderr'))}
            write(out/(label+'.receipt.json'),row);rows.append(row);print(label, 'PASS' if valid else 'FAIL',flush=True)
    unchanged=hashes=={p:sha(ROOT/p) for p in sources}
    write(out/'summary.json',{'schemaVersion':'1.0','input_hashes':hashes,'inputs_unchanged':unchanged,'runs':rows,'all_passed':unchanged and all(r['passed'] for r in rows),'claim_ceiling':'Producer-side certificate replay, not independent implementation, full analytic proof review, or publication approval.'})
    return 0 if unchanged and all(r['passed'] for r in rows) else 1
if __name__=='__main__':raise SystemExit(main())
