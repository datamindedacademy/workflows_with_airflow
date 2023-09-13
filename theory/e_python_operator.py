import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

def hello_world(ds=None):
    print("That's right, I'm a Python function!")
    return "This goes to the logs..."

with DAG(
    dag_id="python-operator-example",
    schedule_interval="@daily",
    start_date=pendulum.datetime(2023, 1, 1, tz="Europe/Brussels"),
) as dag:
    task = PythonOperator(
        task_id="hello_world",
        python_callable=hello_world
    )
