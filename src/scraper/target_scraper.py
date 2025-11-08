# import json, re, time, requests
# from playwright.sync_api import sync_playwright

# headers = {
#   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                 "AppleWebKit/537.36 (KHTML, like Gecko) "
#                 "Chrome/119.0.0.0 Safari/537.36",
#   "Referer": "https://www.target.com/",
#   "Origin": "https://www.target.com"
# }

# def get_tcins_playwright(query):
#   """Use Playwright to load the search page and extract tcins."""
#   with sync_playwright() as p:
#     browser = p.firefox.launch(headless=True)
#     page = browser.new_page()
#     url = f"https://www.target.com/s?searchTerm={query.replace(' ', '+')}"
#     page.goto(url)
#     page.wait_for_timeout(4000)  # wait for JS to load results
#     html = page.content()
#     browser.close()

#   tcins = re.findall(r'data-tcin="(\d+)"', html)
#   tcins = list(dict.fromkeys(tcins))
#   print(f"Found {len(tcins)} tcins:", tcins[:5])
#   return tcins[:3]

# def get_product_urls(tcins):
#   """Get canonical product URLs from Target's fulfillment API."""
#   if not tcins:
#     return []
#   tcin_str = ",".join(tcins)
#   api_url = (
#     "https://redsky.target.com/redsky_aggregations/v1/web/"
#     f"product_summary_with_fulfillment_v1?"
#     "key=9f36aeafbe60771e321a7cc95a78140772ab3e96"
#     f"&tcins={tcin_str}&store_id=3230&zip=36100"
#   )
#   r = requests.get(api_url, headers=headers)
#   if r.status_code != 200:
#     print("Fulfillment API failed:", r.status_code)
#     return []
#   data = r.json()
#   urls = [
#     p["item"]["enrichment"]["buy_url"]
#     for p in data.get("data", {}).get("product_summaries", [])
#     if p.get("item", {}).get("enrichment", {}).get("buy_url")
#   ]
#   print("Product URLs:", urls)
#   return urls

# def scrape_product_page(url):
#   """Extract product info from JSON embedded in the product page."""
#   pattern = r"window\.__TGT_DATA__\s*=\s*({.*?})\s*;</script>"
#   r = requests.get(url, headers=headers)
#   if r.status_code != 200:
#     print("Page request failed:", r.status_code)
#     return None
#   match = re.search(pattern, r.text, re.DOTALL)
#   if not match:
#     print("No embedded JSON found for", url)
#     return None
#   tgt_json = json.loads(match.group(1))
#   product_data = tgt_json.get("product", {}).get("item", {})
#   name = product_data.get("product_description", {}).get("title", "N/A")
#   price = product_data.get("price", {}).get("current_retail", "N/A")
#   rating = product_data.get("ratings_and_reviews", {}).get("statistics", {}).get("rating", "No ratings")
#   return {"name": name, "price": price, "rating": rating, "url": url}

# def scrape_target(query):
#   tcins = get_tcins_playwright(query)
#   urls = get_product_urls(tcins)
#   results = []
#   for url in urls:
#     print(f"Scraping {url}")
#     data = scrape_product_page(url)
#     if data:
#       results.append(data)
#     time.sleep(1.5)
#   with open("target_data.json", "w", encoding="utf-8") as f:
#     json.dump(results, f, indent=2, ensure_ascii=False)
#   print(f"Done. Saved {len(results)} items to target_data.json")

# if __name__ == "__main__":
#   scrape_target("lego 75399")


# import requests, json, re

# headers = {
#   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                 "AppleWebKit/537.36 (KHTML, like Gecko) "
#                 "Chrome/119.0.0.0 Safari/537.36",
#   "Accept": "application/json",
#   "Referer": "https://www.target.com/",
#   "Origin": "https://www.target.com"
# }

# # Step 1 – fetch product URLs from the example API
# api_url = (
#   "https://redsky.target.com/redsky_aggregations/v1/web/"
#   "product_summary_with_fulfillment_v1?"
#   "key=9f36aeafbe60771e321a7cc95a78140772ab3e96"
#   "&tcins=90381165,90381177,90471876,90471877,90471880"
#   "&store_id=3230&zip=36100"
# )

# resp = requests.get(api_url, headers=headers)
# print("API status:", resp.status_code)
# data = resp.json()

# urls = [
#   p["item"]["enrichment"]["buy_url"]
#   for p in data.get("data", {}).get("product_summaries", [])
#   if p.get("item", {}).get("enrichment", {}).get("buy_url")
# ]

# print("Found URLs:", urls)

# # Step 2 extract product info from one product page
# pattern = r"__TGT_DATA__':\s*{\s*configurable:\s*false,\s*enumerable:\s*true,\s*value:\s*deepFreeze\(JSON\.parse\(\"(.*?)\"\)\)"

# product_details = []
# for url in urls[:1]:
#   try:
#     print(f"Scraping {url}")
#     r = requests.get(url, headers=headers)
#     r.raise_for_status()

#     match = re.search(pattern, r.text, re.DOTALL)
#     if not match:
#       print("No embedded JSON found.")
#       continue

#     json_str = match.group(1).encode("utf-8").decode("unicode_escape")
#     tgt_json = json.loads(json_str)

#     # navigate to data
#     queries = tgt_json.get("__PRELOADED_QUERIES__", {}).get("queries", [])
#     product_data = queries[3][1].get("data", {}).get("product", {}) if len(queries) > 3 else {}

#     item_info = product_data.get("item", {}).get("product_description", {})
#     price_info = product_data.get("price", {})
#     rating_info = product_data.get("ratings_and_reviews", {}).get("statistics", {})

#     details = {
#       "name": item_info.get("title", "N/A"),
#       "description": item_info.get("downstream_description", "No description"),
#       "features": item_info.get("soft_bullets", {}).get("bullets", []),
#       "price": price_info.get("current_retail", "N/A"),
#       "average_rating": rating_info.get("rating", "No ratings"),
#       "url": url
#     }
#     product_details.append(details)
#     print("Scraped:", details["name"])

#   except Exception as e:
#     print("Error scraping", url, ":", e)

# # Step 3 save results
# with open("target_data.json", "w", encoding="utf-8") as f:
#   json.dump(product_details, f, indent=2, ensure_ascii=False)

# print("Done, saved to target_data.json")