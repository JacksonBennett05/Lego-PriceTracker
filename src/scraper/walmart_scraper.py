# import json
# from playwright.sync_api import sync_playwright
# import re

# def get_walmart_price(set_num):
#   with sync_playwright() as p:
#     browser = p.firefox.launch(headless=True)
#     page = browser.new_page()
#     page.goto(f"https://www.walmart.com/search?q={set_num}+lego", timeout=60000)
#     html = page.content()
#     browser.close()

#   # Walmart embeds JSON in <script id="__NEXT_DATA__" type="application/json">...</script>
#   match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
#   if not match:
#     return {"error": "Could not locate __NEXT_DATA__ JSON"}

#   json_text = match.group(1).strip()
#   try:
#     data = json.loads(json_text)
#   except Exception as e:
#     return {"error": f"Failed to parse Walmart JSON: {e}"}

#   try:
#     product = data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["items"][0]
#     price = product.get("priceInfo", {}).get("priceDisplay", "N/A")
#     url = "https://www.walmart.com" + product.get("canonicalUrl", "")
#     return {"set_num": set_num, "price": price, "url": url}
#   except Exception as e:
#     return {"error": f"Failed to extract data: {e}"}

# if __name__ == "__main__":
#   print(get_walmart_price("75399"))
"""
Walmart LEGO Scraper

IMPORTANT: Walmart has very aggressive bot detection that blocks automated scraping.
This script won't work reliably without additional measures.

Options to make this work:

1. Use a scraping service like:
   - ScraperAPI (https://www.scraperapi.com/)
   - Bright Data (https://brightdata.com/)
   - Oxylabs (https://oxylabs.io/)
   These services handle CAPTCHAs and bot detection for you.

2. Use Playwright with stealth plugins:
   - playwright-stealth
   - Add realistic delays and mouse movements
   - Use residential proxies

3. Use Walmart's official API (if available for your use case)

4. Manual option: Just check Walmart prices manually for now

For this project, I recommend focusing on retailers with friendlier scraping policies
(like Target which works well), or using a paid scraping service for Walmart.
"""

import json
from playwright.sync_api import sync_playwright
from urllib.parse import quote_plus

def scrape_walmart_lego(query, limit=1):
  """
  Attempt to scrape Walmart (likely to be blocked by CAPTCHA)
  
  This function is provided as a template but will likely not work
  due to Walmart's bot detection.
  """
  
  print(f"\nSearching Walmart for: {query}")
  print("=" * 60)
  print("[WARNING] Walmart has aggressive bot detection.")
  print("[WARNING] This scraper will likely be blocked by CAPTCHA.")
  print("=" * 60)
  
  # Placeholder return for when blocked
  return [{
    "Retailer": "Walmart",
    "Price": "BLOCKED - Bot detection active",
    "URL": f"https://www.walmart.com/search?q={quote_plus(query + ' lego')}"
  }]

def scrape_walmart_with_scraperapi(query, api_key, limit=1):
  """
  Alternative: Use ScraperAPI to bypass Walmart's bot detection
  
  Sign up at https://www.scraperapi.com/ for an API key
  Free tier: 1,000 requests/month
  
  Usage:
    api_key = "your_scraperapi_key_here"
    results = scrape_walmart_with_scraperapi("75399", api_key)
  """
  import requests
  
  print(f"\nSearching Walmart via ScraperAPI for: {query}")
  print("=" * 60)
  
  # ScraperAPI endpoint
  target_url = f"https://www.walmart.com/search?q={quote_plus(query + ' lego')}"
  
  params = {
    'api_key': api_key,
    'url': target_url,
    'render': 'true'  # Enable JavaScript rendering
  }
  
  try:
    response = requests.get('http://api.scraperapi.com/', params=params, timeout=60)
    response.raise_for_status()
    
    html = response.text
    
    # Save for debugging
    with open("walmart_scraperapi_debug.html", "w", encoding="utf-8") as f:
      f.write(html)
    
    # Now parse the HTML for product data
    # (Similar logic to before, but now we have the actual page)
    
    print("[SUCCESS] Page retrieved via ScraperAPI")
    print("[INFO] HTML saved to walmart_scraperapi_debug.html")
    print("[TODO] Add JSON parsing logic here")
    
    return [{
      "Retailer": "Walmart",
      "Price": "N/A - Parse the HTML from walmart_scraperapi_debug.html",
      "URL": target_url
    }]
    
  except Exception as e:
    print(f"[ERROR] ScraperAPI failed: {e}")
    return []

def scrape_walmart_manual_instructions(query):
  """
  Print instructions for manually checking Walmart prices
  """
  print(f"\nManual Walmart Price Check Instructions:")
  print("=" * 60)
  print(f"1. Visit: https://www.walmart.com/search?q={quote_plus(query + ' lego')}")
  print(f"2. Find the '{query}' LEGO set in the results")
  print(f"3. Note the price and URL")
  print(f"4. Return format: {{'Retailer': 'Walmart', 'Price': '$XX.XX', 'URL': '...'}}")
  print("=" * 60)

if __name__ == "__main__":
  # Default: Just show it's blocked
  results = scrape_walmart_lego("75399", limit=1)
  print("\nResults:")
  print("-" * 60)
  for prod in results:
    print(prod)
  
  print("\n" + "=" * 60)
  print("RECOMMENDATION:")
  print("- Skip Walmart for now and focus on Target (which works)")
  print("- Or use a paid service like ScraperAPI")
  print("- Or check Walmart prices manually when needed")
  print("=" * 60)
  
  # Show manual instructions as alternative
  print()
  scrape_walmart_manual_instructions("75399")