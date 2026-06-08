import os
import pandas as pd
import pickle

from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

df = pd.read_csv(
    os.path.join(
        BASE_DIR,
        "dataset",
        "final_dataset.csv"
    )
)

X = df.drop(
    ["filename", "delay_estimate"],
    axis=1
)

y = df["delay_estimate"]

model = pickle.load(
    open(
        os.path.join(
            BASE_DIR,
            "saved_models",
            "rf_model.pkl"
        ),
        "rb"
    )
)

pred = model.predict(X)

print("MAE =", mean_absolute_error(y, pred))
print("R2  =", r2_score(y, pred))