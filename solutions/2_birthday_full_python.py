from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import dateutil
from pendulum import datetime

"""
Exercise 2.5

Extend your previous result to also print your age.
"""


MY_NAME = "Barack Obama"
MY_BIRTHDAY = datetime(year=1961, month=8, day=4, tz="Pacific/Honolulu")


dag = DAG(
    dag_id="solution_2_happy_birthday_python_v3",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule="0 13 8 5 *",
    start_date=MY_BIRTHDAY,
    catchup=False,
)


def years_today(name, dag, data_interval_end):
    """Prints how old you are at this moment"""
    years = dateutil.relativedelta.relativedelta(data_interval_end, dag.start_date).years
    print(f"Congratulations {MY_NAME}, you are {years} years old today!")
    return "Done!"

birthday_greeting = PythonOperator(
        task_id="send_wishes",
        dag=dag,
        python_callable=years_today,
        op_args=[MY_NAME]
    )

