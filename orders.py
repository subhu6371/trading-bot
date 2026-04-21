from binance.exceptions import BinanceAPIException, BinanceOrderException
from bot.client import get_client
from bot.logging_config import logger

def execute_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    client = get_client()
    
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC" # Required for limit orders on Binance

    logger.info(f"Attempting to place {order_type} {side} order for {quantity} {symbol}...")

    try:
        # Use futures_create_order specifically for the USDT-M futures testnet
        response = client.futures_create_order(**params)
        logger.info(f"Order Success | ID: {response.get('orderId')} | Status: {response.get('status')}")
        return response

    except (BinanceAPIException, BinanceOrderException) as e:
        logger.error(f"Binance API Error: {e.message} (Code: {e.code})")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        raise