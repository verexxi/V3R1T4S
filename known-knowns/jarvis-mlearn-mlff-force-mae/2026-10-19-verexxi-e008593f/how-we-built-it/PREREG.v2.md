# PREREG.v2 (frozen 2026-10-19T19:41Z; still before any model was scored on any test split)
Reason: measured MACE-from-scratch cost on this CPU (4 threads, Mo: about 18 s/epoch for the small model; the 107-atom Cu/Ni cells are about 2.7x slower), so the 8 h budget cannot cover all six elements in the original order.
Changes (process only; PREREG.md otherwise stands, including the metric, the val rule, the success rule and no test peeking):
1. Element order becomes Mo, Li, Si, Ge, then Ni, Cu (cheap cells first, 107-atom cells last).
2. Selection phase: two configurations per element run in parallel at 2 threads each: A = 32 channels, r_max 5.0; B = 16 channels, r_max 4.5; both L=1 (hidden NxOe+Nx1o), max_ell 2, correlation 3, 2 interactions, float32 training, 120 epochs, Adam lr 0.01 with plateau decay, EMA 0.99, forces weight 100, energy weight 1. The config with the lower val force MAE (best EMA checkpoint on val) wins.
3. Final phase uses the winner with a fixed epoch count (the winning run's epoch count), seeds 1, 2, 3 on all train ids; ensemble = mean of the 3 seeds' forces; inference in float64 from the saved models.

## PREREG.v3 addendum (20:08Z, val-only information used: B reached val MAE 0.1x and train≈val RMSE, i.e. underfit at only ~2000 optimizer steps)
Configs A (killed unfinished at epoch ~50) and B (finished) at batch 10 / lr 0.01 are superseded. Selection now compares C = 16 channels, r_max 4.5 and D = 32 channels, r_max 4.5, both batch size 3, lr 0.005, 150 epochs, otherwise identical. Still val-only; test untouched.

## PREREG.v3 addendum 2 (22:50Z; before any Li/Si/Ge/Ni/Cu test scoring; Mo test scored once at 22:50Z)
Compute is the limit. For elements after Mo and Li the config pair C/D may be reduced to C alone if the remaining wall clock cannot pay for D; the choice is made from val only and is stated in each package.

## PREREG.v4 addendum (2026-10-20T07:31:26Z; written before any Ni or Cu validation or test result)
Ge ran the full C/D pair (val MAE C 0.047547, D 0.045351, D selected). For Ni and Cu (107-atom cells, about 2.7x slower) compute allows one width only: C = 16 channels, r_max 4.5, batch 3, lr 0.005, 150 epochs, as for Si. Ni_valD was started and stopped at epoch about 8 for this reason (no result read). Because C is the only configuration, the three final seeds (1, 2, 3, all train ids) may start before the validation run ends; the validation run is then only a sanity gate: if val MAE of C is not below 0.95 x the live best, no claim is made for that element and its test result is still reported. No test label is read before all three seeds are trained.
