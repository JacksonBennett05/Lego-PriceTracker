import os
import requests
from dotenv import load_dotenv

load_dotenv()
SCRAPER_API_KEY = os.getenv("SCRAPER_API")


def get_walmart_price_scraperapi(product_url: str) -> dict:
  if not SCRAPER_API_KEY:
    return {
      "error": "Missing SCRAPER_API key",
      "url": product_url
    }

  params = {
    "api_key": SCRAPER_API_KEY,
    "url": product_url,
    "autoparse": "true",
    "render": "true",
    "output_format": "json",
    "follow_redirect": "false"
  }

  try:
    r = requests.get(
      "https://api.scraperapi.com/",
      params=params,
      timeout=60
    )
    r.raise_for_status()
    data = r.json()

    price = data.get("price")

    raw_name = data.get("product_name")
    name = clean_product_name(raw_name) if raw_name else None

    if price is None:
      return {
        "error": "Price not found in ScraperAPI response",
        "url": product_url
      }

    return {
      "retailer": "Walmart",
      "name": name,
      "price": f"${price}",
      "url": product_url
    }

  except Exception as e:
    return {
      "error": str(e),
      "url": product_url
    }
    
    
def clean_product_name(name: str) -> str:
  return name.split(" - ", 1)[0]

if __name__ == "__main__":
  url = "https://www.walmart.com/ip/LEGO-Speed-Champions-77255/17115356372"
  print(get_walmart_price_scraperapi(url))
