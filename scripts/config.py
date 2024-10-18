# config.py
import requests
from bs4 import BeautifulSoup

# Base URL for the product list pages
base_url = 'https://gsm24.pl/12-smartfony'

# Function to determine the total number of pages dynamically
def get_total_pages(base_url):
    response = requests.get(base_url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assuming there's a pagination element that contains the total number of pages
    pagination = soup.find('ul', class_='page-list flex-container')
    
    if pagination:
        # Extract the last page number
        last_page_link = pagination.find_all('a')[-2]  # Usually, the second to last link
        if last_page_link:
            return int(last_page_link.text)
        
    else:
        return(10)
    
# Number of pages to scrape (determined dynamically)
total_pages = get_total_pages(base_url)

# Data points to extract from each product page
data_points = [
    ('name', 'h1', 'h1'),
    ('price', 'div', 'current-price'),
    ('guarantee', 'dd', 'value feat22'),
    ('operating_system', 'dd', 'value feat7', 'value feat8'),
    ('communication', 'dd', 'value feat17', 'value feat16'),
    ('battery', 'dd', 'value feat18'),
    ('processor', 'dd', 'value feat11'),
    ('ram', 'dd', 'value feat12'),
    ('capacity', 'dd', 'value feat13'),
    ('display', 'dd', 'value feat26'),
    ('display_diagonal', 'dd', 'value feat14'),
    ('display_resolution', 'dd', 'value feat15'),
    ('display_refresh_rate', 'dd', 'value feat15', 'value feat108'),
    ('front_cam_resolution', 'dd', 'value feat98'),
    ('back_cam_resolution', 'dd', 'value feat97'),
    ('wireless_charging', 'dd', 'value feat94'),
]
print("Config created")