import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise 4

Can you modify this DAG in such a way that downstream tasks (e, f, g, h)
will still start, even when the upstream task 'd' failed?

BONUS: Can you make it so that downstream tasks will only run if at least one upstream task has succeeded,
but not if all upstream tasks failed?
"""

dag = DAG(
    dag_id="4_failing_tasks",
    description="failing tasks",
    default_args={"owner": "Airflow"},
    schedule_interval="@daily",
    start_date=dt.datetime(2025, 1, 1),
    end_date=dt.datetime(2025, 1, 15),
)

task_a = BashOperator(
    task_id="task_a", dag=dag, bash_command="echo 'task_a done'"
)

task_b = BashOperator(
    task_id="task_b", dag=dag, bash_command="echo 'task_b done'"
)

task_c = BashOperator(
    task_id="task_c", dag=dag, bash_command="echo 'task_c done'"
)

task_d = BashOperator(
    task_id="task_d", dag=dag, bash_command="echo 'task_d failed'; exit -1"
)

task_e = BashOperator(
    task_id="task_e", dag=dag, bash_command="echo 'task_e done'"
)

task_f = BashOperator(
    task_id="task_f", dag=dag, bash_command="echo 'task_f done'"
)

task_g = BashOperator(
    task_id="task_g", dag=dag, bash_command="echo 'task_g done'"
)

task_h = BashOperator(
    task_id="task_h", dag=dag, bash_command="echo 'task_h done'"
)

task_a >> task_e
task_a >> task_f
task_a >> task_g
task_a >> task_h

task_b >> task_e
task_b >> task_f
task_b >> task_g
task_b >> task_h

task_c >> task_e
task_c >> task_f
task_c >> task_g
task_c >> task_h

task_d >> task_e
task_d >> task_f
task_d >> task_g
task_d >> task_h
