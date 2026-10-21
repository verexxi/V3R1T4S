# Receipts (real output of `sh verify-it-yourself/run_checks.sh`, exit status 0, 2026-10-20T14:08:59Z)

```
ok   benchmark.json.zip ed3562d4724cf971f74a2b70bb1ad45913b369c7531fc97f9acb77728bec73d7
ok   sha256 object/ensemble.json
ok   sha256 object/models/mace_Li_seed1.model
ok   sha256 object/models/mace_Li_seed2.model
ok   sha256 object/models/mace_Li_seed3.model
ok   sha256 object/predictions_Li_forces_test.csv
ok   benchmark json sha256
ok   csv header
ok   prediction ids == official test ids (29)
ok   every prediction has the right number of components
components 3960  force MAE 0.012793121853596025 eV/A
ok   MAE equals INDEX.csv value 0.012793121853596025
ok   MAE 0.012793 <= 0.95 * listed best 0.02733803004038507 (= 0.025971): improvement 53.2%
ok   training ids used == benchmark train ids (241)
ok   no test id in the training list
ok   mlearn_figshare.zip f731b3ad5ac3e1b083a7ce12936a9e0e6aa2704de2a1b95150429823c1398a28
max |re-run - predictions file| = 2.692e-08 eV/A over 29 test structures
PASS
PASS
```
