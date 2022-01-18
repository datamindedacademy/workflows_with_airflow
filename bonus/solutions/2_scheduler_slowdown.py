import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise

This DAG seems to take a long time to **load**. 
Can you figure out why, and how to fix it?
"""

dag = DAG(
    dag_id="sleepy_task",
    description="Run a task which a certain delay",
    schedule_interval="@daily",
    start_date=dt.datetime(2021, 1, 1),
)


def waiting_task(seconds):
    """Importing time was not actually needed at all!"""
    return BashOperator(
        task_id="slow_task",
        bash_command=f"sleep {seconds}; echo 'done after {seconds} seconds'"
    )


with dag:
    waiting_task(seconds=100)
