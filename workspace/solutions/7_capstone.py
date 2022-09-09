import pendulum
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor
from airflow.providers.http.operators.http import SimpleHttpOperator


"""Exercise: Capstone

In this exercise, you will need to look up the right Operators and Sensors and
combine them in the right way. Credentials will be provided to you by the
instructor.

The exercise can easily be built in two stages: 

1. Start by creating a sensor that is looking for the existence of a blob ('a
   file')  on AWS S3.  You'll only get a prefix, since often you'll not be fully
   informed about the filename to expect (e.g. "customerX.csv" or "customerX.xlsx"
   or "customerX-2022-01-16.csv"?)

2. After the file has been found, query a RESTful API, at httpbin.org/get, and
   provide it with the parameter of an API-key, which has been made available 
   to you as an Airflow global variable, through a secrets backend. So, you 
   should launch a query similar to this:
    httpbin.org/get?api-key=SOME_SECRET

Finally, discuss the pros and cons if the contents of the file were to be read
with another operator and passed to the API.
"""

BUCKET_NAME = "dmacademy-course-assets"
BUCKET_KEY = "airflow/pms_under_elizabeth*"

dag = DAG(
    dag_id="sensor-example",
    start_date=pendulum.datetime(2022, 1, 1, tz="Europe/Brussels"),
    schedule_interval="* * * * *",
    catchup=False,
)
# Have students build up to the keysensor using a connection
task = S3KeySensor(
    task_id="sensor",
    bucket_name=BUCKET_NAME,
    bucket_key=BUCKET_KEY,
    wildcard_match=True,
    aws_conn_id="aws_default",
    timeout=60,
    dag=dag,
)

# To access the variables from the secrets backend, Airflow needs to
# authenticate itself to AWS.  If this Airflow instance were to run inside the
# AWS cloud, this could be done by assigning an instance profile to the
# machine(s).  The Airflow instance you're using is in Gitpod though, so you
# need to pass it the means to authenticate. The instructor gives you IAM
# credentials.  Those credentials will need to be passed to the Airflow
# instance, which you could do in several ways. The easiest is to export them
# as environment variables in the gitpod environment, then run `docker compose
# down && docker compose build && docker compose up`
next_call = SimpleHttpOperator(
    task_id="get_op",
    method="GET",
    endpoint="get",
    data={
        "apikey": "{{ var.value.get('weather-api-key')  }}",
    },
    dag=dag,
)
task >> next_call
