# Orchestrating work with Apache Airflow

## Repository description

This code repository contains exercises that go with the [Data Minded
Academy](https://www.dataminded.academy/) workshop on "Orchestrating work with
[Apache Airflow](https://airflow.apache.org/)".

## Workshop topic introduction

Data transformation pipelines rarely run by themselves. There are typically
boundary conditions at play, like "we first need to have the results from this
API, before we can upload the data to the database". Such workflows can be
coded as part of your pipeline, but you risk creating an intangible mess that
won't allow you to continue from halfway if an error occurred only halfway
through. Learn about Apache Airflow, one of the most popular ways to
orchestrate work, while allowing for a pleasant dashboard to follow up the
daily progress of tasks that had to be completed.

## Getting started

You can simply click the button below to start the exercise environment within
GitHub Codespaces.
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/datamindedacademy/workflows_with_airflow)


### Airflow UI

The GitHub Codespaces environment will set up an Airflow instance for you to use during the
exercise session. The Airflow UI will load in a new browser window once the
startup is complete. You can log in to the UI using "airflow" both as username
and password.

### Mounted folders

The GitHub Codespaces environment you receive will contain three folders:

1. exercises
2. solutions
3. mount

The folder named _mount_ will contain three sub-folders: dags, logs and plugins.
These three folders will reflect the internal state of Airflow for these points,
and can be used to upload DAGs or plugins into Airflow, or download log files.

### Debugging

When you need access to the containerized Airflow environment, use

```shell
docker compose run airflow-cli bash
```
