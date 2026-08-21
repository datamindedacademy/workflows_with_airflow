import datetime as dt

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

"""
Exercise 1 solution: Top-level code cost

The DAG called load_data()/run_analysis()/store_results() directly
inside the `with dag:` block, so the scheduler re-ran the full download,
sleep, and pandas import every time it parsed the file. Wrapping the
pipeline in a single PythonOperator moves that work into task execution,
where it belongs.
"""

dag = DAG(
    dag_id="solution_1_investment_analysis",
    description="Analyze investment data",
    default_args={"owner": "Airflow"},
    schedule="@once",
    start_date=dt.datetime(2026, 1, 1),
    catchup=False,
)


def load_data():
    from io import BytesIO
    from zipfile import ZipFile

    import pandas as pd
    import requests

    investment_link = "https://eforexcel.com/wp/wp-content/uploads/2021/09/2000000-HRA-Records.zip"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"
    }
    response = requests.get(
        investment_link, stream=True, verify=False, headers=headers
    )
    with ZipFile(BytesIO(response.content)) as myzip:
        with myzip.open(myzip.namelist()[0]) as myfile:
            df = pd.read_csv(myfile)
    return df


def run_analysis(df):
    # < Insert hard data science problem here >
    import time

    time.sleep(10)
    return df.count()


def store_results(df):
    output_path = "/opt/airflow/dags/investment.csv"
    df.to_csv(output_path)
    print(f"CSV file written to: {output_path}")


def pipeline():
    df_investment = load_data()
    results = run_analysis(df_investment)
    store_results(results)


with dag:
    # No pipeline code is executed during DAG parsing
    PythonOperator(task_id="analyze_investment_data", python_callable=pipeline)
