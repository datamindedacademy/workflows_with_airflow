import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise 2
Create a DAG which will run on your birthday to congratulate you.
"""

MY_NAME = "Gert Verhulst"
MY_BIRTHDAY = dt.datetime(year=1968, month=1, day=24)

dag = DAG(
    dag_id="happy_birthday",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule_interval="0 0 24 1 *",
    start_date=MY_BIRTHDAY,
)

birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=f"echo 'happy birthday {MY_NAME}!'"
)
