import datetime as dt

from airflow import DAG
from airflow.models.baseoperator import cross_downstream
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

"""
Exercise 3

This DAG contains a lot of repetitive, duplicated and ultimately boring code.
Can you simplify this DAG and make it more concise?
"""

dag = DAG(
    dag_id="solution_3_parallel_tasks",
    description="Many tasks in parallel",
    default_args={"owner": "Airflow"},
    schedule="@daily",
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2025, 1, 15),
)


def create_task(idx):
    return BashOperator(
        task_id=f"task_{idx}", dag=dag, bash_command=f"echo 'task_{idx} done'"
    )


left = [create_task(x) for x in "abcd"]
right = [create_task(x) for x in "efgh"]

use_dummy = True
if use_dummy:
    left >> EmptyOperator(task_id="join", dag=dag) >> right
else:
    cross_downstream(from_tasks=left, to_tasks=right)
