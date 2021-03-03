import random
from random import choice

a = input().split()
k, m = list(map(int, input().split()))
d, c = list(map(float, input().split()))
n = int(input())
bilo = []

for i in range(n):
    fuel = choice(a)
    a.remove(fuel)
    d = True
    intensy = random.randrange(k, m)
    while d:
        b = random.uniform(d, c)
        if b not in bilo:
            bilo.append(b)
            d = False
    cost = round(intensy * b,1)
    print(f'Lamp {i + 1}: works on {fuel}, light intensity {intensy} cd, volume {str(b)[:3]} l, cost {cost} coins.')
