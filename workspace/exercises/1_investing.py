import datetime as dt

import pandas as pd
from airflow import DAG

"""
Exercise 1

This DAG seems to take a long time to load.
(Have a look at the scheduler logs if you're unsure about this)

Can you figure out why, and how to fix it?
"""

dag = DAG(
    dag_id="investment_analysis",
    description="Analyze investment data",
    default_args={"owner": "Airflow"},
    schedule_interval="@once",
    start_date=dt.datetime(2021, 1, 1),
)


def load_data():
    from io import BytesIO
    from zipfile import ZipFile

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
    df.to_csv("./investment.csv")


with dag:
    df_investment = load_data()
    results = run_analysis(df_investment)
    store_results(results)
