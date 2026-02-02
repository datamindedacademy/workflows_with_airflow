from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
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
    schedule="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Brussels"),
    end_date=pendulum.datetime(2021, 1, 10, tz="Europe/Brussels"),
    catchup=True,
    tags=["reporting"],
) as dag:
    # Note the bash command. What does that imply for the worker? If you don't
    # immediately see it, consider what would happen if you'd call the less
    # prevalent tool 'jq'.
    make_report = BashOperator(
        task_id="create_report",
        # The trailing space is required to prevent Jinja templating
        # See https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html#jinja-template-not-found
        bash_command='echo "home is $HOME" ',
    )
    empty_task = EmptyOperator(
        task_id="send_most_recent_report",
        trigger_rule="all_done"
    )

    branch = BranchDayOfWeekOperator(
        task_id="make_choice",
        follow_task_ids_if_true=make_report.task_id,
        follow_task_ids_if_false=empty_task.task_id,
        week_day={"Monday", "Wednesday"},
        use_task_execution_day=True,
    )
    # Make report if branch executes on Monday or on Wednesday.
    branch >> [make_report, empty_task]
    make_report >> [EmptyOperator(
        task_id="foo",
        trigger_rule="all_done",
        depends_on_past=True,
    ), empty_task]

    empty_task >> [EmptyOperator(task_id="signal_done")]
# We can simplify this a lot: rather than scheduling it daily, we can adapt the
# schedule to use CRON syntax. Though keep in mind that it will then
# run with different data intervals, so if you depend on those parameters (e.g.
# in templates) then you cannot simply change to this alternative.

