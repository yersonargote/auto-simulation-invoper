from random import randrange
from typing import Optional

from fill import fill
from tables import AMOUNT, SALES


def random(first: int = 0, last: int = 999) -> int:
    rand: int = randrange(first, last, step=1)
    return rand


def show(table: dict):
    print('--------------------------------')
    for key, value in table.items():
        print(f'{key}')
        for i in value:
            print('    ', end="")
            print(i)
    print('--------------------------------')


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


def main():
    amounts = fill(AMOUNT)
    sales = fill(SALES)

    table: dict = {}
    sell_price: dict = {}
    amount_sould: dict = {}
    table["sell_price"] = sell_price
    table["amount_sould"] = amount_sould

    price, rand1 = define_price(sales)
    q, rand2 = define_q(amounts)

    print(price, rand1)
    print(q, rand2)


if __name__ == "__main__":
    main()
