from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator  # Incorrect import

dag = DAG(
    dag_id="broken_dag",
    schedule_interval=None,
    start_date="2024-01-01",  # Incorrect start_date format (should be datetime)
)

task = DummyOperator(task_id="dummy", dag=dag)
