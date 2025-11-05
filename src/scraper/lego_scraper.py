import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("BRICKSET_API_KEY")
USERNAME = os.getenv("BRICKSET_USER")
PASSWORD = os.getenv("BRICKSET_PASS")


def brickset_login(api_key, username, password):
  url = "https://brickset.com/api/v3.asmx/login"
  params = {
    "apiKey": api_key,
    "username": username,
    "password": password
  }
  r = requests.get(url, params=params)
  data = r.json()
  return data.get("hash")

def get_lego_price(set_num, api_key, user_hash):
  url = "https://brickset.com/api/v3.asmx/getSets"
  params = {
    "apiKey": api_key,
    "userHash": user_hash,
    "params": json.dumps({
      "setNumber": f"{set_num}-1", 
      "extendedData": True,
      "countryCode": "US"
    }),
    "format": "json"
  }
  r = requests.get(url, params=params)
  data = r.json()
  sets = data.get("sets")
  if not sets:
    return {"Set Name": "N/A", "Retailer": "LEGO", "Price": "N/A", "URL": "https://brickset.com"}
  
  set_info = sets[0]
  name = set_info.get("name", "Unknown Set")
  price = None
  
  try: 
    price = set_info["LEGOCom"]["US"]["retailPrice"]
  except KeyError:
    price = "N/A"
  
  if price != "N/A":
    price = f"${price}"

  return {
    "Set Name": name,
    "Retailer": "LEGO",
    "Price": price,
    "URL": set_info.get("bricksetURL", "https://brickset.com")
  }

if __name__ == "__main__":
  user_hash = brickset_login(API_KEY, USERNAME, PASSWORD)
  print("User hash:", user_hash)
  if user_hash:
    print(get_lego_price("75399", API_KEY, user_hash))
  else:
    print("Login failed")