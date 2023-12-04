from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from hazySkies import blurrr
from transform_one import cloudburst
from featureExtraction import feature_extract
from lstm_file import lstm_model
from featureReverse import feature_reverse
from load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 12),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}
dag = DAG(
    'hazySky_ingest_dag',
    default_args=default_args,
    description='ingest air quality data',
    schedule_interval=timedelta(days=1),
)
hazy_etl = PythonOperator(
    task_id='blurrr',
    python_callable=blurrr,
    dag=dag,
)

transone_etl = PythonOperator(
    task_id='cloudburst',
    python_callable=cloudburst,
    dag=dag,
)
featureExtract_etl = PythonOperator(
    task_id='feature_extract',
    python_callable=feature_extract,
    dag=dag,
)
lstm_etl = PythonOperator(
    task_id='lstm_model',
    python_callable=lstm_model,
    dag=dag,
)
featureReverse_etl = PythonOperator(
    task_id='feature_reverse',
    python_callable=feature_reverse,
    dag=dag,
)
load_etl = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)


hazy_etl >> transone_etl >> featureExtract_etl >> lstm_etl >> featureReverse_etl >> load_etl
