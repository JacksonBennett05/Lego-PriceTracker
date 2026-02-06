def find_cheapest(lego, target, walmart):
  prices = {
    "Lego.com": lego.get("Price"),
    "Target.com": target.get("Price"),
    "Walmart.com": walmart.get("Price")
  }

  clean_prices = {}
  for store, price in prices.items():
    try:
      clean_prices[store] = float(price.replace("$", ""))
    except (TypeError, ValueError):
      continue
  
  if not clean_prices:
    print("No prices available")
  else:
    cheapest_store = min(clean_prices, key=clean_prices.get)
    cheapest_price = clean_prices[cheapest_store]
    print(f"{cheapest_store} is the cheapest at ${cheapest_price}")