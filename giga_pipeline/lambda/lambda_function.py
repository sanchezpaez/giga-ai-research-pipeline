import json
import boto3
import pandas as pd
import os

s3 = boto3.client("s3")

def lambda_handler(event, context):

    # --- 1. Extract S3 info from event ---
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # Work only on CSV files
    if not key.lower().endswith(".csv"):
        return {
            "status": "ignored",
            "reason": "Not a CSV file"
        }

    local_path = f"/tmp/{os.path.basename(key)}"

    # --- 2. Download CSV from S3 ---
    s3.download_file(bucket, key, local_path)

    # --- 3. Load CSV ---
    df = pd.read_csv(local_path)

    # --- 4. Basic quality check ---
    initial_rows = len(df)

    # Optional: filter by expert count if column exists
    if "n_pos" in df.columns:
        df = df[df["n_pos"] >= 5]

    # --- 5. Create summary statistics ---
    summary = {
        "file_source": f"s3://{bucket}/{key}",
        "rows_before_filtering": initial_rows,
        "rows_after_filtering": len(df),
        "num_columns": len(df.columns),
        "columns": list(df.columns),
        "numeric_columns": list(df.select_dtypes(include="number").columns),
        "sample_head": df.head(5).to_dict(orient="records")
    }

    # --- 6. Save outputs locally ---
    cleaned_csv_path = "/tmp/cleaned_prepps_latam.csv"
    summary_json_path = "/tmp/summary.json"

    df.to_csv(cleaned_csv_path, index=False)

    with open(summary_json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)

    # --- 7. Upload outputs to processed bucket ---
    output_bucket = "giga-processed-sandra"

    s3.upload_file(cleaned_csv_path, output_bucket, "cleaned_prepps_latam.csv")
    s3.upload_file(summary_json_path, output_bucket, "summary.json")

    return {
        "status": "success",
        "processed_file": key,
        "rows_after_filtering": len(df)
    }
