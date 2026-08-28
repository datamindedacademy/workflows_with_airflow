import datetime as dt

from airflow import DAG
from airflow.models.baseoperator import cross_downstream
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule

"""
Exercise 6 solution: Trigger rules

An EmptyOperator "join" task with `trigger_rule=TriggerRule.ALL_DONE`
sits between the upstream tasks and e-h, so a failure in `task_d` no
longer blocks the whole right-hand side -- `ALL_DONE` fires regardless
of whether upstream tasks succeeded or failed.
"""

dag = DAG(
    dag_id="solution_6_failing_tasks",
    description="failing tasks",
    default_args={"owner": "Airflow"},
    schedule="@daily",
    start_date=dt.datetime(2026, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
)


def create_task(idx, trigger_rule=TriggerRule.ALL_SUCCESS):
    return BashOperator(
        task_id=f"task_{idx}",
        dag=dag,
        bash_command=f"echo 'task_{idx} done'",
        trigger_rule=trigger_rule,
    )


def failing_task(idx):
    return BashOperator(
        task_id=f"task_{idx}",
        dag=dag,
        bash_command=f"echo 'task_{idx} failed'; exit -1",
    )


left = [create_task(x) for x in "abc"]
left.append(failing_task("d"))

use_dummy = True
if use_dummy:
    dummy = EmptyOperator(
        task_id="join",
        dag=dag,
        trigger_rule=TriggerRule.ALL_DONE,
    )
    right = [create_task(x) for x in "efgh"]
    left >> dummy >> right
else:
    right = [create_task(x, trigger_rule=TriggerRule.ALL_DONE) for x in "efgh"]
    cross_downstream(from_tasks=left, to_tasks=right)
