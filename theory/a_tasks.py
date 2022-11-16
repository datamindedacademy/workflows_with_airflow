from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.weekday import BranchDayOfWeekOperator

with DAG(
    dag_id="tutorial",
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
    description="Generate semi-weekly sales report",
    schedule_interval="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Brussels"),
    catchup=False,
    tags=["reporting"],
) as dag:

    # Note the bash command. What does that imply for the worker?
    make_report = BashOperator(
        task_id="branch_true",
        # The trailing space is required to prevent Jinja templating
        # See https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html#jinja-template-not-found
        bash_command="/usr/bin/reportgen.sh ",
    )
    empty_task = DummyOperator(task_id="branch_false")

    branch = BranchDayOfWeekOperator(
        task_id="make_choice",
        follow_task_ids_if_true=make_report.task_id,
        follow_task_ids_if_false=empty_task.task_id,
        week_day={"Monday", "Wednesday"},
        use_task_execution_day=True,
    )
    # Make report if branch executes on Monday or on Wednesday.
    branch >> [make_report, empty_task]
    make_report >> DummyOperator(
        task_id="foo",
        trigger_rule="all_done",
        depends_on_past=True,
    )

# We can simplify this a lot: rather than scheduling it daily, we can adapt the
# schedule_interval to use CRON syntax. Though keep in mind that it will then
# run with different data intervals, so if you depend on those parameters (e.g.
# in templates) then you cannot simply change to this alternative.
