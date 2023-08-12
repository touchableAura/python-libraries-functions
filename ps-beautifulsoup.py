from bs4 import BeautifulSoup
import requests
import os 
import re 

url = "htpp://127.0.0.1./pluralsight/sample.html"
website = requests.get(url)
bf4_web = BeautifulSoup(website.text, "lxml")

# pull out individual products with findall
products = bf4_web.find_all(class_="product")
# regex alternative: search for header contents instead 
#pattern = requests.get(url)
#product_results = pattner.search(website.text)

for product in products:
    prod_details = str(product).split("<br/>")
    print("-----------------------------------------")
    with open(prod_details[0][47:-3].split("/")[2], 'wb'/) as pic:
