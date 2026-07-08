import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)
    price = validate_price(args.price, order_type)

    print("\nOrder Summary")
    print("----------------")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {side}")
    print(f"Type     : {order_type}")
    print(f"Quantity : {quantity}")

    if price:
        print(f"Price    : {price}")

    client = BinanceClient().get_client()

    manager = OrderManager(client)

    response = manager.place_order(
        args.symbol,
        side,
        order_type,
        quantity,
        price
    )

    print("\nOrder Successful\n")

    print("Order ID :", response.get("orderId"))
    print("Status   :", response.get("status"))
    print("Executed :", response.get("executedQty"))
    print("Avg Price:", response.get("avgPrice"))

except Exception as e:

    print("\nOrder Failed")
    print(e)
