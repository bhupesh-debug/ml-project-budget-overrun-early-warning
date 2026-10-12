# Model Card: Budget Overrun Early-Warning Model (SR 11-7 Aligned)
**Target Organization:** Corporate Finance / Budgeting & Financial Planning (FP&A)  
**Author:** Bhupesh Chandra Dimri | Email: bhupesh7cd@gmail.com | October 2026

---

### 1. Model Overview & Purpose
- **Model Name:** Agency Budget Overrun Early-Warning Scorer
- **Model Architecture:** Regularized Binary Logistic Regression (Pipeline with StandardScaler)
- **Primary Objective:** Predict whether an agency budget line will exceed its approved annual allocation by > 5% at year-end, based on mid-year checkpoint attributes.
- **Intended Scope:** Government agencies, corporate departments, and commercial business units managing multi-year budgeting lines.

---

### 2. Quantitative Performance & Validation (Holdout FY4, N=839)
- **ROC-AUC:** 0.906 (Selected Model) vs 0.686 (Burn-Gap Rule Heuristic)
- **PR-AUC:** 0.777 vs 0.435
- **Brier Calibration Score:** 0.103
- **Top 20% Capacity Recall:** **62.1%** (157 / 253 overruns captured) vs 35.5% for rule heuristic (3.10x lift over random).
- **Benchmark Against Gradient Boosting:** Gradient Boosting achieved 0.899 ROC-AUC and 0.763 PR-AUC. The difference is within statistical noise. Logistic regression is chosen for regulatory auditability and parameter transparency.

---

### 3. Key Feature Drivers & Econometric Odds Ratios
1. `vendor_dup_flag` / `overtime_share`: Odds Ratio > 4.3x (p < 0.0001)
2. `change_orders_ytd`: Odds Ratio > 2.9x (p < 0.0001)
3. `mapping_stale_flag` / `burn_gap`: Odds Ratio > 1.3x (p < 0.0001)
4. `prior_year_variance_pct`: Odds Ratio > 1.2x (p < 0.0001)

---

### 4. Governance & Monitoring
- **Weekly Population Stability Index (PSI)** and drift checks on overtime and change order distributions.
- Retraining triggered if PR-AUC falls below 0.70 across consecutive fiscal quarters.
