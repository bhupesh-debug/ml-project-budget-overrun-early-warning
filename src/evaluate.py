import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss
from sklearn.inspection import permutation_importance
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
def metrics(y,p,top=0.2):
    k=int(len(y)*top); idx=np.argsort(-p)[:k]
    return {"roc_auc":round(roc_auc_score(y,p),3),"pr_auc":round(average_precision_score(y,p),3),
            "brier":round(brier_score_loss(y,p),3),"recall_at_top20pct":round(y.values[idx].sum()/y.sum(),3)}
def importance_chart(model,X,y,path):
    r=permutation_importance(model,X,y,n_repeats=5,random_state=7,scoring="roc_auc")
    s=sorted(zip(X.columns,r.importances_mean),key=lambda t:t[1])[-10:]
    plt.figure(figsize=(7,4)); plt.barh([a for a,_ in s],[b for _,b in s],color="#1F3864")
    plt.title("Top drivers of year-end overrun risk (permutation importance, AUC drop)"); plt.tight_layout(); plt.savefig(path,dpi=130); plt.close()
    return [(a,round(float(b),4)) for a,b in s[::-1]]
