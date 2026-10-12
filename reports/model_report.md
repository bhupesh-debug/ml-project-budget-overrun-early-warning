# Model Validation and Performance Report

- **Total Rows:** 3,200 | **Overrun Prevalence:** 25.0%
- **Test Holdout (FY4):** 839 rows

### Primary Model Benchmarking Results

| Model | ROC-AUC | PR-AUC | Brier Score | Recall in Top 20% Flagged |
| :--- | :---: | :---: | :---: | :---: |
| **Burn-Gap Rule (Heuristic)** | 0.686 | 0.435 | 0.185 | 35.5% |
| **Logistic Regression (Selected)** | **0.906** | **0.777** | **0.103** | **62.1%** |
| **Gradient Boosting** | 0.899 | 0.763 | 0.105 | 61.6% |

> **Recommendation:** Logistic Regression is the recommended production model due to statistical equivalence with Gradient Boosting and full parameter auditability under SR 11-7 standards.
