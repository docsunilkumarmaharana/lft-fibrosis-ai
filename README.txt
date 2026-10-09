# LFT Pattern Recognition + Fibrosis Risk AI: Synthetic Starter Dataset

## Files
- `lft_master_synthetic_5000.csv`: 5,000 synthetic records, one row per synthetic patient/encounter.
- `data_dictionary.csv`: field descriptions, units and caveats.
- `edge_case_tests.csv`: 10 deterministic cases for unit tests and input validation.
- `README.txt`: this guide.

## Provenance and limitations
Every row is synthetic. No real patient data are included. The cohort was generated programmatically for software development, teaching, pipeline testing, and prototyping. It is NOT a clinical cohort and must not be used to make clinical decisions, estimate real-world prevalence, or claim clinical model performance.

`synthetic_advanced_fibrosis_label` and `synthetic_metavir_stage` are artificial labels created from a simulated process. They are not derived from elastography, biopsy, or clinician adjudication. A model trained on them can only demonstrate that the software pipeline runs, not that fibrosis can be predicted accurately in real patients.

## Suggested use
1. Validate parsing, missing-value handling, unit handling and plausibility checks.
2. Recalculate FIB-4 and APRI independently and compare with stored calculated values (allow small rounding differences).
3. Develop a rule-based LFT pattern baseline.
4. Train a baseline model only as a technical demonstration. Exclude `patient_id`, `encounter_id`, `dataset_type`, `synthetic_scenario_source`, `suggested_split`, all target labels, and any derived score that would cause target leakage from model features as appropriate.
5. Preserve the suggested split or split by `data_split_group` to avoid leakage.
6. Replace synthetic outcome labels with a reliable reference standard before clinical prediction research.

## Important calculation notes
- FIB-4 = age × AST / (platelet count [10^9/L] × sqrt(ALT)).
- APRI = ((AST / AST ULN) × 100) / platelet count [10^9/L].
- The dataset assumes AST ULN = 40 U/L, ALT ULN = 40 U/L and ALP ULN = 120 U/L only for this synthetic exercise. Actual reference intervals depend on assay and laboratory.
- The R-ratio is a biochemical pattern tool, usually interpreted in an appropriate clinical/drug-induced liver injury context. The dataset's pattern labels are simplified synthetic labels, not definitive diagnoses.
- FIB-4/APRI cutoffs depend on population and clinical indication. Use current guidance and expert review before clinical use.

## Proposed project modules
A. Input validation and missingness report
B. LFT pattern classification
C. FIB-4/APRI calculator
D. Explainable baseline model and evaluation
E. Streamlit dashboard and exportable report
F. Later: external validation against real de-identified records with reliable fibrosis reference outcomes
