import requests
from bs4 import BeautifulSoup

def get_target_price(set_num):
  search_url = f"https://www.target.com/s?searchTerm={set_num}+lego"
  headers = {"User-Agent": "Mozilla/5.0"}
  r = requests.get(search_url, headers=headers)
  soup = BeautifulSoup(r.text, "html.parser")

  product_tag = soup.find("a", {"data-test": "product-title"})
  if not product_tag:
    return {"error": "Set not found on Target"}
    
  product_url = "https://www.target.com" + product_tag["href"]

  product_page = requests.get(product_url, headers=headers)
  psoup = BeautifulSoup(product_page.text, "html.parser")

  name_tag = psoup.find("h1", {"data-test": "product-title"})
  price_tag = psoup.find("span", {"data-test": "product-price"})
  
  name = name_tag.text.strip() if name_tag else "Unknown"
  price = price_tag.text.strip() if price_tag else "N/A"
  
  return {
    "set_num": set_num,
    "name": name,
    "price": price,
    "url": product_url
  }