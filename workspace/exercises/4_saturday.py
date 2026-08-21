import datetime as dt

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import BranchPythonOperator

"""
Exercise 4: Catchup & backfills

Every day we ingest and clean data. On Saturdays we also run an
aggregation. A colleague already built the branch for this, but the DAG
is not working correctly. Do you see what's wrong?

You'll practice: `catchup=True`, backfill windows, and telling the DAG's
logical/execution date apart from wall-clock `datetime.now()` -- the
same distinction exercise 3's Jinja template relied on, except this time
nothing reminds you to use it.

There are three separate problems. Fix them one at a time and re-run:
each fix will reveal the next.

Hint: unpause the DAG and let it backfill its whole window: 15 daily
runs, from 2026-01-01 up to and including 2026-01-15. That window
contains exactly two Saturdays (the 3rd and the 10th), so you already
know what a healthy run history has to look like: 2 runs with an
aggregation, 13 without, and 15 runs in which 'publish_results'
succeeded. Clear the tasks you fixed to make a run happen again, and
read the task colours in the grid view carefully -- 'skipped' and
'failed' mean very different things.

BONUS: which of the three problems would you never have noticed if you
had only ever triggered this DAG manually?
"""

dag = DAG(
    dag_id="4_aggregate_on_saturday",
    description="On saturdays we run aggregations",
    default_args={"owner": "Airflow"},
    schedule="@daily",
    start_date=dt.datetime(2026, 1, 1),
    end_date=dt.datetime(2026, 1, 15),
    catchup=True,
    max_active_runs=3,
)


def create_task(name):
    return BashOperator(
        task_id=name,
        dag=dag,
        bash_command=f"echo '{name} done'",
    )


def pick_branch():
    """Decide whether this run needs the aggregation step."""
    if dt.date.today().isoweekday() == 6:
        return "aggregation_task"
    return "skip_aggregation_task"


ingestion_task = create_task("ingestion")
cleaning_task = create_task("cleaning")
aggregation_task = create_task("aggregation")
skip_aggregation_task = EmptyOperator(task_id="skip_aggregation", dag=dag)
publish_results = EmptyOperator(task_id="publish_results", dag=dag)

is_it_saturday = BranchPythonOperator(
    task_id="is_it_saturday",
    dag=dag,
    python_callable=pick_branch,
)

ingestion_task >> cleaning_task >> is_it_saturday
is_it_saturday >> [aggregation_task, skip_aggregation_task] >> publish_results
