import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

side = soup.find("div", class_="side_categories")

print(side)