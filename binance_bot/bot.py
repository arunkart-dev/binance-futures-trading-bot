import sys
from binance import Client
from logger import logger
from validators import validate_symbol, validate_quantity, validate_price

API_KEY = "1dbiPkM3dZ5xb4ywkicn5sFGujPK29oPUX48bqJSdri6zefHLUuTPgGhskR4Ss6b"
API_SECRET = "bAsBuv1vkRc548UwLl2NKfR3uGAWuD79TETYDNvTTFamGXej9pWUUafLoj7Dd7vE"


class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)

    def _server_timestamp(self):
        return self.client.futures_time()["serverTime"]

    def market_order(self, symbol, side, quantity):
        try:
            validate_symbol(symbol)
            validate_quantity(quantity)

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
                timestamp=self._server_timestamp(),  # ⭐ FIX
                recvWindow=20000
            )

            logger.info(order)
            print("✅ Market order placed successfully")
            print(order)

        except Exception as e:
            logger.error(str(e))
            print("❌ Error:", e)

    def limit_order(self, symbol, side, quantity, price):
        try:
            validate_symbol(symbol)
            validate_quantity(quantity)
            validate_price(price)

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price,
                timestamp=self._server_timestamp(),  # ⭐ FIX
                recvWindow=20000
            )

            logger.info(order)
            print("✅ Limit order placed successfully")
            print(order)

        except Exception as e:
            logger.error(str(e))
            print("❌ Error:", e)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage:")
        print("Market: python bot.py BTCUSDT BUY MARKET 0.01")
        print("Limit : python bot.py BTCUSDT SELL LIMIT 0.01 65000")
        sys.exit(1)

    bot = BasicBot(API_KEY, API_SECRET)

    symbol = sys.argv[1]
    side = sys.argv[2]
    order_type = sys.argv[3]
    quantity = float(sys.argv[4])

    if order_type == "MARKET":
        bot.market_order(symbol, side, quantity)

    elif order_type == "LIMIT":
        price = float(sys.argv[5])
        bot.limit_order(symbol, side, quantity, price)

    else:
        print("Unsupported order type")
