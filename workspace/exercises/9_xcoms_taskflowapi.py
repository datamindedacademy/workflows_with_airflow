import datetime as dt

from airflow.sdk import dag, task

"""
Solution 9: TaskFlow API, XComs, and Dynamic Task Mapping

Key concepts demonstrated:
1. @dag decorator - Creates a DAG factory function
2. @task decorator - Converts Python functions to Airflow tasks
3. Automatic XCom - Return values are automatically passed between tasks
4. .expand() - Dynamically creates one task instance per input item
"""


@dag(
    dag_id="solution_9_taskflow_dynamic",
    description="TaskFlow API and Dynamic Task Mapping",
    schedule="@daily",
    start_date=dt.datetime(2025, 1, 1),
    catchup=False,
    tags=["solution", "taskflow", "dynamic"],
)
def sales_pipeline():

    @task
    def get_regions() -> list[dict]:
        """Fetch regions to process. In reality, this might query a database."""
        return [
            {"name": "North", "sales": [1200, 1500, 1800, 1100]},
            {"name": "South", "sales": [2200, 2100, 1900]},
            {"name": "East", "sales": [800, 950, 1100, 1200, 900]},
            {"name": "West", "sales": [3000, 2800, 3200]},
        ]

    @task
    def process_region(region: dict) -> dict:
        """Process a single region - this task will run once per region."""
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

    @task
    def generate_summary(results: list[dict]) -> None:
        """Aggregate results from all dynamically mapped tasks."""
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

    # Wire up the DAG using TaskFlow patterns:
    # 1. get_regions() returns a list
    # 2. .expand() creates one process_region task per list item
    # 3. generate_summary receives a list of all results (automatic aggregation)
    
    regions = get_regions()
    processed = process_region.expand(region=regions)
    generate_summary(processed)


# Instantiate the DAG
sales_pipeline()