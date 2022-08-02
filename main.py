import json

from define import define_price, define_q
from fill import fill
from rand import random
from tables import AMOUNT, SALES

PRICE: int = 300000
SIMULATIONS: int = 25
LEFTOVER: int = 150000


def show(data):
    print(json.dumps(data, indent=4))


def utility(price: float, amount: int, order: int) -> float:
    excess: int = order - amount
    income: float = price * amount
    expenses: float = PRICE * order + LEFTOVER * excess
    utility: float = income - expenses
    return round(utility, 2)

# print(f'Random: {rand1}')
# print(f'Price: {price}')
# print(f'Random: {rand2}')
# print(f'Quantity: {q}')
# print(f'Utility: {utlty}')


def main():
    amounts = fill(AMOUNT)
    sales = fill(SALES)

    random1: list = []
    random2: list = []
    prices: list = []
    quantity: list = []
    utilities: list = []

    # Cantidad de producto ordenado
    order: int = random(100, 300)
    print(f'Orden: {order}')

    # Inversion total
    total: float = order * PRICE
    print(f'Total invertido: {total}')

    counter: int = 0
    # Cantidad minima de rentabilidad
    min_prof: float = total * 0.3
    print(f'Ganancia minima: {min_prof}')

    for _ in range(SIMULATIONS):
        price, rand1 = define_price(sales)
        q, rand2 = define_q(amounts)

        utlty = utility(price, q, order)
        if utlty > min_prof:
            counter += 1

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

    # show(table)

    prob: float = round((counter/SIMULATIONS)*100, 2)
    print(f"Rentabilidad mayor al 30% es del {prob}%")


if __name__ == "__main__":
    main()
