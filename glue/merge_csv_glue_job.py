"""
Glue Job: Merge Kaggle CSV with Existing CSV

Steps:
- Read Kaggle CSV from S3
- Read existing CSV from S3
- Align schemas
- Join datasets on key
- Write enriched dataset to S3
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("merge-csv-glue-job").getOrCreate()

kaggle_csv_path = "s3://your-bucket/kaggle/processed/"
existing_csv_path = "s3://your-bucket/existing/data.csv"
output_path = "s3://your-bucket/output/enriched/"

kaggle_df = spark.read.option("header", "true").csv(kaggle_csv_path)
existing_df = spark.read.option("header", "true").csv(existing_csv_path)

# Example join key
joined_df = kaggle_df.join(
    existing_df,
    kaggle_df["id"] == existing_df["id"],
    "left"
)

joined_df.write.mode("overwrite").csv(output_path)

spark.stop()
