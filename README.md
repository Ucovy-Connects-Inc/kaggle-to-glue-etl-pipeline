# Kaggle Glue ETL Pipeline

## Overview
This project demonstrates an end-to-end ETL pipeline using Kaggle datasets and AWS Glue.

## Flow
1. Download dataset from Kaggle using Kaggle API
2. Extract raw files locally
3. Convert JSON to CSV using AWS Glue
4. Read existing CSV from S3
5. Perform schema alignment and join
6. Write enriched dataset back to S3

## Status
Initial pipeline structure and Glue job scaffolding completed.
Further enhancements will include schema optimization and validations.
