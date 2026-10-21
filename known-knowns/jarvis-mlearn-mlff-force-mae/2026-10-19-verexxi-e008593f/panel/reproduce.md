# panel/reproduce.md

context: subagent (same VM)

## Scope
The skeptic read only the Cu claim folder, used the given Python (numpy, torch, mace) as a tool, wrote scratch files to a temp directory, used no network, wrote its own checkers before opening the author's code and did not run the author's `verify-it-yourself/*` scripts.

## Definition checked (quoted from `CLAIM.md`)
"force MAE on the leaderboard's official test split, recomputed by the checker from the benchmark json ... STRICTLY LOWER (direction: min) than the best MAE listed on that task's live leaderboard page ... by at least 5% relative; AND the model was trained only on the train (and val) ids of that benchmark json ...; AND re-running the saved model on the test structures reproduces the predictions file to 1e-6 eV/A".

## Findings
1. Input and record hashes match the stated values: `inputs/benchmark.json.zip` (1d9c4633...13a8), `inputs/mlearn_figshare.zip` (f731b3ad...8a28), `the-record-we-beat/page_as_fetched.html` (935d1a54...13ed7, equal to `snapshot.md`), `object/predictions_Cu_forces_test.csv` (e008593f...7508, equal to `INDEX.csv` and `verify-it-yourself/expected_hashes.txt`). The sha256 of the three model files and `object/ensemble.json` were not checked against `expected_hashes.txt` by this skeptic.
2. Best listed value derived from the saved page: 8 table rows parsed, minimum of the Multimae column is `matgl_mlearn` 0.017749048098047573, as claimed; no listed entry is lower.
3. Predictions against the benchmark json: 31 ids, exactly the benchmark test ids, no duplicates; component counts match (9534 in total); all values finite; recomputed MAE 0.00857427628878558, equal to `INDEX.csv` and the claim; improvement 51.69% against the 5% requirement.
4. Trivial baselines: zero-force MAE 0.451413 and train-mean MAE 0.451413, as claimed.
5. Training-id integrity: `how-we-built-it/train_ids.txt` lists 262 ids, all in the benchmark train set, 0 overlap with test; the 26 validation ids used for selection are a subset of train.
6. Re-running the saved models: own float64 inference with the ASE MACE calculator on structures looked up in `mlearn.json`; ensemble = mean of the 3 seeds; maximum absolute difference from the predictions file 3.1e-7 eV/A (< 1e-6); ensemble MAE 0.008574281; per-seed MAEs 0.008758, 0.009043, 0.008793 as claimed; a second run was identical (no non-determinism).
7. Training provenance: three training logs, one per seed, differing from each other, showing from-scratch training from epoch 0 with a validation set drawn from train; `mkxyz.py` builds train and validation sets from the benchmark train split only. Absence of pretraining cannot be proven from the saved weights; logs, `COMMANDS.md` and the loss curves are consistent with the claim.
8. Stated bar: the claim is the criterion as written for `mlearn_Cu_forces`; `the-record-we-beat/mlearnall_comparison.md` says openly that a pretrained zero-shot entry on the all-structures task has a lower value (0.0052 eV/A on these 31 ids), that it is not an entry of the claimed task, and that the claim is not "lowest known". The literature comparison belongs to the NOVELTY skeptic.

No mismatches, missing objects or non-determinism found.

pass: true
