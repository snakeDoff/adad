import random
from random import choice


a = input().split()
d, c = list(map(int, input().split()))
k, n = list(map(float, input().split()))
bilo = []
for i in range(3):
    aa = True
    while aa:
        ds = choice(a)
        if ds not in bilo:
            bilo.append(ds)
            aa = False

v1 = random.randrange(d, c)
v2 = random.randrange(d, c)
v3 = random.randrange(d, c)
w1 = round(random.uniform(k, n), 1)
w2 = round(random.uniform(k, n), 1)
w3 = round(random.uniform(k, n), 1)
tw1 = round(v1 * w1, 1)
tw2 = round(v2 * w2, 1)
tw3 = round(v3 * w3, 1)
print(f'1. {bilo[0]} weighing {w1} kg, {v1} of pieces, {tw1} kg.')
print(f'2. {bilo[1]} weighing {w2} kg, {v2} of pieces, {tw2} kg.')
print(f'3. {bilo[2]} weighing {w3} kg, {v3} of pieces, {tw3} kg.')
