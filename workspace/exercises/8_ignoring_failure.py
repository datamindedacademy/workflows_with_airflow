"""
# Exercise 8

Some operators, like the BranchPythonOperator,
allow you to skip tasks. Often, you will want to
do something after this branch, regardless of
whether or not the step has been skipped. To do
so, the task that depends on the skipped task
and the non-skipped task will need to wait for
one of them to be successfully finished.
"""
import datetime as dt
import random

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import BranchPythonOperator, PythonOperator

default_args = {
    "owner": "Airflow",
    "retries": 3,
    "retry_delay": dt.timedelta(minutes=1),
}

dag = DAG(
    dag_id="8_ignoring_failure",
    description="Many tasks in parallel",
    default_args=default_args,
    schedule="@daily",
    start_date=dt.datetime(2026, 1, 1),
    end_date=dt.datetime(2026, 3, 1),
    max_active_runs=3,
    catchup=True
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

# Dummies[5] recombines the 2 branches. However, we don't want it skipped.
[dummies[3], dummies[4]] >> dummies[5] >> dummies[6]


