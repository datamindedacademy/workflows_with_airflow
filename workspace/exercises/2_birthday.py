import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise 2

Create a DAG which will run on your birthday to congratulate you.
"""

MY_NAME = ...
MY_BIRTHDAY = dt.datetime(...)

dag = DAG(
    dag_id="happy_birthday_v1",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule_interval="@yearly",
    start_date=...,
)

birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=f"echo 'Happy birthday {MY_NAME}!'",
)
