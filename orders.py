from bot.logging_config import logger


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):

        try:

            params = {
                "symbol": symbol.upper(),
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            logger.info(f"REQUEST : {params}")

            response = self.client.futures_create_order(**params)

            logger.info(f"RESPONSE : {response}")

            return response

        except Exception as e:

            logger.exception(e)
            raise
