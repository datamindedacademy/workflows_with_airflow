from datetime import timedelta

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


with DAG(
    dag_id="xcoms",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="An example of how to use XComs",
    schedule="*/5 * * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Brussels"),
    catchup=False,
    tags=["XCom", "timezone"],
) as dag:

    def say_hello():
        return "hello"

    auto_pusher = PythonOperator(
        task_id="hello",
        python_callable=say_hello,
        do_xcom_push=True,
    )

    def shout_hello(**kwargs):
        task_instance = kwargs["task_instance"]
        task_instance.xcom_push(key="manual push", value="HELLO")

    manual_pusher = PythonOperator(
        task_id="HELLO",
        python_callable=shout_hello,
        do_xcom_push=False,
        provide_context=True,
    )

    def pulling_function(**kwargs):
        task_instance = kwargs["ti"]
        hello = task_instance.xcom_pull(task_ids="hello")
        shout = task_instance.xcom_pull(task_ids="HELLO", key="manual push")
        if (hello != shout) and (hello.upper() == shout):
            print("Pulled two XCom values")
        else:
            raise ValueError()
        return (1, 3)  # Parenthesis added for clarity

    puller = PythonOperator(
        task_id="pull",
        python_callable=pulling_function,
        provide_context=True,
    )

    bash = BashOperator(
        task_id="last_pull",
        bash_command=f"echo 'got the set {puller.output}'",
        do_xcom_push=False,
    )
[auto_pusher, manual_pusher] >> puller >> bash
