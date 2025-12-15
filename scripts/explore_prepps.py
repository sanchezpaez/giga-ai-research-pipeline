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

# -----------------------
# 7. Position vs Importance
# -----------------------

DIM = "Taxes v. Spending"

df_lr = df_q[df_q["dimensionname"] == DIM]

print(f"\nObservations for {DIM}: {df_lr.shape}")

if df_lr.shape[0] == 0:
    print(f"WARNING: No data found for dimension '{DIM}'")
else:
    plt.figure(figsize=(7, 5))
    sns.scatterplot(
        data=df_lr,
        x="score_pos",
        y="score_imp",
        hue="country",
        alpha=0.7
    )

    plt.title("Position vs Importance\nTaxes v. Spending")
    plt.xlabel("Ideological position (score_pos)")
    plt.ylabel("Importance (score_imp)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

# -----------------------
# 8. Disagreement among experts
# -----------------------

sd_by_dim = (
    df_q
    .groupby("dimensionname")["sd_pos"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

print("\nMean disagreement by dimension:")
print(sd_by_dim)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=sd_by_dim,
    x="sd_pos",
    y="dimensionname"
)

plt.title("Mean Disagreement Among Experts by Dimension")
plt.xlabel("Mean standard deviation (sd_pos)")
plt.ylabel("Dimension")

plt.tight_layout()
plt.show()


