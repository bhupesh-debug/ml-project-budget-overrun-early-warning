# Data Dictionary: Budget Overrun Early-Warning Dataset
**Project:** Budget Overrun Early-Warning Scorer | **Author:** Bhupesh Chandra Dimri | **Version:** 1.0

---

| Column Name | Type | Logical Type | CDE? | Valid Range | Description |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `unit_id` | Integer | Identifier | Yes | 0 to 3,199 | Unique operational budget line identifier |
| `fiscal_year` | Integer | Temporal | Yes | 1 to 4 | Fiscal year cohort (FY1-3 Train, FY4 Test) |
| `unit_type` | Categorical | Segment | Yes | `labor`, `non_labor`, `capital` | Expenditure classification of budget line |
| `budget_m` | Numeric | Monetary ($M) | Yes | $0.1M to $50.0M | Total annual approved baseline budget in millions |
| `checkpoint_month` | Integer | Temporal | Yes | 3 to 9 (Month) | Mid-year checkpoint observation month |
| `ytd_spend_pct` | Numeric | Percentage | Yes | 5.0% to 110.0% | Year-to-date cumulative actual spend as % of annual budget |
| `prior_year_variance_pct`| Numeric | Percentage | Yes | -15.0% to +25.0% | Final percentage variance from prior fiscal year budget |
| `vacancy_rate` | Numeric | Ratio | No | 0.00 to 0.50 | Current unfilled FTE staffing vacancy rate |
| `overtime_share` | Numeric | Ratio | Yes | 0.00 to 0.60 | Overtime expenditure as fraction of total labor budget |
| `vendor_spend_share` | Numeric | Ratio | Yes | 0.00 to 1.00 | Third-party contractor spend as fraction of budget |
| `change_orders_ytd` | Integer | Count | Yes | 0 to 10 | Approved contract change orders year-to-date |
| `one_time_share` | Numeric | Ratio | No | 0.00 to 0.50 | Fraction of expenditure allocated to non-recurring items |
| `forecast_revisions` | Integer | Count | No | 0 to 8 | Number of formal mid-year forecast revisions submitted |
| `burn_gap` | Numeric | Derived | Yes | -40.0% to +40.0% | Difference between actual spend % and calendar elapsed % |
| `run_rate_projection_pct`| Numeric| Derived | Yes | 10.0% to 250.0% | Annualized run-rate projection of spend |
| `overrun` | Binary | Target | Yes | 0 or 1 | Ground truth label (1 = year-end spend exceeds budget by > 5%) |
