from scraper.lego_scraper import brickset_login, get_lego_price
from scraper.walmart_scraper import get_walmart_price
from utils.compare import find_cheapest
import os

def main():
  API_KEY = os.getenv("BRICKSET_API_KEY")
  USERNAME = os.getenv("BRICKSET_USER")
  PASSWORD = os.getenv("BRICKSET_PASS")

  user_hash = brickset_login(API_KEY, USERNAME, PASSWORD)
  if not user_hash:
    print("Login failed check your .env credentials.")
    return
  correct = False
  
  while not correct: 
    set_number = input("Enter LEGO set number: ").strip()
    lego_set = get_lego_price(set_number, API_KEY, user_hash)
    walmart_set = get_walmart_price(set_number)
    print(lego_set)
  
    is_correct = input("Is this the correct set (Y/N)? ").upper().strip()
    if(is_correct == "Y"):
      correct = True
      
  lego_price_json = {"lego.com": lego_set.get("Price")}
  walmart_price_json = {"walmart.com": walmart_set.get("Price")}
  print(lego_price_json)
  print(walmart_price_json)
  
if __name__ =="__main__":
  main()