import json
from random import randrange
from typing import Optional

from fill import fill
from tables import AMOUNT, SALES


def random(first: int = 0, last: int = 999) -> int:
    rand: int = randrange(first, last, step=1)
    return rand


def show(table: dict):
    print(json.dumps(table, indent=4))


def define_price(sales: dict) -> Optional[tuple]:
    rand: int = random()

    for idx, limit in enumerate(sales["assigned"]):
        if rand < limit[1]:
            price = sales["price"][idx]
            return price, rand


def define_q(amounts: dict) -> Optional[tuple]:
    rand: int = random()

    for idx, limit in enumerate(amounts["assigned"]):
        if rand < limit[1]:
            LI, LS = amounts["range"][idx]
            li, ls = limit[0], limit[1]
            Q = LI + ((rand - li)/(ls - li)) * (LS - LI)
            return round(Q), rand


def utility(price: float, amount: int):
    return price * amount - 0.3 * amount - 0.15

# print(f'Random: {rand1}')
# print(f'Price: {price}')
# print(f'Random: {rand2}')
# print(f'Quantity: {q}')
# print(f'Utility: {utlty}')


def main():
    amounts = fill(AMOUNT)
    sales = fill(SALES)

    simulatios: int = 25

    random1: list = []
    random2: list = []
    prices: list = []
    quantity: list = []
    utilities: list = []

    for _ in range(simulatios):
        price, rand1 = define_price(sales)
        q, rand2 = define_q(amounts)

        utlty = utility(price, q)

        random1.append(rand1)
        prices.append(price)
        random2.append(rand2)
        quantity.append(q)
        utilities.append(utlty)

    table: dict = {}
    sell_price: dict = {}
    amount_sould: dict = {}

    sell_price["random"] = random1
    sell_price["price"] = prices

    amount_sould["random"] = random2
    amount_sould["amount"] = quantity

    table["sell_price"] = sell_price
    table["amount_sould"] = amount_sould
    table["utilities"] = utilities

    show(table)


if __name__ == "__main__":
    main()
