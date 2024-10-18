# main.py
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from scripts import config
from scripts import products_details_scrapper
from scripts import products_links_scrapper
from scripts import database

# Run each script in sequence
config.get_total_pages(config.base_url)
products_links = products_links_scrapper.scrape_product_links(config.base_url, config.total_pages)          # Assuming you have defined a run_scraper() function
products_details = products_details_scrapper.scrape_product_details(products_links, config.data_points) # Assuming you have defined a run_extractor() function
database.save_to_postgres(products_details, postgres_conn_id='db_conn_jakub')          # Assuming you have defined a save_to_db() function
