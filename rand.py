from random import randrange


def random(first: int = 0, last: int = 999) -> int:
    rand: int = randrange(first, last, step=1)
    return rand
