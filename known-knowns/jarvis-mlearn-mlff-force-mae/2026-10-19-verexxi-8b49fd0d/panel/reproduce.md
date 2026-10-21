# Reproduce skeptic report

context: subagent (same VM)

Scope: I read only files inside the Li claim folder. I ran everything on a temp copy and wrote nothing into the claim folder. The only fetches were the URLs named in `verify-it-yourself/sources.json` and the status-source leaderboard page named in `CLAIM.md`.

## 1. My own checker (written from the CLAIM.md criterion before reading the author's code)

The criterion, quoted: "force MAE on the leaderboard's official test split, recomputed by the checker from the benchmark json … STRICTLY LOWER … than the best MAE listed … by at least 5% relative; AND the model was trained only on the train (and val) ids …; AND re-running the saved model on the test structures reproduces the predictions file to 1e-6 eV/A".

My script loads `inputs/benchmark.json.zip` and reads `mlearn_Li_forces.json`, which has `train` with 241 ids and `test` with 29 ids. It flattens every test force component and compares it with `object/predictions_Li_forces_test.csv`.

```
inputs sha256: ed3562d4...73d7 (benchmark), f731b3ad...8a28 (figshare)  -> both equal sources.json
29 29 True 241                  # test ids == prediction ids, 241 train ids
3960 True                       # all 3960 force components present and finite
MAE 0.012793121853596025 zero 0.20620189010353535
margin 0.5320393666003951 True  # (0.027338 - MAE)/0.027338 = 53.2% >= 5%
241 241 True 0                  # train_ids.txt: 241 unique, equal to the benchmark train set, 0 overlap with test
val 24 True 0                   # val ids are a subset of train, 0 overlap with test
predictions sha256 8b49fd0d...671e == INDEX.csv
```

- The MAE 0.012793121853596025 matches the claimed value and `INDEX.csv` to every digit.
- The zero-force baseline 0.2062 matches the claim.
- None of the 29 official test ids (`Li-242` onward) appear in `how-we-built-it/train_ids.txt`. The set overlap is 0. The train ids are exactly the benchmark's 241 train ids.

## 2. Best listed value on the live leaderboard

I re-fetched `https://pages.nist.gov/jarvis_leaderboard/AI/MLFF/mlearn_Li_forces/`. It returned HTTP 200 and still contains `snap_mlearn` at 0.02733803004038507 as the lowest value. The next values are 0.031076715707407717, 0.0464678409069162 and 0.050938555232858874.

The page sha256 differs from `the-record-we-beat/snapshot.md` (`1d5e7508…` against `a6b99448…`). The table values are unchanged, so I treat this as harmless page-markup drift.

I also re-downloaded the benchmark zip from the raw GitHub URL. Its sha256 is `ed3562d4…73d7`, equal to the saved copy.

## 3. Package checker and model re-run

I ran `sh verify-it-yourself/run_checks.sh` on the temp copy, with the cached input zips and the heavy-step interpreter.

```
max |re-run - predictions file| = 2.692e-08 eV/A over 29 test structures
PASS
PASS
```

- The 2.692e-08 maximum difference is well under the 1e-6 limit.
- The run took 33 s and ended with PASS. The only warnings were deprecation notices.

## 4. Other items

- **Seed MAEs:** `how-we-built-it/test_scores.json` gives 0.0130182, 0.0130968 and 0.0130920 for the three seeds, with an ensemble of 0.012793121853596025. This matches the claim.
- **Pretraining and selection:** `how-we-built-it/PREREG.md` states no pretrained weights. Selection used val ids only, and val is a subset of train.
- **Literature comparison:** `CLAIM.md` states it, covering Zuo et al. 2020 and the later ALIGNN 2.0 figure of 0.0264.
- **Not independently checked:** I did not retrain the models, and I did not verify the ALIGNN 2.0 citation. Neither is needed for this criterion.

All properties are confirmed. The claimed value reproduces exactly, the margin is 53.2% against the 5% requirement, the re-run matches to 2.7e-8, and there is no id leakage.

pass: true
