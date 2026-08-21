"""
Exercise 11 solution: Connections & Hooks

Swaps the hardcoded `psycopg2.connect(..., password="airflow")` call for
`PostgresHook(postgres_conn_id="warehouse_postgres")`. The password now
lives in a Connection, created once via `airflow connections add` or
the "Admin > Connections" page, instead of in the DAG file: it's no
longer visible in git or in the "Code" tab of the UI, and the Hook
handles opening/closing the connection for us via `run()`/`get_first()`.
The sales amount is passed as a parameterized query argument rather
than interpolated into the SQL string, since it now comes from a DAG
`Param` a user could override on a manual run.

To create the Connection, run once:
    docker compose run airflow-cli airflow connections add \
        warehouse_postgres \
        --conn-type postgres \
        --conn-host postgres \
        --conn-schema airflow \
        --conn-login airflow \
        --conn-password airflow
"""
import datetime as dt

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import Param

dag = DAG(
    dag_id="solution_11_connections_and_hooks",
    description="Reads and writes daily sales figures in Postgres",
    default_args={"owner": "Airflow"},
    schedule="@daily",
    start_date=dt.datetime(2026, 1, 1),
    catchup=False,
    params={
        "amount": Param(
            4200, type="integer", description="Sales amount to record"
        ),
    },
)


def write_and_read_sales(params):
    hook = PostgresHook(postgres_conn_id="warehouse_postgres")
    hook.run("CREATE TABLE IF NOT EXISTS sales (day DATE, amount INTEGER)")
    hook.run(
        "INSERT INTO sales (day, amount) VALUES (CURRENT_DATE, %s)",
        parameters=(params["amount"],),
    )
    total = hook.get_first("SELECT SUM(amount) FROM sales")[0]
    print(f"Total sales so far: {total}")


write_sales = PythonOperator(
    task_id="write_and_read_sales",
    dag=dag,
    python_callable=write_and_read_sales,
)
