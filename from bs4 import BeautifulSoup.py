from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

headers = {
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

time.sleep(3)


# List to store all product links
products_links = []

# Iterate over pages
for x in range(1, 18):
    print(f"Scraping page {x}...")
    
    # Make a request to the page
    response = requests.get(f'https://gsm24.pl/12-smartfony?page={x}')
    
    if response.status_code != 200:
        print(f"Failed to fetch page {x}, status code: {response.status_code}")
        continue  # Skip to the next iteration if there's an error fetching the page
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers
    products = soup.find_all('div', class_='thumbnail product-thumbnail relative flex-container')
    
    # Extract links from each product container
    for item in products:
        # Find the <a> tag with the class "relative subimage-true"
        link_tag = item.find('a', class_='relative subimage-true')
        
        if link_tag:
            href = link_tag.get('href')
            products_links.append(href)
            print(f"Found product link: {href}")
import requests
from bs4 import BeautifulSoup

# Helper function to extract text or return 'NA'
def extract_text(soup, *classes):
    for class_name in classes:
        element = soup.find('dd', class_=class_name)
        if element:
            return element.text.strip()
    return 'NA'

# List of data points to extract
data_points = [
    ('name', 'h1', 'h1'),
    ('price', 'div', 'current-price'),
    ('guarantee', 'dd', 'value feat22'),
    ('operating_system', 'dd', 'value feat7', 'value feat8'),
    ('communication', 'dd', 'value feat17', 'value feat16'),
    ('baterry', 'dd', 'value feat18'),
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

smartphones = []

# Use a session to improve efficiency of repeated requests
with requests.Session() as session:
    for link in products_links:
        print(link)
        response = session.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        smartphone = {}
        
        for key, tag, *classes in data_points:
            if tag == 'h1' or tag == 'div':  # Special handling for name and price
                element = soup.find(tag, class_=classes[0])
                smartphone[key] = element.text.strip() if element else 'NA'
            else:
                smartphone[key] = extract_text(soup, *classes)

        smartphones.append(smartphone)
