# panel/novelty.md

Files read (all in the Cu claim folder): `CLAIM.md`, `the-record-we-beat/snapshot.md`, `the-record-we-beat/mlearnall_comparison.md`, `the-record-we-beat/page_as_fetched.html` (hash and diff check only).

Status page, fetched once with no retries: https://pages.nist.gov/jarvis_leaderboard/AI/MLFF/mlearn_Cu_forces/ , HTTP 200, `Date` header Tue, 20 Oct 2026 14:05:49 GMT. Best listed value (multimae, forces): 0.017749048098047573 for `matgl_mlearn`; next `alignnff_mlearn_wt1` 0.019367 and `snap_mlearn` 0.0596; 8 entries in total. This matches the claim's snapshot. The raw body differs from the saved page only by a Cloudflare per-request challenge script (hence different sha256 values); the table is identical. The claimed 0.008574 is 51.7% below 0.017749, clearing the 5% margin.

Repo `elder-plinius/V3R1T4S`: `TROPHY_CASE.md` (main) has no mlearn, JARVIS or MLFF row. Open pull requests: the only related one is the Mo claim of this target (0.0974 vs 0.1843), a different element; no open pull request for Cu (titles searched across the first 4 pages of open pull requests, 100 per page).

Literature, last 24 months: one web search found no published MLIP result better than the claimed value for mlearn-Cu force MAE (weak search, generic benchmarks only). The claim folder cites ALIGNN 2.0 (arXiv 2609.19487) at 0.0179, above the claimed 0.008574 and marked unverified there; not checked independently.

Lower values and decision: the folder lists the sibling task `mlearnall_Cu_forces`; its best entry, the pretrained eqV2-86M model, has 0.004834 eV/A on all 293 Cu structures and 0.005205 on the 31 official `mlearn_Cu_forces` test ids, lower than the claimed 0.008574 by a factor of about 1.6. This skeptic decided that this does not defeat novelty under the criterion's literal text: the criterion compares against the best MAE listed on the `mlearn_<element>_forces` task's page and requires training only on that benchmark's train (and val) ids with no pretraining on data containing the test configurations. The eqV2 entry sits on a different task with a zero-shot protocol and an empty train set and is a pretrained universal model, so it does not satisfy the training clause; on the Cu task's own page the claim beats the best value by 51.7%. This is a pass for a from-scratch, train-ids-only record on this task, not a claim of the lowest force MAE known on these structures, and the claim says so itself. Unverified: the eqV2 training data (the claim does not verify it either) and the ALIGNN 2.0 figure.

novelty: CONFIRMED against the task's live leaderboard page, in the from-scratch, train-ids-only category.
context: subagent (same VM)
pass: true
