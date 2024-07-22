from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import date, datetime
import os
import sys
# Thêm đường dẫn thư mục hiện tại vào sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

default_args = {
    'owner' : 'ClarkSonTech',
    'start_date' : datetime.now(),
    
}
file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags = ['reddit', 'etl' , 'pipeline']
)
#extract from reddit api
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline,
    op_kwargs={
        'file_name' : f'reddit_{file_postfix}',
        'subreddit' :'dataengineering',
        'time_filter' : 'day',
        'limit' : 100
    }
)


