import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure(figsize=(10,5))

plt.bar(
    X.columns,
    model.feature_importances_
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        BASE_DIR,
        "visualization",
        "plots",
        "feature_importance.png"
    )
)

plt.show()