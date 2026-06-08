import os
import pandas as pd
import pickle

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("MAE =", mean_absolute_error(y_test, pred))
print("R2  =", r2_score(y_test, pred))

pickle.dump(
    model,
    open(
        os.path.join(
            BASE_DIR,
            "saved_models",
            "xgb_model.pkl"
        ),
        "wb"
    )
)

print("\nXGB Model Saved!")