import datetime as dt

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

"""
Exercise 10: XComs and Dynamic Task Mapping

This DAG uses the classical API (DAG() context manager + PythonOperator)
with .expand() for true dynamic task mapping. The number of regions is
determined at runtime, not hardcoded!

You'll practice: passing data between tasks via XCom, `.expand()` for
dynamic task mapping, and the classical API.

Key concepts demonstrated here:
1. DAG() context manager instead of @dag decorator
2. PythonOperator with .expand() for dynamic mapping
3. Return values automatically pushed to XCom, pulled via .output
4. op_args expansion for dynamic inputs

Your task: open `10_xcoms_taskflowapi.py` and rewrite this same pipeline
using the TaskFlow API (@dag / @task decorators) instead. This file is
your reference for what the pipeline should do.
"""


def get_regions():
    """Fetch regions to process. In reality, this might query a database."""
    regions = [
        {"name": "North", "sales": [1200, 1500, 1800, 1100]},
        {"name": "South", "sales": [2200, 2100, 1900]},
        {"name": "East", "sales": [800, 950, 1100, 1200, 900]},
        {"name": "West", "sales": [3000, 2800, 3200]},
    ]
    # Return value is automatically pushed to XCom
    return regions


def process_region(region):
    """Process a single region - called once per region via .expand()."""
    name = region["name"]
    total = sum(region["sales"])
    avg = total / len(region["sales"])

    print(f"Processing {name}: {len(region['sales'])} transactions")
    print(f"  Total: ${total:,}")
    print(f"  Average: ${avg:,.2f}")

    return {
        "name": name,
        "total": total,
        "count": len(region["sales"]),
        "average": avg,
    }


def generate_summary(results):
    """Aggregate results from all processed regions."""
    print("\n" + "=" * 40)
    print("       REGIONAL SALES SUMMARY")
    print("=" * 40)

    grand_total = 0
    for result in results:
        print(f"{result['name']:10} | ${result['total']:>8,} | {result['count']} sales")
        grand_total += result["total"]

    print("-" * 40)
    print(f"{'TOTAL':10} | ${grand_total:>8,}")
    print("=" * 40)


with DAG(
    dag_id="10_classical_api",
    description="Classical API with dynamic task mapping",
    schedule="@daily",
    start_date=dt.datetime(2025, 1, 1),
    catchup=False,
    tags=["exercise", "classical", "xcom", "dynamic"],
) as dag:

    get_regions_task = PythonOperator(
        task_id="get_regions",
        python_callable=get_regions,
    )

    # Use .expand() with op_args to dynamically create tasks
    # The XCom output from get_regions_task is automatically expanded
    process_region_task = PythonOperator.partial(
        task_id="process_region",
        python_callable=process_region,
    ).expand(op_args=get_regions_task.output.map(lambda region: [region]))

    # Collect all mapped task outputs using .output
    summary_task = PythonOperator(
        task_id="generate_summary",
        python_callable=generate_summary,
        op_args=[process_region_task.output],
    )

    # Dependencies are implicit via .output references, but we can be explicit:
    get_regions_task >> process_region_task >> summary_task