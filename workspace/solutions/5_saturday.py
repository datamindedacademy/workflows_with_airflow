import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.weekday import BranchDayOfWeekOperator

"""
Exercise 5

This DAG needs to do an extra step on Saturday, but the current implementation has some downsides.
What's wrong? And how can you fix this?
"""

dag = DAG(
    dag_id="aggregate_on_saturday",
    description="On saturdays we run aggregations",
    default_args={"owner": "Airflow"},
    schedule_interval="@daily",
    start_date=dt.datetime(2021, 1, 1),
    end_date=dt.datetime(2021, 1, 15),
)


def create_task(name):
    return BashOperator(
        task_id=name,
        dag=dag,
        bash_command=f"echo '{name} done'"
    )


branch_for_saturday = BranchDayOfWeekOperator(
    task_id="is_it_saturday",
    dag=dag,
    follow_task_ids_if_true="aggregation",
    follow_task_ids_if_false="all_done",
    week_day="saturday",
)

ingestion_task = create_task("ingestion")
cleaning_task = create_task("cleaning")
aggregation_task = create_task("aggregation")
all_done = DummyOperator(task_id="all_done", dag=dag)

ingestion_task >> cleaning_task >> branch_for_saturday >> aggregation_task >> all_done
