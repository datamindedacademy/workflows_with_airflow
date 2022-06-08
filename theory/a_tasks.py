from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.weekday import BranchDayOfWeekOperator
from airflow.operators.dummy import DummyOperator
from datetime import timedelta, datetime


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
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["reporting"],
) as dag:

    branch = BranchDayOfWeekOperator(
        task_id="make_choice",
        follow_task_ids_if_true="branch_true",
        follow_task_ids_if_false="branch_false",
        week_day={"Monday", "Wednesday"},
        use_task_execution_day=True,
    )

    # Note the command. What does that imply for the worker?
    make_report = BashOperator(
        task_id="branch_true",
        # The trailing space is required to prevent Jinja templating
        bash_command="/usr/bin/reportgen.sh "
    )
    empty_task = DummyOperator(task_id="branch_false")

    # Make report if branch executes on Monday or on Wednesday.
    branch >> [make_report, empty_task]

# We can simplify this a lot: rather than scheduling it daily, we can adapt the
# schedule_interval to use a CRON syntax.
