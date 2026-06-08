import os
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

corr = df.corr(
    numeric_only=True
)

plt.figure(figsize=(10,8))

plt.imshow(corr)

plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=90
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        BASE_DIR,
        "visualization",
        "plots",
        "correlation.png"
    )
)

plt.show()