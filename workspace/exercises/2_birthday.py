import datetime as dt

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

"""
Exercise 2: Scheduling basics

Create a DAG which will run on your birthday to congratulate you.

You'll practice: `schedule` presets vs. cron expressions, aligning
`start_date` with the schedule, and `catchup=False`.
"""

MY_NAME = ...
MY_BIRTHDAY = dt.datetime(...)

dag = DAG(
    dag_id="2_happy_birthday_v1",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule="@yearly",
    start_date=...,
    catchup=False
)

birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=f"echo 'Happy birthday, {MY_NAME}!'",
)
