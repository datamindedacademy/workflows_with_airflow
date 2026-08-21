import datetime as dt

from airflow import DAG
from airflow.models.baseoperator import cross_downstream
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

"""
Exercise 5 solution: DRY DAGs

Replaces the 8 hand-written BashOperators and 16 explicit `>>` edges
with a `create_task()` helper plus either an EmptyOperator join or
`cross_downstream()`, so adding or removing a task no longer means
editing every downstream/upstream pair by hand.
"""

dag = DAG(
    dag_id="solution_5_parallel_tasks",
    description="Many tasks in parallel",
    default_args={"owner": "Airflow"},
    schedule="@daily",
    start_date=dt.datetime(2026, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
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
    