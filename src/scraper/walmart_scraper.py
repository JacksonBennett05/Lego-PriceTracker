import json
from playwright.sync_api import sync_playwright
import re

def get_walmart_price(set_num):
  with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    page = browser.new_page()
    page.goto(f"https://www.walmart.com/search?q={set_num}+lego", timeout=60000)
    html = page.content()
    browser.close()

  # Walmart embeds JSON in <script id="__NEXT_DATA__" type="application/json">...</script>
  match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
  if not match:
    return {"error": "Could not locate __NEXT_DATA__ JSON"}

  json_text = match.group(1).strip()
  try:
    data = json.loads(json_text)
  except Exception as e:
    return {"error": f"Failed to parse Walmart JSON: {e}"}

  try:
    product = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["items"][0]
    price = product.get("priceInfo", {}).get("priceDisplay", "N/A")
    url = "https://www.walmart.com" + product.get("canonicalUrl", "")
    return {"set_num": set_num, "price": price, "url": url}
  except Exception as e:
    return {"error": f"Failed to extract data: {e}"}

if __name__ == "__main__":
  print(get_walmart_price("75399"))
