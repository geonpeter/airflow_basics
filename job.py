from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import timedelta,datetime

def task1_function():
    print('Task1 completed.')

def task2_function():
    print('Task2 completed.')

default_args = {
    'owner' : 'air0',
    'start_date' : datetime(2029,09,09),
    'retries' : 1,
    'retry_delay' : timedelta(minutes=2)
}

with DAG(
    'air_dag',
    default_args = default_args,
    schedule_interval = timedelta(minutes=2)
) as dag:
    
    task1 = PythonOperator(task_id = 'task1', python_callable= task1_function)

    sleep = BashOperator(task_id = 'sleep', bash_command= 'sleep 2')

    task2 = PythonOperator(task_id = 'task2', python_callable= task2_function)

    task3 = BashOperator (task_id = 'task3', bash_command= 'echo "Batch 1 is finished."')
    
  

    task1 >> sleep >> task2