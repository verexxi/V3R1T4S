# mlearn Si forces: from-scratch MACE ensemble, test force MAE 0.049536 eV/A

Target: bank id `jarvis-mlearn-mlff-force-mae`, cell `mlearn_Si_forces` (JARVIS-Leaderboard, NIST). One element, one package.

## What
A 3-seed ensemble of small MACE models trained from scratch on the 214 official train ids of mlearn_Si_forces gives a force MAE of 0.049536 eV/A on that task's 25 official test structures, 28.6% below the best listed entry (0.069424), with predictions reproducible to 2.1e-7 eV/A; it is not the lowest known force MAE on these structures, since a zero-shot pretrained eqV2 entry on the sibling task mlearnall_Si_forces gets 0.0135 eV/A on the same 25 test ids, and it is not a claim about other elements, splits or the wider state of the art.

Files of this package: the predictions file is `object/predictions_Si_forces_test.csv`, the three trained models are `object/models/mace_Si_seed1.model` to `seed3.model`, the training scripts are in `how-we-built-it/`, and the checker is `verify-it-yourself/check_predictions.py`.

## Check it yourself
```sh
sh verify-it-yourself/run_checks.sh
```
Needs internet once (it downloads the benchmark json from GitHub and checks its sha256). Expected last line: `PASS` (it exits non-zero and prints `FAIL` otherwise; it also fails if a digit of anything in `object/` is changed). Rough time: a few seconds. If a Python with numpy, ase, torch and mace-torch is available (set `MLFF_PYTHON`), it also downloads the public jarvis 'mlearn' structures (about 2.5 MB, sha256-checked) and re-runs the three saved models on the test structures; the maximum difference to the predictions file must be at most 1e-6 eV/A (about 30 s on a laptop CPU).

## Compared to
| item | value | source |
|---|---|---|
| best listed force MAE on the live task page when staged | 0.06942387617720659 (alignnff_mlearn_wt1) | https://pages.nist.gov/jarvis_leaderboard/AI/MLFF/mlearn_Si_forces/ , fetched 2026-10-20T01:41:14Z, HTTP 200, page sha256 2f99dfaacb4289863846b2dc5390aab3e14b265bba4f1d9e7195d9ecc9d5cf17 |
| this package (3-seed ensemble) | 0.04953645273271273 | `object/predictions_Si_forces_test.csv` |
| improvement over the live best | 28.6% (the criterion asks for at least 5%) | computed by the checker |
| seed MAEs (sd 0.000115) | 0.052529, 0.052342, 0.052319 | `how-we-built-it/test_scores.json` |
| zero-force baseline / train-mean-force baseline | 0.5662 / 0.5662 | same test ids |
| ALIGNN 2.0 table (arXiv 2609.19487, marked there as pending verification) | 0.0872 | https://arxiv.org/abs/2609.19487 (same train/test sizes) |
| Zuo et al. 2020 | errors are only in its Figure 3 on its own split; no number was extracted here | https://arxiv.org/abs/1906.08888 |

## Lower published values on the same structures (stated, not hidden)
The leaderboard's sibling task `mlearnall_Si_forces` (empty train set; zero-shot pretrained models; test = all 239 structures of this element) lists `mlearn_analysis_Si_eqV2_153M_omat` at 0.012335 eV/A. On the 25 official test ids of `mlearn_Si_forces` that entry's published predictions give 0.013515 eV/A, which is LOWER than this package's 0.049536 (about 3.7 times lower). It is a pretrained universal potential, not trained only on this element's train ids, so it is outside the criterion's training clause and is not an entry of the task claimed here; its training data was not verified. This package is NOT a claim of the lowest known force MAE for these structures. Details and the script that recomputes the number: `the-record-we-beat/mlearnall_comparison.md`, `the-record-we-beat/compare_mlearnall.py`.

## Not claimed
- Only the force task of this one element. No claim on energies, stresses or any other element in this package (the partial wins p1 and p2 were not attempted).
- Not a claim that the model is a good general potential: it was fitted to this element's few hundred DFT configurations only.
- The Zuo et al. 2020 comparison is qualitative (figure-only numbers, a different split).
- Test results for every element attempted in this run (the claim is for Si only; an element is claimed only if its own package exists):

| element | ensemble test MAE (eV/A) | seeds 1 / 2 / 3 | zero-force baseline | live best when staged | vs live best |
|---|---|---|---|---|---|
| Mo | 0.097400 | 0.106269 / 0.104097 / 0.106594 | 0.9496 | 0.18434104563832232 | 47.2% below |
| Li | 0.012793 | 0.013018 / 0.013097 / 0.013092 | 0.2062 | 0.02733803004038507 | 53.2% below |
| Si | 0.049536 | 0.052529 / 0.052342 / 0.052319 | 0.5662 | 0.06942387617720659 | 28.6% below |
| Ge | 0.038802 | 0.039985 / 0.040929 / 0.041756 | 0.4236 | 0.07201822622548142 | 46.1% below |
| Ni | 0.019804 | 0.020131 / 0.020667 / 0.020363 | 0.4984 | 0.06181732186425153 | 68.0% below |
| Cu | 0.008574 | 0.008758 / 0.009043 / 0.008793 | 0.4514 | 0.017749048098047573 | 51.7% below |

## Review record
Three skeptic files and the gate are in `panel/` (subagents started in the same session on the same machine, each shown only the claim folder; the gate is the main session's own). `panel/gate.md` records the final status.

## Credits
- JARVIS-Leaderboard: Kamal Choudhary and co-workers, NIST (npj Comput. Mater. 2024), https://github.com/usnistgov/jarvis_leaderboard , task pages at https://pages.nist.gov/jarvis_leaderboard/ .
- mlearn datasets: Yunxing Zuo, Chi Chen, Xiangguo Li, Zhi Deng, Yiming Chen, Joerg Behler, Gabor Csanyi, Alexander Shapeev, Aidan Thompson, Mitchell Wood, Shyue Ping Ong, J. Phys. Chem. A 124, 731 (2020), https://arxiv.org/abs/1906.08888 ; https://github.com/materialsvirtuallab/mlearn .
- The listed entry compared against (alignnff_mlearn_wt1) and the other listed entries are their contributors' work on the leaderboard.
- MACE: Ilyes Batatia, David Kovacs, Gregor Simm, Christoph Ortner, Gabor Csanyi, https://github.com/ACEsuit/mace (mace-torch 0.3.16 was used for training).
- ASE (Atomic Simulation Environment), PyTorch, jarvis-tools (structures from the figshare 'mlearn' archive, https://doi.org/10.6084/m9.figshare.22721047).
- ALIGNN 2.0 authors (Lee, Campbell, Ajith, Kalinin, Wolverton, Choudhary), arXiv 2609.19487, for the later reference values quoted above.
