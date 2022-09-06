"""
    Define file for define the prices and quantity amounts.
"""
from rand import random


def define_price(sales: dict) -> tuple:
    rand: int = random()
    price: float = float()

    for idx, limit in enumerate(sales["assigned"]):
        if rand < limit[1]:
            price = sales["price"][idx]
            break
    return price, rand


def define_q(amounts: dict) -> tuple:
    rand: int = random()
    Q: float = float()

    for idx, limit in enumerate(amounts["assigned"]):
        if rand < limit[1]:
            LI, LS = amounts["range"][idx]
            li, ls = limit[0], limit[1]
            Q = LI + ((rand - li)/(ls - li)) * (LS - LI)
            break
    return round(Q), rand
