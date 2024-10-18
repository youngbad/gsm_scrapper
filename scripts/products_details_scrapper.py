# product_details_scraper.py
import requests
from bs4 import BeautifulSoup

# Helper function to extract text or return 'NA'
def extract_text(soup, *classes):
    for class_name in classes:
        element = soup.find('dd', class_=class_name)
        if element:
            return element.text.strip()
    return 'NA'

# Function to scrape product details
def scrape_product_details(products_links, data_points):
    smartphones = []

    with requests.Session() as session:
        for link in products_links:
            print(f"Scraping product details from: {link}")
            response = session.get(link)
            soup = BeautifulSoup(response.content, 'html.parser')

            smartphone = {'url': link}
            
            for key, tag, *classes in data_points:
                if tag == 'h1' or tag == 'div':  # Special handling for name and price
                    element = soup.find(tag, class_=classes[0])
                    smartphone[key] = element.text.strip() if element else 'NA'
                else:
                    smartphone[key] = extract_text(soup, *classes)
            
            smartphones.append(smartphone)
    
    return smartphones
print("Product details functions created")