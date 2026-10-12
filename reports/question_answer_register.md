# Question and Answer Register
## Budget Overrun Early-Warning Model
**Author:** Bhupesh Chandra Dimri | Email: bhupesh7cd@gmail.com | October 2026

---

### Q-01: Which budget lines deserve immediate attention at mid-year?
- **Answer:** Budget lines with high overtime share (>25%), frequent change orders (>=2), and a positive burn gap (spending ahead of calendar by >5%) represent >60% of all subsequent budget overruns.
- **Evidence:** `reports/regression_analysis.md`, `reports/simulation_report.md`.
- **Recommendation:** Route these lines into the Top 20% review queue for proactive mitigation.

### Q-02: Which features are the strongest risk indicators?
- **Answer:** In order of empirical importance: (1) `overtime_share` (Odds Ratio 4.36x), (2) `change_orders_ytd` (Odds Ratio 2.95x), (3) `prior_year_variance_pct` (Odds Ratio 1.20x), and (4) `burn_gap` (Odds Ratio 1.32x).
- **Evidence:** Permutation importance analysis (`reports/feature_importance.png`) and Logistic regression coefficients.

### Q-03: Does logistic regression outperform the existing heuristic?
- **Answer:** Yes, substantially. Logistic regression achieves an ROC-AUC of 0.906 and PR-AUC of 0.777, capturing **62.1% of all overruns in the top 20% flagged items**, compared to only **35.5%** for the legacy burn-gap rule (a 1.75x improvement in analyst efficiency).

### Q-04: Is gradient boosting worth the additional complexity?
- **Answer:** No. HistGradientBoosting achieved an ROC-AUC of 0.899 and captured 61.6% of overruns, performing within statistical noise of logistic regression. Logistic regression is preferred because controllers can audit its explicit odds ratios.

### Q-05: How much risk can be identified at a fixed review capacity?
- **Answer:** At 10% capacity: captures 36.8% of overruns. At 20% capacity: captures 62.1% of overruns. At 30% capacity: captures 72.4% of overruns. At 40% capacity: captures 79.8% of overruns.
- **Evidence:** `reports/simulation_report.md` Section 1.

### Q-06: What preventive actions should finance managers consider?
- **Answer:** (1) Imposing mid-year overtime authorization caps; (2) Freezing non-essential change orders; (3) Reallocating uncommitted balances from under-burning capital lines.

### Q-07: What data would improve the predictions?
- **Answer:** Granular vendor invoice submission dates, committed purchase order backlogs, and seasonal hiring requisition lead times.

### Q-08: What evidence is required before real operational use?
- **Answer:** A 2-quarter parallel shadow run with agency budget analysts to calibrate threshold sensitivity against live ERP feeds.
