from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
def baseline(): return make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000,C=0.5))
def gbm(): return HistGradientBoostingClassifier(max_depth=3,learning_rate=0.06,max_iter=250,l2_regularization=1.0,
                                                  early_stopping=True,random_state=7)
