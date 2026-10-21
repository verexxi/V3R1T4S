# panel/criterion.md  (round 2: claim folder includes the sibling-task comparison)

Verdict: the claim meets the full success criterion for the mlearn_Li_forces task only. It is not a state-of-the-art claim for these structures.

Re-run checks: `verify-it-yourself/check_predictions.py` printed PASS against the cached benchmark json (pinned sha256 matches); object hashes match (three models, predictions CSV, ensemble.json); prediction ids equal the 29 official test ids, all 3960 force components present; recomputed MAE 0.012793121853596025 eV/A, 53.2% below the best listed 0.02733803004038507 (snap_mlearn; the criterion needs 0.025971 or lower); the listed best is the minimum of the 7 snapshot entries; direction min, strict comparison. Snapshot fetched 2026-10-20 00:38Z; this skeptic could not re-fetch.

Training clause: `how-we-built-it/train_ids.txt` equals the benchmark's 241 train ids, no overlap with test; selection set of 24 ids (`val_ids_used_for_selection.txt`); `selection_on_val.txt` shows config choice by val MAE only (0.010867 versus 0.010175); preregistration frozen before test scoring; MACE trained from scratch; test scored once by `evaluate_final.py`.

Reproduction clause: `verify-it-yourself/rerun_models.py` re-ran the saved models in float64; maximum difference 2.69e-08 eV/A (< 1e-6).

Null models: zero-force and train-mean-force baselines both 0.2062 eV/A; seed sd 0.000044; the test set is only 29 structures.

Comparison clause: the criterion requires the comparison to be stated in the claim, not beaten. Zuo et al. 2020 gives errors only in a figure on its own split (stated). ALIGNN 2.0 lists 0.0264 (higher; marked pending verification). The lower published value is `mlearn_analysis_Li_eqV2_153M_omat` on the sibling task mlearnall_Li_forces: 0.004228 on all 270 structures and 0.004035 on the 29 test ids (`the-record-we-beat/mlearnall_comparison.md`, `compare_mlearnall.py`); the claim states it and states that this package is 3.2 times higher. That entry is a zero-shot pretrained universal potential whose training data was not verified; it is not on the mlearn_Li_forces page and would fail the training clause there. The criterion's baseline is the best MAE listed on that task's live page, so it does not raise the bar. The win is not subsumed within the criterion's own terms; in absolute terms for these structures it is subsumed by the pretrained model, and the claim says so.

Hidden quantifiers: "best listed" is the best on the mlearn_Li_forces page only; the win is over an old leaderboard whose top entry is SNAP (2023-01-14), not over every known model; the scored unit is the three-seed ensemble (individual seeds 0.01302 to 0.01310 would also pass the 5% margin).

confirmed_scope: A 3-seed ensemble of small MACE models trained from scratch on only the 241 official train ids (24 of them held out for selection) of mlearn_Li_forces gives a force MAE of 0.012793 eV/A on the 29 official test ids, 53.2% below the best entry listed on that task's page (snap_mlearn, 0.027338) and reproducible to 3e-8 eV/A, but it is NOT the lowest known error for these structures, since the pretrained zero-shot eqV2 entry on the sibling task mlearnall_Li_forces scores about 0.004 eV/A on the same test ids, and it is a claim on a 29-structure test set only.

context: subagent (same VM)
pass: true
