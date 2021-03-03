import random
from random import choice


n = int(input())
a = input().split()
b = input().split()
d, c = list(map(int, input().split(', ')))
bilo = []
bila = []

for i in range(n):
    d = True
    while d:
        first = choice(a)
        if first not in bilo:
            bilo.append(first)
            d = False
    d = True
    while d:
        second = choice(b)
        if second not in bila:
            bila.append(second)
            d = False
    size = random.randrange(d, c)
    value = round(random.uniform(0.1, 7.5), 2)
    usefulness = round(size ** 2 * value, 2)
    print(f'Sandwich {first} and {second}, {size} cm, thickness {value} cm, usefulness {usefulness}.')
