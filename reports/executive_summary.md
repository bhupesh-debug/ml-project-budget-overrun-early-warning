# Executive Summary: Budget Overrun Early-Warning Model
**Prepared for:** Chief Financial Officer & FP&A Leadership  
**Author:** Bhupesh Chandra Dimri | Email: bhupesh7cd@gmail.com | October 2026

---

### Executive Overview
Managing large enterprise or public agency budgets requires prioritizing review capacity. Historically, budget overruns are discovered in Q4 when mitigation options are limited. This project delivers an interpretable, auditable machine learning early-warning model that evaluates mid-year checkpoints to predict which budget lines will exceed their annual appropriation by >5%.

### Key Findings
1. **Model Superiority:** On an out-of-sample holdout test (FY4, 839 budget lines), our regularized Logistic Regression model achieved an **ROC-AUC of 0.906** and **PR-AUC of 0.777**, capturing **62.1% of all overruns within the top 20% flagged items**. This represents a **1.75x lift** over the legacy burn-gap rule (35.5% capture).
2. **Explainability Over Complexity:** Gradient Boosting achieved 0.899 ROC-AUC (61.6% capture), performing within sampling error of Logistic Regression. We recommend Logistic Regression as the production standard for controller auditability.
3. **Primary Early Warning Signals:** Overtime share (Odds Ratio 4.36x) and change orders YTD (Odds Ratio 2.95x) are the strongest operational predictors of year-end deficits.
4. **Substantial ROI:** Across a $1.2B budget pool, targeting the top 20% highest-risk lines avoids an estimated **$3.0M in unmitigated deficit exposure** annually, generating an ROI > 2,800% with a **1.4-month payback period**.
