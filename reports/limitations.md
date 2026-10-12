# Project Limitations and Risk Disclosures
## Budget Overrun Early-Warning Model
**Author:** Bhupesh Chandra Dimri | Email: bhupesh7cd@gmail.com | October 2026

---

1. **Synthetic Data Constraint:** The primary dataset was generated synthetically (`seed=7`). Relationships represent stylized facts rather than verified historical institutional transactions.
2. **Observational vs. Causal Effects:** Regression coefficients and odds ratios quantify predictive associations. They do not prove that artificially capping a metric (such as overtime) will directly prevent an overrun without operational unintended consequences.
3. **Mid-Year Information Boundary:** Unforeseen policy changes, emergency appropriations, or fourth-quarter macro shocks occurring after the mid-year checkpoint fall outside the model's information set.
4. **General Ledger Integration:** Prior to production deployment, data pipelines must be integrated with SAP/Oracle ERP tables, validating accounting encumbrance tracking and commitment accounting logic.
