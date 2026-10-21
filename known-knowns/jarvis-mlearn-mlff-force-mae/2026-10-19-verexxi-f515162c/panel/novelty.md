# panel/novelty.md  (round 2: the claim folder now states the sibling-task values)

Files read (all inside the claim folder): CLAIM.md, the-record-we-beat/snapshot.md and the-record-we-beat/mlearnall_comparison.md.

Status page (fetched once, no retries): https://pages.nist.gov/jarvis_leaderboard/AI/MLFF/mlearn_Si_forces/ , HTTP 200, Date header Tue, 20 Oct 2026 12:20:42 GMT (2026-10-20T12:20:42Z), last modified 2025-08-25. Best listed value (chart data of the fetched HTML): alignnff_mlearn_wt1 0.06942387617720659 eV/A; next nequip_mlearn 0.0901 and alignnff_mlearn_all_wt1 0.0965. The page matches the folder's snapshot (same 11 entries and values); its sha256 differs, probably dynamic page content. Claimed 0.049536 is 28.6% below the best listed value: strictly lower, clears 5%, not a tie.

Repo (read-only): TROPHY_CASE.md on main has no mention of mlearn, jarvis or MLFF (0 matches). Open pull requests: about 281 scanned by title; exactly one concerns this target, the Mo claim (different element). No open Si PR found.

Literature (last 24 months): Zuo et al. 2020 uses its own split with figure-only errors; no from-scratch result on the mlearn Si test ids below 0.0495 was found (two web searches, not exhaustive); ALIGNN 2.0 lists 0.0872 for Si force (higher; pending verification).

Do the lower values defeat novelty? Decision of this skeptic: no, with an explicit scope limit. The sibling task mlearnall_Si_forces has `mlearn_analysis_Si_eqV2_153M_omat` at 0.012335 eV/A; restricted to the 25 official test ids it gives 0.013515, lower than 0.0495. The criterion defines the record to beat as the best MAE on that task's live page (mlearn_Si_forces) and requires training only on the train and val ids with no pretraining on data containing the test configurations; the eqV2 entry is a pretrained universal potential scored zero-shot on a different task with an empty train set (its training data may even include these structures; not verified), so it sits outside the protocol. The claim strictly beats everything known inside the criterion's protocol (from scratch, train ids only, task page); it does not beat everything known for these structures, and a reader who takes "everything known" to include zero-shot pretrained models gets a lower value, 0.0135. The claim keeps its caveat that it is not the lowest force MAE known for these structures (CLAIM.md says so); this skeptic judged the honest labelling sufficient for a pass. Training and reproducibility clauses were not verified here (outside novelty scope).

context: subagent (same VM)
pass: true
