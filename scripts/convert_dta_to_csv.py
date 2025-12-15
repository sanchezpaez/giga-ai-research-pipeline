import pyreadstat
import pandas as pd
import os
import json

INPUT = "data/PREPPS Latam V1.dta"
OUTDIR = "local_outputs"
os.makedirs(OUTDIR, exist_ok=True)

print("Reading .dta...")
# Try different encodings if the default fails
encodings = ['latin-1', 'utf-8', 'cp1252', 'iso-8859-1']
df, meta = None, None

for encoding in encodings:
    try:
        print(f"Trying encoding: {encoding}")
        df, meta = pyreadstat.read_dta(INPUT, encoding=encoding)
        print(f"Successfully read with encoding: {encoding}")
        break
    except Exception as e:
        print(f"Failed with {encoding}: {str(e)[:100]}")
        continue

if df is None:
    raise Exception("Could not read the file with any of the tried encodings")

# Normalize columns
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(".", "_")
    .str.replace("-", "_")
)

# Export CSV
csv_path = f"{OUTDIR}/prepps_latam_clean.csv"
df.to_csv(csv_path, index=False)
print(f"CSV generated at {csv_path}")

# Metadata
meta_path = f"{OUTDIR}/prepps_meta.json"
with open(meta_path, "w") as f:
    json.dump({
        "nrows": df.shape[0],
        "ncols": df.shape[1],
        "columns": list(df.columns),
        "file_source": INPUT,
    }, f, indent=2)

print(f"Metadata generated at {meta_path}")
