import datetime as dt
from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.datasets import Dataset

"""
Exercise 7

We've built another DAG to create a report every time our data is updated.
Here we use a Dataset dependency instead of a sensor.

However, the dependency is not working correctly. Do you see what's wrong?
"""

data_ready = Dataset("s3://bucket_name/ingress/processed.csv")

# Processing DAG - produces the dataset
processing_dag = DAG(
    dag_id="7_processing_pipeline",
    description="Processes and stores data",
    default_args={"owner": "Processing Team"},
    schedule="@daily",
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2025, 1, 15),
)

with processing_dag:
    process = EmptyOperator(task_id="process_data")
    done = EmptyOperator(task_id="done", outlets=[data_ready])  # The task updates the dataset
    process >> done

# Reporting DAG - scheduled to run when the dataset is updated
reporting_dag = DAG(
    dag_id="7_solution_reporting_pipeline",
    description="Generates and sends reports",
    default_args={"owner": "Reporting Team"},
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2025, 1, 15),
)

with reporting_dag:
    report = EmptyOperator(task_id="generate_report")
    send = EmptyOperator(task_id="send_report")
    report >> send
