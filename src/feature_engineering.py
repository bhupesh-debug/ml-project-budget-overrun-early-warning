import pandas as pd
NUM=["budget_m","ytd_spend_pct","checkpoint_month","prior_year_variance_pct","vacancy_rate","overtime_share",
     "vendor_spend_share","change_orders_ytd","one_time_share","forecast_revisions","burn_gap","run_rate_projection_pct"]
def build_features(d):
    x=d.copy()
    x["burn_gap"]=x.ytd_spend_pct-x.checkpoint_month/12*100          # spending ahead of the calendar
    x["run_rate_projection_pct"]=x.ytd_spend_pct/(x.checkpoint_month/12)  # naive full-year projection
    x=pd.concat([x,pd.get_dummies(x.unit_type,prefix="type").astype(int)],axis=1)
    cols=NUM+[c for c in x.columns if c.startswith("type_")]
    return x[cols], x["overrun"]
