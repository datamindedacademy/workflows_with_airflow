from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.smooth import SmoothOperator


"""
Exercise 0

Test your first Airflow Deployment!

Copy this file to /workflows-with-airflow/workspace/mount/dags and wait or refresh your Airflow UI!

"""

# Default DAG arguments
default_args = {
    'owner': 'dataminded',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id='0_hello_airflow',
    dag_display_name='🤖 Hello Airflow 🚀',
    default_args=default_args,
    description='A DAG demonstrating the use of SmoothOperator',
    schedule=timedelta(days=1),  # Adjust as needed
    catchup=False,
) as dag:

    start = EmptyOperator(task_id='start')

    smooth_task = SmoothOperator(
        task_id='run_smooth_operator',
    )

    end = EmptyOperator(task_id='end')

    # Task dependencies
    start >> smooth_task >> end
