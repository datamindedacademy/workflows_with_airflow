from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Param
import time

"""
Exercise 9

We've built a DAG that can be manually triggered by anyone in the organisation to copy a table from an Oracle database
to our Enterprise Data Warehouse. They manually input the table they want to copy. 

Sometimes they want to copy more than 100 tables at the same time. So got the task to make the DAG dynamic and allow the DAG
to run for an arbitrary number of tables given as input.

"""

# Define the Python functions to be used in the tasks
def extract(**kwargs):
    # Extract data (simulated here with a print statement)
    source = kwargs['dag_run'].conf.get('source', 'default_source')
    print(f"Extracting data from {source}...")
    time.sleep(10)

def transform(**kwargs):
    # Transform data (simulated here with a print statement)
    data_format = kwargs['dag_run'].conf.get('data_format', 'CSV')
    print(f"Transforming data into {data_format} format...")
    time.sleep(10)

def load(**kwargs):
    # Load data (simulated here with a print statement)
    destination = kwargs['dag_run'].conf.get('destination', 'default_destination')
    print(f"Loading data into {destination}...")
    time.sleep(10)

# Define default arguments
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2025, 2, 1),
    'catchup': False,
}

with DAG(
    '9_manual_trigger_etl',
    default_args=default_args,
    description='A simple manually triggered ETL DAG',
    schedule_interval=None,  # None means manual trigger only
    params={
        'source': Param('oracle_database', type='string'),
        'data_format': Param('CSV', type='string'),
        'destination': Param('my_data_swamp', type='string')
    },
    tags=['example'],
) as dag:
    t1 = PythonOperator(
        task_id='extract_data',
        python_callable=extract,
        provide_context=True,
    )

    t2 = PythonOperator(
        task_id='transform_data',
        python_callable=transform,
        provide_context=True,
    )

    t3 = PythonOperator(
        task_id='load_data',
        python_callable=load,
        provide_context=True,
    )

    t1 >> t2 >> t3