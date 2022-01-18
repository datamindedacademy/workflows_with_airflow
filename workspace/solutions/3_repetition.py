import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.models.baseoperator import cross_downstream

"""
Exercise 3

This DAG contains a lot of repetitive, duplicated and ultimately boring code.
Can you simplify this DAG and make it more concise?
"""

dag = DAG(
    dag_id="parallel_tasks",
    description="Many tasks in parallel",
    schedule_interval="@daily",
    start_date=dt.datetime(2021, 1, 1),
    end_date=dt.datetime(2021, 1, 15),
)


def create_task(idx):
    return BashOperator(
        task_id=f"task_{idx}",
        dag=dag,
        bash_command=f"echo 'task_{idx} done'"
    )


left = [create_task(x) for x in ("a", "b", "c", "d")]
right = [create_task(x) for x in ("e", "f", "g", "h")]

use_dummy = True
if use_dummy:
    left >> DummyOperator(task_id="join", dag=dag) >> right
else:
    cross_downstream(from_tasks=left, to_tasks=right)

