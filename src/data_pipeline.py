import numpy as np, pandas as pd
def make_data(n=3200, seed=7):
    """Synthetic mid-year budget checkpoints for agency units (4 fiscal years)."""
    r=np.random.default_rng(seed)
    d=pd.DataFrame({
        "unit_id":np.arange(n),
        "fiscal_year":r.integers(1,5,n),
        "unit_type":r.choice(["labor","non_labor","capital"],n,p=[.45,.4,.15]),
        "budget_m":np.round(r.lognormal(1.6,.9,n),2),
        "checkpoint_month":r.integers(3,10,n),
    })
    d["ytd_spend_pct"]=np.clip(d.checkpoint_month/12*100+r.normal(0,9,n),5,110).round(1)
    d["prior_year_variance_pct"]=r.normal(1.5,5,n).round(1)
    d["vacancy_rate"]=np.clip(r.beta(2,12,n),0,.5).round(3)
    d["overtime_share"]=np.clip(r.beta(2,9,n),0,.6).round(3)
    d["vendor_spend_share"]=np.clip(r.beta(3,3,n),0,1).round(3)
    d["change_orders_ytd"]=r.poisson(1.2,n)
    d["one_time_share"]=np.clip(r.beta(1.5,10,n),0,.5).round(3)
    d["forecast_revisions"]=r.poisson(1.5,n)
    burn=d.ytd_spend_pct-d.checkpoint_month/12*100
    z=(0.07*burn+0.11*d.prior_year_variance_pct+4.5*d.overtime_share+0.35*d.change_orders_ytd
       -5*d.vacancy_rate*(d.unit_type=="labor")+2.2*d.vendor_spend_share*(d.unit_type=="non_labor")
       +0.12*d.forecast_revisions-3*d.one_time_share+r.normal(0,1.1,n))
    d["overrun"]=(z>np.quantile(z,.75)).astype(int)
    return d
