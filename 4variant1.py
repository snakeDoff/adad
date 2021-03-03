import random
from random import choice


n = int(input())
a = input().split('; ')
d, c = list(map(float, input().split()))
maximal = int(input())

bilo = []

for i in range(n):
    filling = choice(a)
    a.remove(filling)
    weight = round(random.uniform(d, c), 2)
    value = round(random.uniform(0, maximal), 2)
    d = True
    while d:
        value = round(random.randrange(1, maximal))
        if value not in bilo:
            bilo.append(value)
            d = False
    total = round(weight * value, 2)
    print(f'{filling} {weight} kg of the weight, quantity {value}, total weight {total}')
