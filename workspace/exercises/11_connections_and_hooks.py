"""
Exercise 11: Connections & Hooks

Every day we write yesterday's total sales to Postgres, then read the
running total back for a report. The task below does this by calling
`psycopg2` directly, with the database password hardcoded right there
in the DAG file. The sales amount itself is a DAG `Param`, so it can be
overridden per manual run instead of editing the file.

You'll practice: what an Airflow Connection is, and using a Hook
(`PostgresHook`) to look one up instead of hardcoding credentials in
code.

A colleague flagged this DAG in a security review: the password is
sitting in plaintext in git, and anyone who can see the DAG's "Code"
tab in the UI can read it too. Can you fix it?

Hint: register a Connection once, either via the UI ("Admin >
Connections") or the CLI:
    docker compose run airflow-cli airflow connections add \
        warehouse_postgres \
        --conn-type postgres \
        --conn-host postgres \
        --conn-schema airflow \
        --conn-login airflow \
        --conn-password airflow
Then rewrite the task to fetch that Connection through a
`PostgresHook(postgres_conn_id="warehouse_postgres")` instead of
connecting directly.
"""
import datetime as dt

import psycopg2
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import Param

dag = DAG(
    dag_id="11_connections_and_hooks",
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
    # TODO: this hardcoded password is the problem -- use a Connection
    # and a Hook instead.
    conn = psycopg2.connect(
        host="postgres",
        dbname="airflow",
        user="airflow",
        password="airflow",
    )
    with conn, conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS sales (day DATE, amount INTEGER)"
        )
        cur.execute(
            "INSERT INTO sales (day, amount) VALUES (CURRENT_DATE, %s)",
            (params["amount"],),
        )
        cur.execute("SELECT SUM(amount) FROM sales")
        total = cur.fetchone()[0]
    print(f"Total sales so far: {total}")


write_sales = PythonOperator(
    task_id="write_and_read_sales",
    dag=dag,
    python_callable=write_and_read_sales,
)
