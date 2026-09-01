import pendulum
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

"""
Exercise 2 solution: Scheduling basics

Uses an explicit cron expression ("0 0 4 8 *") instead of the `@yearly`
preset. `@yearly` is fixed to "0 0 1 1 *" (midnight, January 1st)
regardless of `start_date` -- it does not run on the anniversary of
`start_date` -- so it can never fire on an August birthday.
"""

MY_NAME = "Barack Obama"
MY_BIRTHDAY = pendulum.datetime(1961, 8, 4, tz="Pacific/Honolulu")

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
