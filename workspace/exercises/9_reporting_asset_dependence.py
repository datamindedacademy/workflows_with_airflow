import datetime as dt
from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.sdk import Asset

"""
Exercise 9: Cross-DAG dependencies: assets

We've built another DAG to create a report every time our data is
updated. Here we use a Asset dependency instead of a sensor.

You'll practice: event-driven, data-aware scheduling via
`Asset`/outlets -- a DAG that reacts to data becoming available, in
contrast to every earlier exercise's interval-based `schedule=`
cron/preset.

However, the dependency is not working correctly. Do you see what's
wrong?
"""

data_ready = Asset("s3://bucket_name/ingress/processed.csv")

# Processing DAG - produces the asset
processing_dag = DAG(
    dag_id="9_processing_pipeline",
    description="Processes and stores data",
    default_args={"owner": "Processing Team"},
    schedule="@daily",
    start_date=dt.datetime(2026, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
)

with processing_dag:
    process = EmptyOperator(task_id="process_data")
    done = EmptyOperator(task_id="done", outlets=[data_ready])  # The task updates the asset
    process >> done

# Reporting DAG - scheduled to run when the asset is updated
reporting_dag = DAG(
    dag_id="9_solution_reporting_pipeline",
    description="Generates and sends reports",
    default_args={"owner": "Reporting Team"},
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
)

with reporting_dag:
    report = EmptyOperator(task_id="generate_report")
    send = EmptyOperator(task_id="send_report")
    report >> send
