# Simulation Suite and Scenario Analysis Report

## 1. Review Capacity Stress Test

| Capacity   |   Lines Reviewed |   Overruns Captured |   Total Overruns | Recall   | Precision   | Lift   |
|:-----------|-----------------:|--------------------:|-----------------:|:---------|:------------|:-------|
| 10%        |               83 |                  73 |              203 | 36.0%    | 88.0%       | 3.64x  |
| 20%        |              167 |                 126 |              203 | 62.1%    | 75.4%       | 3.12x  |
| 30%        |              251 |                 151 |              203 | 74.4%    | 60.2%       | 2.49x  |
| 40%        |              335 |                 180 |              203 | 88.7%    | 53.7%       | 2.22x  |

> **Key Takeaway:** Reviewing the top 20% of flagged budget lines captures **62.1% of all overruns** with a **3.1x lift** over random selection. Reviewing the top 40% captures nearly **80% of all overruns**.

## 2. Operational Driver Stress & Intervention Scenarios

- **Baseline Portfolio Mean Risk:** 26.3%
- **Adverse Shock (+30% overtime, +50% change orders):** 41.9% (Relative Risk Surge: +59.3%)
- **Governance Intervention (Capping change orders & overtime):** 17.2% (**Systemic Risk Reduction: -34.4%**)

## 3. 5,000-Run Monte Carlo Portfolio Financial Exposure

- **Total Agency Budget Evaluated:** $5,859.11M
- **Median Unmitigated Overrun Exposure:** $168.88M (Range: $117.34M - $241.25M)
- **Median Incremental Avoided Overrun (vs. Rule):** **$17.48M** annually (10th percentile floor: $12.00M)
