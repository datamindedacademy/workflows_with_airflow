# Orchestrating work with Apache Airflow

[![Dataminded Academy](https://raw.githubusercontent.com/datamindedacademy/branding/main/assets/badge.svg)](https://github.com/datamindedacademy)

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

## Exercises

The exercises build on each other in the order below: scheduling fundamentals
first (2-4), then DAG-authoring patterns (5-7), then cross-DAG dependencies
(8-9), ending with XComs/TaskFlow (10) and Connections & Hooks (11) as the
most advanced, self-contained topics.

| # | Exercise | Topic | Concepts |
|---|---|---|---|
| 0 | `0_hello_airflow` | Your first DAG | DAG object, operators, task dependencies, deploying a DAG file |
| 1 | `1_investing` | Top-level code cost | DAG-file parsing cost, why heavy work at import time slows the scheduler |
| 2 | `2_birthday` | Scheduling basics | `schedule` presets vs. cron expressions, aligning `start_date`, `catchup=False` |
| 3 | `3_birthday_full` | Templating with Jinja | Jinja-templated fields, `data_interval_end` (logical date) vs. wall-clock time |
| 4 | `4_saturday` | Catchup & backfills | `catchup=True`, backfill windows, logical/execution date vs. `datetime.now()`, skipped vs. failed states |
| 5 | `5_repetition` | DRY DAGs | Generating tasks/dependencies programmatically instead of copy-pasting |
| 6 | `6_failing_tasks` | Trigger rules | Default `ALL_SUCCESS`, `ALL_DONE`/`ONE_SUCCESS`, letting downstream work survive an upstream failure |
| 7 | `7_ignoring_failure` | Trigger rules with retries & branching | How retries interact with trigger rules, recombining a branch's skipped/succeeded paths |
| 8 | `8_reporting_sensor` | Cross-DAG dependencies: sensors | `ExternalTaskSensor`, why schedules/start_dates must line up across DAGs |
| 9 | `9_reporting_dataset_dependence` | Cross-DAG dependencies: datasets | Event-driven/data-aware scheduling (`Dataset`/outlets), contrast with interval-based scheduling |
| 10 | `10_xcoms_classicapi` / `10_xcoms_taskflowapi` | XComs & dynamic task mapping | Passing data via XCom, `.expand()`, classical API vs. TaskFlow API |
| 11 | `11_connections_and_hooks` | Connections & Hooks | Airflow Connections, `PostgresHook`, why hardcoded credentials in a DAG file are a security review finding |

## What's next

Once you've worked through these exercises, you've covered DAG
structure, scheduling, templating, trigger rules, cross-DAG
dependencies, XComs, and Connections & Hooks. A few more core Airflow
concepts are worth exploring on your own from here:

- **Sensor mechanics** — go back to `8_reporting_sensor` and try
  switching its `ExternalTaskSensor` to `mode="reschedule"`. Compare
  how that behaves versus the default `poke` mode, and look up
  `timeout` and `soft_fail` while you're there. A sensor stuck poking
  is a classic way to quietly starve an entire Airflow instance of
  worker slots.
- **Airflow Variables** — try storing a small config value (say, the
  schema name from exercise 11) as a Variable via "Admin > Variables"
  or `airflow variables set`, then read it back with `Variable.get()`
  in a DAG. It's the sibling of what exercise 11's Connections do for
  credentials, but for arbitrary config instead of secrets.
- **Failure notifications** — add an `on_failure_callback` (or
  `email_on_failure`) to one of the trigger-rule DAGs (6 or 7) and
  watch it fire when a task fails. Reliable alerting is a big part of
  "orchestrating work" once you're past the tutorial stage.

It's also worth reading up on Airflow's architecture (scheduler,
webserver, workers, executor types) even though there's no exercise
for it here — it's more conceptual than something you can poke at
hands-on in this environment.
