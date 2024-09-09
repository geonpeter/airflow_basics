Airflow DAG Example
This repository contains an example of an Apache Airflow DAG that demonstrates basic usage of PythonOperator and BashOperator to define a simple workflow consisting of multiple tasks. The DAG executes a sequence of Python functions and Bash commands, scheduled to run every two minutes.

DAG Overview
The DAG named air_dag contains the following tasks:

Task 1 (task1): A Python function that prints "Task1 completed."
Sleep (sleep): A Bash command that pauses execution for 2 seconds using the sleep command.
Task 2 (task2): A Python function that prints "Task2 completed."
Task 3 (task3): A Bash command that echoes the message "Batch 1 is finished."
DAG Execution Flow
The tasks are executed in the following order:

task1: Executes the Python function task1_function().
sleep: Pauses execution for 2 seconds.
task2: Executes the Python function task2_function().
task3: Executes the Bash command to echo "Batch 1 is finished."
DAG Scheduling
The DAG is scheduled to run every 2 minutes, starting on September 9, 2024.

Code Explanation
The DAG code is defined as follows:

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime

def task1_function():
    print('Task1 completed.')

def task2_function():
    print('Task2 completed.')

# Default arguments for the DAG
default_args = {
    'owner': 'geonpeter',
    'start_date': datetime(2024, 9, 9),
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

# Define the DAG
with DAG(
    'air_dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=2)
) as dag:

    # Task 1: PythonOperator calling task1_function
    task1 = PythonOperator(task_id='task1', python_callable=task1_function)

    # Sleep Task: BashOperator executing a 2-second pause
    sleep = BashOperator(task_id='sleep', bash_command='sleep 2')

    # Task 2: PythonOperator calling task2_function
    task2 = PythonOperator(task_id='task2', python_callable=task2_function)

    # Task 3: BashOperator echoing a message
    task3 = BashOperator(task_id='task3', bash_command='echo "Batch 1 is finished."')

    # Set task dependencies: task1 -> sleep -> task2 -> task3
    task1 >> sleep >> task2 >> task3



Key Components
PythonOperator: Runs Python functions task1_function() and task2_function() as tasks.
BashOperator: Runs Bash commands such as sleep 2 and echo "Batch 1 is finished."
Task Dependencies: Defined using the >> operator to create a linear flow between tasks.

