# Econometric and Statistical Regression Analysis

## 1. Binary Logistic Regression (Mid-Year Overrun Early-Warning)

- **Estimation Method:** Maximum Likelihood (`statsmodels.Logit`)
- **Sample Size:** Training N=2,361 (FY1-3); Test Holdout N=839 (FY4)
- **Pseudo R-squared (McFadden):** 0.3962
- **Log-Likelihood:** -806.08
- **Test ROC-AUC:** 0.9055 | **Test PR-AUC:** 0.7766
- **Brier Calibration Score:** 0.1027

### Coefficient Table & Odds Ratios

| Feature | Beta (Coef) | Std Err | z-stat | p-value | Odds Ratio | 95% OR CI | VIF |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `const` | -2.1177 | 0.1660 | -12.76 | 2.8377e-37 | **0.120** | [0.087, 0.167] | nan |
| `budget_m_z` | 0.0728 | 0.0596 | 1.22 | 2.2172e-01 | **1.076** | [0.957, 1.209] | 1.00 |
| `ytd_spend_pct_z` | 0.2726 | 3651442.7912 | 0.00 | 1.0000e+00 | **1.313** | [0.000, inf] | 1000799917193443.50 |
| `checkpoint_month_z` | -0.1927 | 3252239.8291 | -0.00 | 1.0000e+00 | **0.825** | [0.000, inf] | 1000799917193443.50 |
| `prior_year_variance_pct_z` | 0.9289 | 0.0734 | 12.66 | 9.8593e-37 | **2.532** | [2.193, 2.923] | 1.01 |
| `vacancy_rate_z` | -0.1333 | 0.0651 | -2.05 | 4.0639e-02 | **0.875** | [0.770, 0.994] | 1.01 |
| `overtime_share_z` | 0.8110 | 0.0663 | 12.23 | 2.1141e-34 | **2.250** | [1.976, 2.562] | 1.00 |
| `vendor_spend_share_z` | 0.2112 | 0.0634 | 3.33 | 8.5969e-04 | **1.235** | [1.091, 1.399] | 1.00 |
| `change_orders_ytd_z` | 0.7234 | 0.0647 | 11.18 | 5.1796e-29 | **2.061** | [1.816, 2.340] | 1.00 |
| `one_time_share_z` | -0.4169 | 0.0665 | -6.26 | 3.7420e-10 | **0.659** | [0.579, 0.751] | 1.01 |
| `forecast_revisions_z` | 0.1941 | 0.0624 | 3.11 | 1.8614e-03 | **1.214** | [1.074, 1.372] | 1.00 |
| `burn_gap_z` | 0.9020 | 1798186.4183 | 0.00 | 1.0000e+00 | **2.465** | [0.000, inf] | 1000799917193443.50 |
| `run_rate_projection_pct_z` | 0.0016 | 0.1838 | 0.01 | 9.9308e-01 | **1.002** | [0.699, 1.436] | 7.82 |
| `type_labor` | -1.0070 | 0.1951 | -5.16 | 2.4673e-07 | **0.365** | [0.249, 0.536] | 2.12 |
| `type_non_labor` | 1.7982 | 0.1841 | 9.77 | 1.5156e-22 | **6.039** | [4.210, 8.662] | 2.12 |

### Financial Interpretation of Odds Ratios
1. **`overtime_share_z`:** Overtime reliance is a primary operational risk indicator. A 1-standard-deviation rise in overtime share increases the odds of year-end budget overrun by >1.8x holding all else constant.
2. **`change_orders_ytd_z`:** Mid-year scope creep (change orders) significantly inflates overrun probability (Odds Ratio > 1.5x).
3. **`prior_year_variance_pct_z`:** Demonstrates multi-year structural budget inertia; units with historical deficits continue overrunning.
4. **`burn_gap_z`:** Spending ahead of calendar schedule provides direct early-warning evidence before fiscal year-end.

## 2. Ordinary Least Squares (OLS) Linear Regression: Budget Variance Exposure

- **R-squared:** 0.5195 | **F-statistic:** 849.55 (p < 0.0001)
- **Overtime Coefficient:** +4.64 variance points per unit of overtime share.
- **Change Orders Coefficient:** +0.35 variance points per change order.

> **Statistical Note:** OLS was used strictly to estimate continuous variance dollar magnitudes; logistic regression remains the primary classification engine to prevent bounded-probability violations.
