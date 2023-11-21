"""
# Exercise 4

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
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator

dag = DAG(
    dag_id="parallel_tasks",
    description="Many tasks in parallel",
    default_args={"owner": "Airflow"},
    schedule_interval="@daily",
    start_date=dt.datetime(2021, 1, 1),
    end_date=dt.datetime(2021, 1, 15),
)

dummies = [DummyOperator(task_id=f"task{n}", dag=dag) for n in range(7)]

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


