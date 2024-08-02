import os
import sys
from datetime import datetime
from airflow import DAG

sys.path.insert(0 , os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

defaults_dag = {
    'owner': 'ClarkSon',
    'start_date': datetime.now()
}

file_postfix = datetime.now().strftime('%Y%m%d')
dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args= defaults_dag , 
    schedule_interval= '@daily',
    catchup= False,
    tags=['reddit' , 'etl' , 'pipeline']
)




