import random


def guess(limit):
    random_num = random.randint(1, limit)
    guess = 0
    while guess != random_num:
        limit