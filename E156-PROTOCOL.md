# E156 Protocol — `Inclisiran-LivingMeta`

This repository is the source code and dashboard backing a cluster of E156 micro-papers on the [E156 Student Board](https://mahmood726-cyber.github.io/e156/students.html).

**2 papers share this repo.** Each is listed below with its own title, estimand, dataset, 156-word body, and submission metadata (authorship, ethics, references, target journal, etc.). Students claiming any of these papers should use the body + metadata for their specific paper number and submit separately.

## Papers in this repo

| Paper # | Title |
| ---: | :--- |
| `[362]` | Inclisiran siRNA PCSK9: A Transparent Living Meta-Analysis v13 |
| `[409]` | Inclisiran for LDL Cholesterol Lowering: Living Meta-Analysis of Randomized Trials |

---

## `[362]` Inclisiran siRNA PCSK9: A Transparent Living Meta-Analysis v13

**Type:** methods  |  ESTIMAND: RR  
**Data:** ClinicalTrials.gov, PubMed, OpenAlex

### 156-word body

Can a browser-based transparent living meta-analysis reproduce published pooled estimates for inclisiran siRNA PCSK9 therapy for LDL reduction? The v13 app ingested 4 RCTs from ClinicalTrials.gov cross-checked against PubMed and OpenAlex. DerSimonian-Laird random-effects pooling with HKSJ correction ran in-browser on the logged risk ratio, with cumulative, provenance, QA, and cross-validation engines logging every step. The pooled risk ratio was concordant with the Qiao 2026 ORION-pooled benchmark within lockdown tolerance, and estimates update live as trials are ingested. Cross-validation against R metafor and Python scipy scripts reproduced the pooled point estimate, and leave-one-out plus REML-versus-HKSJ sensitivity preserved direction. A transparent browser-native pipeline matches benchmark pooled effects for inclisiran siRNA PCSK9 therapy for LDL reduction without server-side computation while surfacing every provenance decision. The app inherits CT.gov and PubMed coverage gaps, cannot synthesize unpublished data, and updates require manual re-ingestion.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/Inclisiran-LivingMeta
  Protocol:  https://github.com/mahmood726-cyber/Inclisiran-LivingMeta/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/inclisiran_livingmeta/

References (topic pack: heterogeneity / prediction interval):
  1. Higgins JPT, Thompson SG. 2002. Quantifying heterogeneity in a meta-analysis. Stat Med. 21(11):1539-1558. doi:10.1002/sim.1186
  2. IntHout J, Ioannidis JP, Rovers MM, Goeman JJ. 2016. Plea for routinely presenting prediction intervals in meta-analysis. BMJ Open. 6(7):e010247. doi:10.1136/bmjopen-2015-010247

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020 (methods-paper variant — reports on review corpus).

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Methods Note — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```

---

## `[409]` Inclisiran for LDL Cholesterol Lowering: Living Meta-Analysis of Randomized Trials

**Type:** living-ma  |  ESTIMAND: HR for major adverse cardiovascular events  
**Data:** 3 RCTs (ORION-9, ORION-10, ORION-11), 3,660 patients, CT.gov sourced

### 156-word body

Does inclisiran, a small interfering RNA targeting hepatic PCSK9 messenger RNA, reduce major adverse cardiovascular events in patients with established atherosclerotic disease or familial hypercholesterolemia? Three randomized phase 3 trials enrolling 3,660 patients with elevated LDL cholesterol despite maximum tolerated statin therapy compared subcutaneous inclisiran twice yearly against placebo. DerSimonian-Laird random-effects meta-analysis pooled hazard ratios on the log scale with HKSJ correction. The pooled hazard ratio for cardiovascular events was 0.77 (95% CI 0.56-1.07), with no detectable heterogeneity (I-squared 0%) across heterozygous familial hypercholesterolemia and ASCVD populations. Pooled LDL cholesterol reduction was approximately 50 percent versus placebo, consistent across all three trials. Inclisiran reliably lowers LDL cholesterol with semi-annual dosing, but the cardiovascular outcome estimate remains imprecise pending the larger ORION-4 trial. Long-term cardiovascular benefit is unproven, cost-effectiveness is contested, and twice-yearly injection logistics may not suit all health systems.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/Inclisiran-LivingMeta
  Protocol:  https://github.com/mahmood726-cyber/Inclisiran-LivingMeta/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/inclisiran_livingmeta/

References (topic pack: restricted mean survival time / survival meta-analysis):
  1. Royston P, Parmar MK. 2013. Restricted mean survival time: an alternative to the hazard ratio for the design and analysis of randomized trials with a time-to-event outcome. BMC Med Res Methodol. 13:152. doi:10.1186/1471-2288-13-152
  2. Tierney JF, Stewart LA, Ghersi D, Burdett S, Sydes MR. 2007. Practical methods for incorporating summary time-to-event data into meta-analysis. Trials. 8:16. doi:10.1186/1745-6215-8-16

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020.

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Short Meta-Analysis — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```


---

_Auto-generated from the workbook by `C:/E156/scripts/create_missing_protocols.py`. If something is wrong, edit `rewrite-workbook.txt` and re-run the script — it will overwrite this file via the GitHub API._