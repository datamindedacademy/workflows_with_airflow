import datetime as dt

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.sensors.external_task import ExternalTaskSensor

"""
Exercise 6

We've built a second DAG to create a report at 6 AM, based on data generated at midnight.
A sensor is used to check that the data processing was successful 
(we don't want to generate a report on incomplete data).

However, the sensor is not working correctly. Do you see what's wrong?
"""

processing_dag = DAG(
    dag_id="solution_6_processing_pipeline",
    description="Processes and stores data",
    default_args={"owner": "Processing Team"},
    schedule="@daily",
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
)

reporting_dag = DAG(
    dag_id="solution_6_reporting_pipeline",
    description="Generates and sends reports",
    default_args={"owner": "Reporting Team"},
    schedule="0 6 * * *",
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
)

with processing_dag:
    process = EmptyOperator(task_id="process_data")
    done = EmptyOperator(task_id="done")
    process >> done

with reporting_dag:
    sensor = ExternalTaskSensor(
        task_id="processing_done",
        external_dag_id="solution_6_processing_pipeline",
        external_task_id="done",
        deferrable=True,
        execution_delta=dt.timedelta(hours=6),
    )

    report = EmptyOperator(task_id="generate_report")
    send = EmptyOperator(task_id="send_report")
    sensor >> report >> send
