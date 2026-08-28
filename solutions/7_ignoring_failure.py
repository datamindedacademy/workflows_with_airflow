"""
Exercise 7 solution: Trigger rules with retries & branching

`dummies[5]` (the branch rejoin point) gets
`trigger_rule=TriggerRule.ONE_SUCCESS` set explicitly, so it fires once
either branch succeeds instead of being skipped whenever the branch it
doesn't inherit from was skipped -- retries on `task2` don't change
this, since a trigger rule only cares about the final state of each
upstream task.
"""
import datetime as dt
import random

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import BranchPythonOperator, PythonOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    "owner": "Airflow",
    "retries": 3,
    "retry_delay": dt.timedelta(minutes=1),
}

dag = DAG(
    dag_id="solution_7_ignoring_failure",
    description="Many tasks in parallel",
    default_args=default_args,
    schedule="@daily",
    catchup=True,
    start_date=dt.datetime(2026, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
    max_active_runs=3,
)


def fail_on_odd_try(ti):
    print("ti:", ti)
    try_number = ti.try_number
    if try_number % 2 == 1:
        raise Exception(f"Failing on odd try number: {try_number}")


dummies = [
    PythonOperator(task_id="task2", dag=dag, python_callable=fail_on_odd_try) if n == 2
    else EmptyOperator(task_id=f"task{n}", dag=dag)
    for n in range(7)
]

def split():
    index = 1 + int(random.random() > .5)
    return dummies[index].task_id

branch = BranchPythonOperator(
    task_id="branch_at_random",
    dag=dag,
    python_callable=split,
)

dummies[0] >> branch >> [dummies[1], dummies[2]]

dummies[1] >> dummies[3]
dummies[2] >> dummies[4]

dummies[5].trigger_rule = TriggerRule.ONE_SUCCESS

# Dummies[5] recombines the 2 branches. However, we don't want it skipped.
[dummies[3], dummies[4]] >> dummies[5] >> dummies[6]


