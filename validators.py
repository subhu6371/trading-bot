def validate_order_input(order_type: str, price: float = None):
    valid_types = ["MARKET", "LIMIT"]
    
    if order_type.upper() not in valid_types:
        raise ValueError(f"Invalid order type. Must be one of: {valid_types}")

    if order_type.upper() == "LIMIT" and price is None:
        raise ValueError("A price must be provided for LIMIT orders.")