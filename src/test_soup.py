import requests
from bs4 import BeautifulSoup

url = "https://www.lego.com/en-us/search?q=75399"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify()[:2000])  # Shows the first 2000 characters
