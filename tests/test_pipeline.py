"""
Automated unit and integration test suite for Budget Overrun Early-Warning Model
"""

import os
import pytest
import numpy as np
import pandas as pd
from src.data_pipeline import make_data
from src.feature_engineering import build_features
from src.model import baseline, gbm
from src.evaluate import metrics

def test_data_generation_shape_and_prevalence():
    df = make_data(n=1000, seed=42)
    assert len(df) == 1000
    assert 'overrun' in df.columns
    assert 0.20 <= df['overrun'].mean() <= 0.30

def test_feature_engineering_columns():
    df = make_data(n=500, seed=42)
    X, y = build_features(df)
    assert len(X) == 500
    assert 'burn_gap' in X.columns
    assert 'run_rate_projection_pct' in X.columns
    assert 'overtime_share' in X.columns
    assert (X['burn_gap'] == df['ytd_spend_pct'] - df['checkpoint_month']/12*100).all()

def test_baseline_logistic_model():
    df = make_data(n=800, seed=42)
    X, y = build_features(df)
    model = baseline()
    model.fit(X, y)
    probs = model.predict_proba(X)[:, 1]
    assert len(probs) == 800
    assert (probs >= 0.0).all() and (probs <= 1.0).all()
    res = metrics(y, probs, top=0.2)
    assert res['roc_auc'] >= 0.85
    assert res['recall_at_top20pct'] >= 0.50
