"""
Glue Job: JSON to CSV Transformation

Reads nested JSON files from S3,
flattens the structure, and writes CSV output back to S3.

Actual transformation logic will be added
once dataset schema is finalized.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("json-to-csv-glue-job").getOrCreate()

# Placeholder paths
input_path = "s3://your-bucket/kaggle/raw/"
output_path = "s3://your-bucket/kaggle/processed/"

df = spark.read.json(input_path)

# Temporary flattening (simple select)
flattened_df = df.select("*")

flattened_df.write.mode("overwrite").csv(output_path)

spark.stop()
