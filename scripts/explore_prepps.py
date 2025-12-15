import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------
# 1. Load data
# -----------------------

CSV_PATH = "local_outputs/prepps_latam_clean.csv"
df = pd.read_csv(CSV_PATH)

print("Shape:", df.shape)
print(df.head())

# -----------------------
# 2. What countries are included?
# -----------------------

print("\nNumber of countries:", df["country"].nunique())
print(df["country"].value_counts())

# -----------------------
# 3. What dimensions are included?
# -----------------------

print("\nDimensions:")
print(df["dimensionname"].value_counts())

# -----------------------
# 4. Minimum quality filtering
# -----------------------

df_q = df[
    (df["n_pos"] >= 5) &
    (df["n_imp"] >= 5)
].copy()

print("\nAfter filtering by n_pos / n_imp >= 5")
print("Shape:", df_q.shape)

# -----------------------
# 5. Aggregation example:
#    Mean importance by dimension
# -----------------------

imp_by_dim = (
    df_q
    .groupby("dimensionname")["score_imp"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

print("\nMean importance by dimension:")
print(imp_by_dim)

# -----------------------
# 6. Visualization with seaborn
# -----------------------

plt.figure(figsize=(10, 6))
sns.barplot(
    data=imp_by_dim,
    x="score_imp",
    y="dimensionname"
)

plt.title("Mean Importance of Political Dimensions (PREPPS)")
plt.xlabel("Mean importance (score_imp)")
plt.ylabel("Dimension")

plt.tight_layout()
plt.show()
