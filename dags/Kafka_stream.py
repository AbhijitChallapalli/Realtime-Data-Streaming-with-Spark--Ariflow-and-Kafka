from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def stream_data():
    import json
    import requests

    res=requests.get("https://randomuser.me/api/")
    print(res.json())

default_args = {
    'owner':'Abhijit',
    'start_date':datetime(2024,6,18,13,44)
}

with DAG('user_automation',
        default_args=default_args,
        schdeule_interval='@daily',
        catchup=False) as dag:
    
    streaming_task= PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

stream_data()