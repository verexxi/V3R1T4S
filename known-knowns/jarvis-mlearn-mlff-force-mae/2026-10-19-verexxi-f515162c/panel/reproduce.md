# panel/reproduce.md

context: subagent (same VM)

Instruction followed: "Before reading the author's code, write your own checker from the definition (quote it)." I wrote `mychk.py` (outside the claim folder) from the Success criterion. It recomputes the MAE from `object/predictions_Si_forces_test.csv` against the test targets in `inputs/benchmark.json.zip`. Before it, I opened only the claim, listing and data files (CLAIM.md, REPRODUCE.md, INDEX.csv, snapshot, sources.json, ensemble.json, expected_hashes.txt). I read the package scripts only afterwards.

**My checker**
```
bench sha 67ac8824...fbb1   (matches sources.json)
n comps 4575 MAE 0.04953645273271273 per-struct mean 0.0508899
zero baseline 0.5662027856240437
rel improvement 0.28646 pass5% True
train ids == benchmark train: True 214 overlap w test: set()
```
- The predictions file has exactly the 25 test ids, with no duplicates and all values finite. Each vector length matches its target.
- The MAE of 0.049536 pools all force components. It matches the INDEX.csv value and the claimed 28.6% margin against the best listed value, 0.0694239 (a 5% requirement).
- The zero-force baseline of 0.5662 also matches the claim.
- The `sha256sum` of the predictions file and both input zips match INDEX.csv and sources.json.
- None of the 25 official test ids appear in `how-we-built-it/train_ids.txt` (overlap is the empty set). The file holds 214 ids and equals the benchmark's train key set.

**Live leaderboard**
I re-fetched https://pages.nist.gov/jarvis_leaderboard/AI/MLFF/mlearn_Si_forces/. It lists 11 entries, and the best is alignnff_mlearn_wt1 at 0.0694, which matches the snapshot. No entry is lower.

**Package checker and model re-run**
I ran both on a temporary copy of the folder with OMP_NUM_THREADS=1, using the cached input zips.
```
sh verify-it-yourself/run_checks.sh
max |re-run - predictions file| = 2.147e-07 eV/A over 25 test structures
PASS
PASS
```
The re-run of the three saved models is below the 1e-6 limit.

**Not verified**
- The three individual seed MAEs (0.0525, 0.0523, 0.0523). I did not run the models separately.
- That training used only the train ids. The logs and ids file are consistent with it, but the saved weights cannot prove it.
- The literature comparison (Zuo 2020, ALIGNN 2.0) is stated in CLAIM.md. I did not independently search or confirm that arXiv 2609.19487 exists.

I found no mismatches, missing objects or non-determinism.

pass: true
