import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow import models
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.utils.dates import days_ago

DATASET_NAME = os.environ.get("GCP_DATASET_NAME", 'online_retail')
TABLE_NAME = os.environ.get("GCP_TABLE_NAME", 'raw_online_retail')

default_args={
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'online_retail',
    default_args=default_args,
    description='online retail pipeline',
    schedule_interval="@monthly",
    start_date=datetime(2024, 1, 1),
    tags=['example'],
) as dag:
    download_dataset_task = BashOperator(
        task_id="download_dataset_drive",
        bash_command="download_data.sh"
    )
up_to_gcs = LocalFilesystemToGCSOperator(
    task_id="up_data_to_gcs",
    src='/opt/airflow/dags/include/OnlineRetail.csv',  
    dst='raw/OnlineRetail.csv',  
    bucket="online-retail-data",
    mime_type='text/csv',
    gcp_conn_id='google_cloud_default'  # Ganti dengan ID koneksi yang telah dibuat di Airflow UI
)
create_test_dataset = BigQueryCreateEmptyDatasetOperator(
    task_id='create_airflow_test_dataset', dataset_id=DATASET_NAME, dag=dag
)
load_raw_data_to_bq = GCSToBigQueryOperator(
    task_id='raw_gcs_to_bigquery',
    bucket='online-retail-data',
    source_objects=['raw/OnlineRetail.csv'],
    destination_project_dataset_table=f"{DATASET_NAME}.{TABLE_NAME}",
    create_disposition='CREATE_IF_NEEDED',
    source_format='CSV',  # Ubah format menjadi CSV
    write_disposition='WRITE_TRUNCATE',
    dag=dag,
)
transform = BashOperator(
        task_id="transform",
        bash_command="dbt run --project-dir /opt/airflow/dags/dbts/project-dbt/OnlineRetail --profiles-dir /opt/airflow/dags/dbts/project-dbt/OnlineRetail",
    )

download_dataset_task >> up_to_gcs >>create_test_dataset>> load_raw_data_to_bq>>transform