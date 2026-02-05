def find_cheapest(lego, target, walmart):
  lego_price = lego.get("Price")
  target_price = target.get("Price")
  walmart_price = walmart.get("Price")

  lego_price = float(lego_price.strip('$'))
  target_price = float(target_price.strip('$'))
  walmart_price = float(walmart_price.strip('$'))
  
  if lego_price < target_price and walmart_price < target_price:
    print(f"Lego.com is cheapest at ${lego_price}")
  elif target_price < walmart_price and target_price < lego_price: 
    print(f"Target.com is cheapest at ${target_price}")
  else:
    print(f"Walmart.com is cheapest at ${walmart_price}")
