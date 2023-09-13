import datetime as dt
import pendulum
from airflow import DAG 
from airflow.providers.postgres.operators.postgres import PostgresOperator

table = "SALES"

with DAG(
    dag_id="need-for-context-example", 
    schedule_interval="@daily",
    start_date=pendulum. datetime (2022, 1, 1, tz= "Europe/Brussels"), 
) as dag:
    revenue = PostgresOperator (
        task_id="query_revenue", 
        postgres_conn_id="postgres_default",
        sql=f"""
        SELECT SUM(amount)
        FROM {table}
        WHERE dt BETWEEN '{dt.date.today( ) - dt.timedelta(days=1)}' AND '{dt.date.today ()}'
        """
    )