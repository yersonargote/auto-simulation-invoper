def accumulated(lst: list) -> list:
    accum: list = []
    cum: int = 0
    for i in lst:
        cum += i
        accum.append(round(cum, 2))
    return accum


def assigned_range(lst: list) -> list:
    assigned: list = []
    min: int = 0
    max: int = 0
    for i in lst:
        max = i * 1000
        assigned.append((round(min), round(max)))
        min = max
    return assigned


def fill(table: dict[str, list]) -> dict[str, list]:
    prob: list = table["prob"]
    accum: list = accumulated(prob)
    range: list = assigned_range(accum)
    table["accum"] = accum
    table["assigned"] = range
    return table
