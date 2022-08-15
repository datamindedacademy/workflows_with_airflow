import pendulum
from airflow import DAG

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
BUCKET_KEY = "..."

dag = DAG(
    dag_id="sensor-example",
    start_date=pendulum.datetime(2022, 1, 1, tz="Europe/Brussels"),
    schedule_interval="...",
    catchup=False,
)
