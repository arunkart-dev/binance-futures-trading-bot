def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M futures pairs allowed")

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

def validate_price(price):
    if price <= 0:
        raise ValueError("Price must be greater than 0")
