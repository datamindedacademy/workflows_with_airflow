from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from pendulum import datetime

"""
Exercise 3 solution: Templating with Jinja

`years_today()` returns a Jinja template string instead of a plain
value, so it's evaluated at task-run time using `data_interval_end` (the
DAG's logical run date) rather than at parse time. Because the schedule
only ever fires on the birthday's month/day, a plain year subtraction
gives the same answer as a full relativedelta -- no extra library
needed.
"""


MY_NAME = "Barack Obama"
MY_BIRTHDAY = datetime(year=1961, month=8, day=4, tz="Pacific/Honolulu")

dag = DAG(
    dag_id="solution_3_happy_birthday_v2",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule="0 0 4 8 *",
    start_date=MY_BIRTHDAY,
    catchup=False,
)


def years_today():
    """Returns how old you are at this moment"""
    # The DAG only ever runs on the birthday's month/day, so a plain
    # year subtraction gives the same result as a full relativedelta.
    return "{{ data_interval_end.year - dag.start_date.year }}"


birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=(
        f"echo 'Happy birthday, {MY_NAME}! "
        f"You are {years_today()} years old today!'"
    ),
)
