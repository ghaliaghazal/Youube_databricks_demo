# Databricks notebook source
# MAGIC %md
# MAGIC # EDA on supply chain

# COMMAND ----------

## TODO: list the volume of data in the database
VOLUME_PATH = "Volumes/supply_chain_demo/default/raw"

spark.sql(f"LIST '{VOLUME_PATH}'").display()
