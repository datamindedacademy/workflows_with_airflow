import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule

"""
Exercise 4

Can you modify this DAG in such a way that downstream tasks (e, f, g, h)
will still start, even when the upstream task 'd' failed?

BONUS: Can you make it so that downstream tasks will only run if at least one upstream task has succeeded,
but not if all upstream tasks failed?
"""

dag = DAG(
    dag_id="solution_4_failing_tasks_bonus",
    description="failing tasks",
    default_args={"owner": "Airflow"},
    schedule="@daily",
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2025, 1, 15),
)


def create_task(idx, trigger_rule=TriggerRule.ALL_SUCCESS):
    return BashOperator(
        task_id=f"task_{idx}",
        bash_command=f"echo 'task_{idx} done'",
        trigger_rule=trigger_rule,
    )


def failing_task(idx):
    return BashOperator(
        task_id=f"task_{idx}",
        bash_command=f"echo 'task_{idx} failed'; exit -1",
    )


def at_least_one_success(group_id):
    with TaskGroup(group_id=group_id) as tg:
        all_done = EmptyOperator(
            task_id="all_done", trigger_rule=TriggerRule.ALL_DONE
        )
        one_success = EmptyOperator(
            task_id="one_success", trigger_rule=TriggerRule.ONE_SUCCESS
        )
        both_done = EmptyOperator(
            task_id="both_done", trigger_rule=TriggerRule.ALL_SUCCESS
        )
        [all_done, one_success] >> both_done
    return tg


with dag:
    left = [create_task(x) for x in "abc"]
    left.append(failing_task("d"))
    right = [create_task(x) for x in "efgh"]

    left >> at_least_one_success("at_least_one_success") >> right
