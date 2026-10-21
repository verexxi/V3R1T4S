# Receipts (real output of `sh verify-it-yourself/run_checks.sh`, exit status 0, 2026-10-20T14:08:38Z)

```
ok   benchmark.json.zip 1d9c463318b581d9debe0a8c5937af6bc504686ee947b611b2a363cd07ed13a8
ok   sha256 object/ensemble.json
ok   sha256 object/models/mace_Cu_seed1.model
ok   sha256 object/models/mace_Cu_seed2.model
ok   sha256 object/models/mace_Cu_seed3.model
ok   sha256 object/predictions_Cu_forces_test.csv
ok   benchmark json sha256
ok   csv header
ok   prediction ids == official test ids (31)
ok   every prediction has the right number of components
components 9534  force MAE 0.008574276288785581 eV/A
ok   MAE equals INDEX.csv value 0.00857427628878558
ok   MAE 0.008574 <= 0.95 * listed best 0.017749048098047573 (= 0.016862): improvement 51.7%
ok   training ids used == benchmark train ids (262)
ok   no test id in the training list
ok   mlearn_figshare.zip f731b3ad5ac3e1b083a7ce12936a9e0e6aa2704de2a1b95150429823c1398a28
max |re-run - predictions file| = 3.106e-07 eV/A over 31 test structures
PASS
PASS
```
