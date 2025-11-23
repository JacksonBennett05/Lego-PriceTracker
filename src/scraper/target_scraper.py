import requests
import json
import time
from urllib.parse import quote_plus

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/119.0.0.0 Safari/537.36",
  "Accept": "application/json",
  "Referer": "https://www.target.com/",
  "Origin": "https://www.target.com"
}

def scrape_target_lego(query, limit=5):
  """Scrape LEGO products from Target search API"""
  search_url = (
    "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?"
    "key=9f36aeafbe60771e321a7cc95a78140772ab3e96"
    f"&channel=WEB&count={limit}&default_purchasability_filter=true"
    f"&keyword={quote_plus(query)}"
    "&offset=0&page=%2Fs%2F{query}"
    "&pricing_store_id=3230"
    "&useragent=Mozilla/5.0"
    "&visitor_id=guest"
  )
  
  try:
    # print(f"\nSearching Target for: {query}")
    # print("=" * 60)
    
    resp = requests.get(search_url, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    
    # Extract products from search results
    search_data = data.get("data", {}).get("search", {})
    products_raw = search_data.get("products", [])
        
    products = []
    for idx, product in enumerate(products_raw):
      # print(f"\n[DEBUG] Product {idx + 1} keys: {list(product.keys())}")
      
      # Extract price
      price = "N/A"
      if "price" in product:
        # print(f"[DEBUG] Price keys: {list(product['price'].keys())}")
        price_obj = product["price"]
        price = (price_obj.get("formatted_current_price") or
                price_obj.get("current_retail") or
                str(price_obj.get("current_retail_price", "N/A")))
      
      # Extract name and URL
      item = product.get("item", {})
      prod_desc = item.get("product_description", {})
      enrichment = item.get("enrichment", {})
      
      name = prod_desc.get("title", "N/A")
      url = enrichment.get("buy_url", "N/A")
      
      # print(f"[DEBUG] Extracted - Name: {name[:50]}..., Price: {price}")
      
      product_info = {
        "Retailer": "Target",
        "Price": price,
        "URL": url
      }
      
      products.append(product_info)

    if products:
      return products[0]
    else:
      return None
  
  except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    return []

if __name__ == "__main__":
  results = scrape_target_lego("lego 75354", limit=1)