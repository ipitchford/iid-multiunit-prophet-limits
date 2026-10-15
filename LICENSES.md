# Component-level licence map

* Original manuscript/prose, structured claims, project-created rational witness data, diagrams if any, and public execution records: **CC0-1.0**, see [LICENSE](LICENSE) and [PUBLIC_DOMAIN.md](PUBLIC_DOMAIN.md).
* Original programs under `code/`, including certificate hardening, tests, clean replay and optional exploration scripts: **MIT**, see [LICENSE-CODE](LICENSE-CODE).
* Cited articles and external source documents: their upstream rights apply; citation is not relicensing. No external article PDF or full supplied reviewer report is included in this package.
* Python, python-flint/FLINT/Arb and optional NumPy/SciPy: external dependencies, not vendored; retain their upstream licences. Package licences do not override them.
* PDF fonts: **SIL Open Font License 1.1 (OFL-1.1)**, not CC0. The embedded-font inventory and rights handling are recorded below. Other generated-format components retain any applicable upstream terms.

The creator attribution is Anonymous; publisher/maintainer identity does not establish human scholarly authorship. This map follows the authorized Evidence Press treatment of original project material, not a transfer of rights in cited works.

## PDF font inventory and embedding rights

Checked 2026-10-15 for `paper.pdf`, SHA-256 `872b5afab8c7bed53995dfe2578a9790a08412389b37ccb5e011e0c6eb8d5aa7`. `pdffonts` reports 20 Type 1 fonts, all embedded and subsetted, with Unicode mappings. Ignoring PDF subset prefixes, their names are:

`CMR17`, `CMR12`, `CMR10`, `CMBX10`, `CMMI10`, `CMMI7`, `MSBM10`, `CMSY10`, `CMSY7`, `CMR7`, `CMBX12`, `CMR8`, `CMMI8`, `CMEX10`, `CMTI10`, `CMSY8`, `CMMI6`, `CMR6`, `CMITT10`, `CMTT10`.

These are the AMSFonts Type 1 implementations of Computer Modern and the AMS symbol font MSBM10. The build uses TinyTeX's `texmf-dist/fonts/type1/public/amsfonts/cm/` and `symbols/` font directories. Each of the 20 corresponding `.pfb` files was checked directly: its human-readable header identifies SIL Open Font License, Version 1.1. The inspected CMR10 and MSBM10 headers identify copyright 1997, 2009 American Mathematical Society, with their respective font names reserved. The [AMS-maintained CTAN package record](https://ctan.org/pkg/amsfonts) independently identifies OFL licensing and includes the canonical Type 1 Computer Modern implementation.

The [official OFL 1.1 text](https://openfontlicense.org/open-font-license-official-text/), permission clause and condition 5, permits embedding and distinguishes font rights from the document's licence. The [official OFL FAQ](https://openfontlicense.org/ofl-faq/), §§1.10–1.14, expressly covers full or subset document embedding and confirms that embedding does not change the document's licence. These primary licensing sources were read on 2026-10-15.

This package distributes the font subsets embedded in the PDF, not standalone font files. Original project prose remains under the licence above; neither those terms nor the code licence relicense the embedded font software. Anyone separately redistributing or modifying extracted or upstream fonts must observe OFL requirements, including applicable notices and Reserved Font Names. No font endorsement is implied. No font-embedding release blocker was identified for these checked PDF bytes; a later PDF using different fonts requires a renewed inventory.
