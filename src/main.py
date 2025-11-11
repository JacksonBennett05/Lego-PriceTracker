from scraper.lego_scraper import brickset_login, get_lego_price
from scraper.walmart_scraper import get_walmart_price
from scraper.target_scraper import scrape_target_lego
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
    print(lego_set)
  
    is_correct = input("Is this the correct set (Y/N)? ").upper().strip()
    if(is_correct == "Y"):
      correct = True
      
  walmart_set = get_walmart_price(set_number)
  target_set = scrape_target_lego(f"lego {set_number}")
  lego_price_json = {"lego.com": lego_set.get("Price", "N/A") if lego_set else "N/A"}
  walmart_price_json = {"walmart.com": walmart_set.get("Price", "N/A") if walmart_set else "N/A"}
  target_price_json = {"target.com": target_set.get("Price", "N/A") if target_set else "N/A"}
  print(lego_price_json)
  print(target_price_json)
  print(walmart_price_json)
  
if __name__ =="__main__":
  main()