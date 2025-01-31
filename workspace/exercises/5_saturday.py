import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

"""
Exercise 5

This DAG needs to do an extra step on Saturday, 
but the current implementation has some downsides.

What's wrong? And how can you fix this?
"""

dag = DAG(
    dag_id="5_aggregate_on_saturday",
    description="On saturdays we run aggregations",
    default_args={"owner": "Airflow"},
    schedule_interval="@daily",
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2025, 1, 15),
)


def today_is_saturday():
    today = dt.date.today()
    return today.isoweekday() == 6


def create_task(name):
    return BashOperator(
        task_id=name,
        dag=dag,
        bash_command=f"echo '{name} done'",
    )


ingestion_task = create_task("ingestion")
cleaning_task = create_task("cleaning")
all_done = EmptyOperator(task_id="all_done", dag=dag)

if today_is_saturday():
    aggregation_task = create_task("aggregation")
    ingestion_task >> cleaning_task >> aggregation_task >> all_done
else:
    ingestion_task >> cleaning_task >> all_done
