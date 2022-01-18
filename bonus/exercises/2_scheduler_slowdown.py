import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise

This DAG seems to take a long time to **load**. 
Can you figure out why, and how to fix it?
"""

# TODO: Load public dataset from S3 and process via pandas inside DAG

dag = DAG(
    dag_id="sleepy_task",
    description="Run a task which a certain delay",
    schedule_interval="@daily",
    start_date=dt.datetime(2021, 1, 1),
)


def waiting_task(seconds):
    import time
    time.sleep(seconds)

    return BashOperator(
        task_id="slow_task",
        bash_command=f"echo 'done after {seconds} seconds'"
    )


with dag:
    waiting_task(seconds=100)
