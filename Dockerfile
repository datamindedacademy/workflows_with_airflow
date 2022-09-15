FROM apache/airflow:2.3.4

USER airflow

RUN pip install --no-cache-dir --user apache-airflow-providers-amazon[cncf.kubernetes]==5.1.0