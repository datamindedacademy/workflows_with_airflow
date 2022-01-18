import datetime as dt

from airflow import DAG
from airflow.models.baseoperator import cross_downstream
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.trigger_rule import TriggerRule

"""
Exercise 4

Can you modify this DAG in such a way that downstream tasks (e, f, g, h)
will still start, even when the upstream task 'd' failed?

BONUS: Can you make it so that downstream tasks will only run if at least one upstream task has succeeded,
but not if all upstream tasks failed?
"""

dag = DAG(
    dag_id="parallel_tasks",
    description="Many tasks in parallel",
    default_args={"owner": "Airflow"},
    schedule_interval="@daily",
    start_date=dt.datetime(2021, 1, 1),
    end_date=dt.datetime(2021, 1, 15),
)


def create_task(idx, trigger_rule=TriggerRule.ALL_SUCCESS):
    return BashOperator(
        task_id=f"task_{idx}",
        dag=dag,
        bash_command=f"echo 'task_{idx} done'",
        trigger_rule=trigger_rule
    )


def failing_task(idx):
    return BashOperator(
        task_id=f"task_{idx}",
        dag=dag,
        bash_command=f"echo 'task_{idx} failed'; exit -1"
    )


left = [create_task(x) for x in ("a", "b", "c")]
left.append(failing_task("d"))

use_dummy = True
if use_dummy:
    right = [create_task(x) for x in ("e", "f", "g", "h")]
    left >> DummyOperator(task_id="join", dag=dag, trigger_rule=TriggerRule.ALL_DONE) >> right
else:
    right = [create_task(x, trigger_rule=TriggerRule.ALL_DONE) for x in ("e", "f", "g", "h")]
    cross_downstream(from_tasks=left, to_tasks=right)
