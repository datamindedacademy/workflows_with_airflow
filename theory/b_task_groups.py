from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id="task_group_required",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A cluttered DAG",
    schedule_interval="*/5 14 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Brussels"),
    catchup=False,
    tags=["style", "timezone"],
)
with dag:
    start, middle, end = [
        DummyOperator(task_id=s) for s in ("start", "middle", "end")
    ]
    indices = range(1, 6)
    task_set_1, task_set_2 = [
        [DummyOperator(task_id=f"section-{section}-task-{n}") for n in indices]
        for section in (1, 2)
    ]

start >> task_set_1 >> middle >> task_set_2 >> end
