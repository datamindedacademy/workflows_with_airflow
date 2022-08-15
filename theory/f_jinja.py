import pendulum
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id="jinja-example",
    schedule_interval="@daily",
    start_date=pendulum.datetime(2022, 1, 1, tz="Europe/Brussels"),
) as dag:
    revenue = PostgresOperator(
        task_id="query_revenue",
        postgres_conn_id="postgres_default",
        sql="sql/daily_revenue.sql",
        params={"table": "SALES"},
    )
