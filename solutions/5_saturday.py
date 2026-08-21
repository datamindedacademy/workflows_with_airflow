import datetime as dt

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import BranchPythonOperator

"""
Solution 5

Three bugs were hiding in the branch:

1. The callable returned "aggregation_task" / "skip_aggregation_task",
   which are the *Python variable* names, not the task_ids. A branch
   callable must return task_ids (strings), so Airflow failed the branch
   task on every run with:
       'branch_task_ids' must contain only valid task_ids.
   Symptom: 'is_it_saturday' red on every single run.

2. 'publish_results' kept the default trigger rule, all_success. A branch
   *skips* the arm it does not take, and a skipped upstream never
   satisfies all_success, so 'publish_results' was skipped on every run.
   Symptom: the whole tail of the DAG grey, forever.
   Fix: a trigger rule that tolerates skips but not failures,
   none_failed_min_one_success.

3. The callable asked dt.date.today() -- the wall clock of whatever
   machine happens to be running the task, at whatever moment it runs.
   Every one of the 15 backfilled runs therefore took the same branch,
   because they were all executed on the same real-world day. A task must
   decide based on the date of the *run* it belongs to, not on today.
   Symptom: 0 or 15 aggregations instead of exactly 2.
   This is the answer to the BONUS: bug 3 is invisible if you only ever
   trigger the DAG by hand, because then "today" and the run's date
   happen to agree.

Note that data_interval_start is used rather than logical_date: since
Airflow 3, logical_date is None for manually triggered runs, whereas
data_interval_start is always populated.

Two more branch pitfalls worth knowing, not present in this exercise:

* A branch may only steer between its own *direct* downstream tasks.
  Returning the task_id of something further down the graph works by
  accident (via skip propagation) but the arrow you are reasoning about
  does not exist, and the graph view will not show it.
* For this specific weekday case there is a purpose-built operator,
  airflow.providers.standard.operators.weekday.BranchDayOfWeekOperator,
  with a use_task_logical_date flag that exists precisely because of
  bug 3. Now that you have written the branch yourself, you know what
  that flag is protecting you from.
"""

dag = DAG(
    dag_id="solution_5_aggregate_on_saturday",
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


def pick_branch(data_interval_start):
    """Decide whether this run needs the aggregation step."""
    if data_interval_start.isoweekday() == 6:
        return "aggregation"
    return "skip_aggregation"


ingestion_task = create_task("ingestion")
cleaning_task = create_task("cleaning")
aggregation_task = create_task("aggregation")
skip_aggregation_task = EmptyOperator(task_id="skip_aggregation", dag=dag)
publish_results = EmptyOperator(
    task_id="publish_results",
    dag=dag,
    trigger_rule="none_failed_min_one_success",
)

is_it_saturday = BranchPythonOperator(
    task_id="is_it_saturday",
    dag=dag,
    python_callable=pick_branch,
)

ingestion_task >> cleaning_task >> is_it_saturday
is_it_saturday >> [aggregation_task, skip_aggregation_task] >> publish_results
