# product_link_scraper.py
import requests
from bs4 import BeautifulSoup
import time

# Function to scrape product links
def scrape_product_links(base_url, total_pages):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }


    products_links = []

    # Iterate over pages
    for x in range(1, total_pages + 1):
        print(f"Scraping page {x}...")

        # Make a request to the page
        response = requests.get(f'{base_url}?page={x}', headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch page {x}, status code: {response.status_code}")
            continue  # Skip to the next iteration if there's an error fetching the page

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all product containers
        products = soup.find_all('div', class_='thumbnail product-thumbnail relative flex-container')

        # Extract links from each product container
        for item in products:
            link_tag = item.find('a', class_='relative subimage-true')
            if link_tag:
                href = link_tag.get('href')
                products_links.append(href)
                print(f"Found product link: {href}")

        time.sleep(3)  # Respectful scraping, avoid overwhelming the server

    return products_links
print("Products links functions created")