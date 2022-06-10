FROM apache/airflow:2.2.3

USER root

RUN pip install --no-cache-dir apache-airflow-providers-amazon[cncf.kubernetes]==3.4.0

USER airflow
