import random
from random import choice

a = input().split(', ')
n = int(input())
d, c = list(map(int, input().split()))
maximal = float(input())

bilo = []

for i in range(n):
    name = choice(a)
    a.remove(name)
    number = random.randrange(d, c)
    value = round(random.uniform(0, maximal), 2)
    full_value = round(number * value, 2)
    print(f'{name} {number} of pieces, calorie content {value} kkal, total caloric {full_value}')
