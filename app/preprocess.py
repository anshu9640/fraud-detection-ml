# app/preprocess.py

import pandas as pd

def preprocess_input(data: dict):
    """
    Convert incoming JSON to DataFrame and match format of training data.
    Add scaling/encoding here if used in training.
    """
    df = pd.DataFrame([data])
    return df
