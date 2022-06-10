import datetime as dt

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.sensors.external_task import ExternalTaskSensor

"""
Exercise 6

We've built a second DAG to create a report at 6 AM, based on data generated at midnight.
A sensor is used to check that the data processing was successful 
(we don't want to generate a report on incomplete data).

However, the sensor is not working correctly. Do you see what's wrong?
"""

processing_dag = DAG(
    dag_id="processing_pipeline",
    description="Processes and stores data",
    default_args={"owner": "Processing Team"},
    schedule_interval="@daily",
    start_date=dt.datetime(2021, 1, 1),
    end_date=dt.datetime(2021, 1, 15),
)

reporting_dag = DAG(
    dag_id="reporting_pipeline",
    description="Generates and sends reports",
    default_args={"owner": "Reporting Team"},
    schedule_interval="0 6 * * *",
    start_date=dt.datetime(2021, 1, 1),
    end_date=dt.datetime(2021, 1, 15),
)

with processing_dag:
    process = DummyOperator(task_id="process_data")
    done = DummyOperator(task_id="done")
    process >> done

with reporting_dag:
    sensor = ExternalTaskSensor(
        task_id="processing_done",
        external_dag_id="processing_pipeline",
        external_task_id="done",
    )

    report = DummyOperator(task_id="generate_report")
    send = DummyOperator(task_id="send_report")
    sensor >> report >> send
