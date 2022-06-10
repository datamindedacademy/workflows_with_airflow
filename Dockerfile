FROM apache/airflow:2.2.3

USER root

RUN pip install --no-cache-dir apache-airflow-providers-amazon[cncf.kubernetes]==2.6.0

USER airflow
