import os
import re
import requests
from dotenv import load_dotenv
from urllib.parse import quote_plus
from typing import Optional
from html import unescape

load_dotenv()
SCRAPER_API_KEY = os.getenv("SCRAPER_API")


def clean_product_name(name: str) -> str:
  return name.split(" - ", 1)[0]


def _canonical_walmart_url(url: str) -> str:
  # Keep it short + stable: strip query params
  return url.split("?", 1)[0]


def search_walmart_product(query: str) -> Optional[str]:
  if not SCRAPER_API_KEY:
    return None

  search_url = f"https://www.walmart.com/search?q={quote_plus(query)}"

  params = {
    "api_key": SCRAPER_API_KEY,
    "url": search_url,
    "render": "true"
  }

  headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
  }

  try:
    r = requests.get(
      "https://api.scraperapi.com/",
      params=params,
      headers=headers,
      timeout=60
    )
    r.raise_for_status()

    html = unescape(r.text)

    # Walmart product URLs usually look like:
    # /ip/NAME/1234567890
    # Sometimes links appear as https://www.walmart.com/ip/...
    m = re.search(r'https?://www\.walmart\.com/ip/[^"\s<>]+', html)
    if m:
      return _canonical_walmart_url(m.group(0))

    m = re.search(r'"/ip/[^"\s<>]+', html)
    if m:
      rel = m.group(0).strip('"')
      return _canonical_walmart_url("https://www.walmart.com" + rel)

    return None

  except Exception:
    return None


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


def get_walmart_price_by_query(query: str) -> dict:
  product_url = search_walmart_product(query)

  if not product_url:
    return {
      "error": "No Walmart product found",
      "query": query
    }

  return get_walmart_price_scraperapi(product_url)


if __name__ == "__main__":
  print(get_walmart_price_by_query("lego 75399"))
