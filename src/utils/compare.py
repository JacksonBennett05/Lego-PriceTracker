def find_cheapest(lego, target):
  lego_price = lego.get("Price")
  target_price = target.get("Price")

  lego_price = float(lego_price.strip('$'))
  target_price = float(target_price.strip('$'))
  
  if lego_price < target_price:
    print(f"Lego.com is cheaper at {lego_price}")
  else: 
    print(f"Target.com is cheaper {target_price}")
