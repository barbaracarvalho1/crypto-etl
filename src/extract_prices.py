import requests
import time
from datetime import datetime, date
from dotenv import load_dotenv
import os
import json

load_dotenv() 

URL = os.getenv("COINGECKO_API_URL")
COINS = os.getenv("COINS")
CURRENCIES = os.getenv("CURRENCIES")
OUTPUT_FILE = os.getenv("OUTPUT_FILE", f"crypto_events_{date.today().strftime('%Y-%m-%d')}.json")

PARAMS = {
    "ids": COINS,
    "vs_currencies": CURRENCIES
}

def save_event(event, filename=OUTPUT_FILE):
    """Append event to JSON file."""
    try:
        with open(filename, "a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception as e:
        print(f"Error saving event: {e}")

def extract_prices_into_json():
    while True:
        try:
            response = requests.get(URL, params=PARAMS)
            data = response.json()

            event = {
                "timestamp": datetime.utcnow().isoformat(),
                "data": data
            }

            save_event(event)
            print(f"Saved event at {event['timestamp']}")

        except Exception as e:
            print(f"Error fetching data: {e}")

        time.sleep(30)