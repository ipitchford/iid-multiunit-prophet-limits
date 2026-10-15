"""Optimization-safe regression tests. No optimizer, network or output-file writes."""
import copy, json, sys
from pathlib import Path
import flint
import cert_lower_mix as mix
import cert_upper2 as upper
import certify_single as single
import theta_cert as theta
ROOT = Path(__file__).resolve().parent.parent
count = 0
def require(ok, label):
    global count
    if not ok: raise RuntimeError('FAIL: ' + label)
    count += 1
    print('PASS:', label, flush=True)
def rejects(fn, label):
    try: fn()
    except (ValueError, TypeError, KeyError, ZeroDivisionError): require(True, label)
    else: require(False, label)
def read(name): return json.loads((ROOT/'data'/name).read_text())
def run():
    require(flint.__version__ == '0.9.0', 'python-flint 0.9.0')
    m=read('mix_fine.json'); u=read('inst_do450.json'); s=read('policy_k2_T24.json')
    for n in [0,-1,True,False,1.5,'40',float('nan'),float('inf')]:
        for name,fn in [('mix',lambda:mix.certify(m,n)),('upper',lambda:upper.certify(u,n)),('single',lambda:single.certify(s,n)),('theta',lambda:theta.barrier('0.483','1.37',n))]:
            rejects(fn, name+' rejects N='+repr(n))
    for field in ['k','T']:
        for value in [True,False,0,-1,2.0]:
            for name,base,fn in [('mix',m,mix.certify),('single',s,single.certify)]:
                bad=copy.deepcopy(base);bad[field]=value
                rejects(lambda:fn(bad,1), name+' rejects '+field+'='+repr(value))
    for value in ['NaN','Infinity','1/0',True,0.5,float('nan')]:
        bad=copy.deepcopy(m);bad['policies'][0]['w']=value
        rejects(lambda:mix.certify(bad,1), 'mix invalid rational '+repr(value))
        bads=copy.deepcopy(s);bads['a'][0][0]=value
        rejects(lambda:single.certify(bads,1), 'single invalid rational '+repr(value))
        badu=copy.deepcopy(u);badu['claim']=value
        rejects(lambda:upper.certify(badu,1), 'upper invalid rational '+repr(value))
    for bad_value in [[],[[]],'not a matrix']:
        bad=copy.deepcopy(s);bad['a']=bad_value
        rejects(lambda:single.certify(bad,1), 'single malformed matrix '+repr(bad_value))
        badm=copy.deepcopy(m);badm['policies'][0]['a']=bad_value
        rejects(lambda:mix.certify(badm,1), 'mix malformed matrix '+repr(bad_value))
    for value in ['0','-1','1','NaN']:
        bad=copy.deepcopy(s);bad['c']=value
        rejects(lambda:single.certify(bad,1), 'single claim domain '+value)
        badm=copy.deepcopy(m);badm['c']=value
        rejects(lambda:mix.certify(badm,1), 'mix claim domain '+value)
    bad=copy.deepcopy(m);bad['policies'][0]['w']='0'
    rejects(lambda:mix.certify(bad,40),'zero mixture weight')
    for field,value in [('x',[]),('nu',[]),('x',['0']),('x',['1','1']),('nu',['-1'])]:
        bad=copy.deepcopy(u);bad[field]=value
        rejects(lambda:upper.certify(bad,1),'upper malformed '+field+repr(value))
    for q in ['0','0.5','-1',True,'NaN']:
        rejects(lambda:theta.T_enclosure(q), 'theta invalid domain '+repr(q))
    for q in [0,-1,2]:
        rejects(lambda:theta.u_lower(q),'lower inverse domain '+repr(q))
        rejects(lambda:theta.u_upper(q),'upper inverse domain '+repr(q))
    require(mix.certify(m,40)['ok'], 'mixture 40 positive certificate')
    require(upper.certify(u,80000)['below_claim'], 'upper 80000 positive certificate')
    require(single.certify(s,400)['ok'], 'single 400 positive certificate')
    # Modules set precision on import; set the supplied theta precision explicitly.
    flint.ctx.prec=200
    require(theta.T_enclosure('0.483')[1] < 1 and theta.T_enclosure('0.48302')[0] > 1, 'theta bracket')
    require(theta.barrier('0.483','1.37',2000)[2], 'theta 2000 positive barrier')
    high=copy.deepcopy(m);high['c']='0.83696'
    require(not mix.certify(high,40)['ok'], 'excessive mixture claim rejected')
    low=copy.deepcopy(u);low['claim']='0.83'
    require(not upper.certify(low,80000)['below_claim'], 'excessive upper claim rejected')
    high=copy.deepcopy(s);high['c']='0.8366'
    require(not single.certify(high,400)['ok'], 'excessive single claim rejected')
    print(json.dumps({'tests_passed':count,'optimized':not __debug__,'flint':flint.__version__}))
if __name__=='__main__':run()
