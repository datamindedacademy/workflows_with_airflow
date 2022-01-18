import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise 2.5

Extend your previous result to also print your age.
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


def years_today():
    """Returns how old you are at this moment"""
    return "{{ macros.dateutil.relativedelta(data_interval_end, macros.datetime.datetime(1968, 1, 24)).years }}"


birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=(
        f"echo 'happy birthday {MY_NAME}! "
        f"You are {years_today()} years old today!'"
    )
)
