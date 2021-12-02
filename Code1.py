# Databricks notebook source
default_name = "DefaultUnknown"

dbutils.widgets.text("name", default_name, "Please Enter user name saurabh shukla s")
user_name = dbutils.widgets.get("name")
if user_name == "DefaultUnknown":
  greeting = "ERROR"
else:
  greeting = f"Hello {user_name}"
  
dbutils.notebook.exit(greeting)

# COMMAND ----------

# just change
