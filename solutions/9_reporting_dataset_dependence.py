import datetime as dt
from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.datasets import Dataset

"""
Exercise 9 solution: Cross-DAG dependencies: datasets

`reporting_dag` was missing a `schedule` entirely, so it never ran.
Setting `schedule=[data_ready]` makes it schedule-on-dataset: a new run
is queued whenever `processing_dag`'s `done` task updates the
`data_ready` dataset via its `outlets`.
"""

data_ready = Dataset("s3://bucket_name/ingress/processed.csv")

# Processing DAG - produces the dataset
processing_dag = DAG(
    dag_id="solution_9_processing_pipeline",
    description="Processes and stores data",
    default_args={"owner": "Processing Team"},
    schedule="@daily",
    start_date=dt.datetime(2026, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
)

with processing_dag:
    process = EmptyOperator(task_id="process_data")
    done = EmptyOperator(task_id="done", outlets=[data_ready])  # The task updates the dataset
    process >> done

# Reporting DAG - scheduled to run when the dataset is updated
reporting_dag = DAG(
    dag_id="solution_9_reporting_pipeline",
    description="Generates and sends reports",
    default_args={"owner": "Reporting Team"},
    # No explicit schedule, this DAG is triggered by dataset update
    schedule=[data_ready],  # Triggered when the dataset is updated
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
)

with reporting_dag:
    report = EmptyOperator(task_id="generate_report")
    send = EmptyOperator(task_id="send_report")
    report >> send
