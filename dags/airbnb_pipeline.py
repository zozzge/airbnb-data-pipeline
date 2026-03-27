import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from scripts.extract_airbnb import extract_airbnb_data
from scripts.validate_airbnb import validate_airbnb_data
from scripts.clean_airbnb import clean_airbnb_data
from scripts.feature_engineering import add_features
from scripts.load_to_sqlite import load_to_sqlite
from scripts.data_quality_checks import run_quality_checks

def extract_task(**context):
    df = extract_airbnb_data()
    context["ti"].xcom_push(key="raw_rows", value=len(df))

# **context airflowun verdiği runtime bilgileri
# ti = TaskInstance, Airflow’daki o an çalışan task’ın temsilcisi
# .xcom Cross Communication taskler arası veri taşıma işlemi
# key="raw_rows" veriye bir isim veriyorum
# value=len(df) DataFramein satır sayısını gönderiyorsun

def validate_task():
    df = extract_airbnb_data()
    validate_airbnb_data(df)

def clean_task():
    df = extract_airbnb_data()
    df_clean = clean_airbnb_data(df)
    df_clean.to_csv("data/processed/airbnb_cleaned.csv", index=False)

def feature_task():
    df = pd.read_csv("data/processed/airbnb_cleaned.csv")
    df = add_features(df)
    df.to_csv("data/processed/airbnb_featured.csv", index=False)

def load_task():
    df = pd.read_csv("data/processed/airbnb_featured.csv")
    load_to_sqlite(df)

def quality_task():
    run_quality_checks()

with DAG(
    dag_id = "airbnb_pipeline_v2",
    start_date = datetime(2024, 1, 1),
    schedule_interval = "@daily",
    catchup = False,
    tags = ["airbnb", "etl", "sqlite", "portfolio"]
) as dag:
    
    extract = PythonOperator(
        task_id = "extract_airbnbb_data",
        python_callable = extract_task
    )

    validate = PythonOperator(
        task_id = "validate_airbnb_data",
        python_callable = validate_task
    )

    clean = PythonOperator(
        task_id = "clean_airbnb_data",
        python_callable = clean_task
    )

    feature_engineering = PythonOperator(
        task_id = "add_features",
        python_callable = feature_task
    )

    load = PythonOperator(
        task_id = "load_airbnb_data",
        python_callable = load_task
    )

    quality_check = PythonOperator(
        task_id = "run_quality_checks",
        python_callable = quality_task
    )

    extract >> validate >> clean >> feature_engineering >> load >> quality_check