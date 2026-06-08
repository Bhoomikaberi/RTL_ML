import pandas as pd

features = pd.read_csv("rtl_features.csv")
yosys = pd.read_csv("yosys_stats.csv")

final = pd.merge(
    features,
    yosys,
    on="filename"
)

final["delay_estimate"] = (
    final["depth"] * 0.5
    + final["cell_count"] * 0.05
    + final["wire_count"] * 0.002
)

final.to_csv(
    "final_dataset.csv",
    index=False
)

print(final.head())
print("\nFinal Dataset Created!")