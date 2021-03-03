import random
from random import choice


n = int(input())
a = input().split()
minimal = int(input())
d, c = list(map(float, input().split()))

bilo = []

for i in range(n):
    type = choice(a)
    a.remove(type)
    d = True
    distance = round(random.uniform(d, c), 1)
    while d:
        b = random.randrange(minimal, 300, 10)
        if b not in bilo:
            bilo.append(b)
            d = False
    amount = round(b / distance * 10, 2)
    print(f'{type} plate size {distance}, through {b} sm fork, fits the {amount} of food.')
