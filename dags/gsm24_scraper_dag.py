# gsm24_scraper_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.product_link_scraper import scrape_product_links
from scripts.product_details_scraper import scrape_product_details
from scripts.database import save_to_postgres
from scripts.config import base_url, total_pages, data_points

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'gsm24_scraper_to_postgres',
    default_args=default_args,
    description='Scrape new smartphones from GSM24 and save to PostgreSQL',
    schedule_interval='0 0 * * 0',  # Every Sunday at midnight
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

def scrape_and_save(**context):
    products_links = scrape_product_links(base_url, total_pages)
    smartphones = scrape_product_details(products_links, data_points)
    save_to_postgres(smartphones)

scrape_and_save_task = PythonOperator(
    task_id='scrape_and_save_to_postgres',
    python_callable=scrape_and_save,
    dag=dag,
)
