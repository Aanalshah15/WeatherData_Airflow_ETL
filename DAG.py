from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from .weather_etl import run_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,11,8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'weather_dag',
    default_args=default_args,
    description="my first dag"
)

run_dag = PythonOperator(
    task_id='complete_weather_dag',
    python_callable=run_etl,
    dag = dag
)

run_dag