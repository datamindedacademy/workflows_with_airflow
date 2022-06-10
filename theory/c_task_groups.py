from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import timedelta
import pendulum
from airflow.utils.task_group import TaskGroup

dag = DAG(
    dag_id="task_groups",
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
indices = range(1, 6)
with dag:
    start, middle, end = (
        DummyOperator(task_id=s) for s in ("start", "middle", "end")
    )
    with TaskGroup(group_id="group1") as group1:
        ts1 = [DummyOperator(task_id=f"section-1-task-{n}") for n in indices]
    with TaskGroup(group_id="group2") as group2:
        ts2 = [DummyOperator(task_id=f"section-2-task-{n}") for n in indices]

start >> group1 >> middle >> group2 >> end
