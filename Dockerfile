FROM apache/airflow:2.3.4-python3.10

USER root

RUN pip install --no-cache-dir apache-airflow-providers-amazon[cncf.kubernetes]==5.1.0

USER airflow
