import requests
from bs4 import BeautifulSoup

# def get_lego_price(set_num):
#   url = f"https://www.lego.com/en-us/search?q={set_num}"
#   headers = {"User-Agent": "Mozilla/5.0"}

#   response = requests.get(url, headers=headers)
#   soup = BeautifulSoup(response.text, "html.parser")