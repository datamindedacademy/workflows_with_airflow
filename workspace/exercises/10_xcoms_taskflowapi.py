import datetime as dt

from airflow.sdk import dag, task

"""
Exercise 10: TaskFlow API, XComs, and Dynamic Task Mapping

Look at `10_xcoms_classicapi.py` in this same folder: it builds a DAG
with the classical API (DAG() + PythonOperator) that
1. fetches a list of regions,
2. processes each region in a dynamically mapped task, and
3. aggregates all the results into a summary.

Your task: rewrite that same pipeline below using the TaskFlow API.

You'll practice: passing data between tasks via XCom, `.expand()` for
dynamic task mapping, and the TaskFlow API compared to the classical
API.

Concepts you'll need:
1. @dag - turns a function into a DAG factory (replaces DAG())
2. @task - turns a function into a task (replaces PythonOperator)
3. Automatic XCom - just return a value, no xcom_push/xcom_pull needed
4. .expand() - call a @task function with a list argument to dynamically
   create one task instance per item in the list

Fill in the TODOs below. When you're done, the DAG should behave exactly
like `10_xcoms_classicapi.py`.
"""


@dag(
    dag_id="10_taskflow_dynamic",
    description="TaskFlow API and Dynamic Task Mapping",
    schedule="@daily",
    start_date=dt.datetime(2025, 1, 1),
    catchup=False,
    tags=["exercise", "taskflow", "dynamic"],
)
def sales_pipeline():

    # TODO: turn this into a @task that fetches the regions to process.
    # Reuse the same region data as in the classical API version.
    def get_regions() -> list[dict]:
        raise NotImplementedError("TODO: return the list of regions")

    # TODO: turn this into a @task that processes a single region.
    # It should compute the total and average sales, print a summary,
    # and return a dict with the results (see the classical version).
    def process_region(region: dict) -> dict:
        raise NotImplementedError("TODO: process a single region")

    # TODO: turn this into a @task that aggregates all processed regions
    # into a printed summary (see the classical version).
    def generate_summary(results: list[dict]) -> None:
        raise NotImplementedError("TODO: aggregate and print the summary")

    # TODO: wire up the DAG:
    # 1. call get_regions() to fetch the list
    # 2. use .expand() on process_region to create one task per region
    # 3. pass all the results into generate_summary()


# Instantiate the DAG
sales_pipeline()
