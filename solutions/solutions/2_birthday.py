import datetime as dt

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

"""
Exercise 2

Create a DAG which will run on your birthday to congratulate you.
"""

MY_NAME = "Barack Obama"
MY_BIRTHDAY = dt.datetime(year=1961, month=8, day=4)

dag = DAG(
    dag_id="solution_2_happy_birthday_v1",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule="0 0 4 8 *",
    start_date=MY_BIRTHDAY,
    catchup=False,
)

birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=f"echo 'Happy birthday, {MY_NAME}!'",
)
