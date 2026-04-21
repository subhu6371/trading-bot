import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_SECRET_KEY")
    
    if not api_key or not api_secret:
        raise ValueError("API keys not found. Please check your .env file.")

    # testnet=True routes requests to the testnet URL automatically
    return Client(api_key, api_secret, testnet=True)