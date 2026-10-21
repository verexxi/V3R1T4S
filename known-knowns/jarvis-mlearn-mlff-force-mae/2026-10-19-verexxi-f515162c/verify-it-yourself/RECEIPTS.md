# Receipts (real output of `sh verify-it-yourself/run_checks.sh`, exit status 0, 2026-10-20T14:09:19Z)

```
ok   benchmark.json.zip 67ac882458f5636e5d39ac45546ea8279ffbcd5f7600292ef55059558c00fbb1
ok   sha256 object/ensemble.json
ok   sha256 object/models/mace_Si_seed1.model
ok   sha256 object/models/mace_Si_seed2.model
ok   sha256 object/models/mace_Si_seed3.model
ok   sha256 object/predictions_Si_forces_test.csv
ok   benchmark json sha256
ok   csv header
ok   prediction ids == official test ids (25)
ok   every prediction has the right number of components
components 4575  force MAE 0.049536452732712732 eV/A
ok   MAE equals INDEX.csv value 0.04953645273271273
ok   MAE 0.049536 <= 0.95 * listed best 0.069423876177206592 (= 0.065953): improvement 28.6%
ok   training ids used == benchmark train ids (214)
ok   no test id in the training list
ok   mlearn_figshare.zip f731b3ad5ac3e1b083a7ce12936a9e0e6aa2704de2a1b95150429823c1398a28
max |re-run - predictions file| = 2.147e-07 eV/A over 25 test structures
PASS
PASS
```
