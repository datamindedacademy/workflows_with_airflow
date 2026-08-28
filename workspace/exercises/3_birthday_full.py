from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from pendulum import datetime

"""
Exercise 3: Templating with Jinja

Extend your previous result to also print your age.

You'll practice: Jinja-templated fields, and using `data_interval_end`
-- the DAG's logical run time, not wall-clock "now" -- inside a
template. Hold onto that distinction: the next exercise punishes
forgetting it.
"""


MY_NAME = "Barack Obama"
MY_BIRTHDAY = datetime(year=1961, month=8, day=4, tz="Pacific/Honolulu")

dag = DAG(
    dag_id="3_happy_birthday_v2",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule="0 0 4 8 *",
    start_date=MY_BIRTHDAY,
    catchup=False,
)


def years_today():
    """Returns how old you are at this moment"""
    return 0  # TODO: create a working implementation


birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=(
        f"echo 'Happy birthday, {MY_NAME}! "
        f"You are {years_today()} years old today!'"
    ),
)
