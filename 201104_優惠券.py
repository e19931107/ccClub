import math
d = {}
i = 0

while i < 5:
    x = input().split()
    d[i] = x
    i += 1

budget = int(input())

for i, j in d.items():
    if len(j) == 2:
        budget -= int(j[1])
    elif len(j) == 1:
        budget = budget*(int(j[0])/10)

if math.floor(budget) < 0:
    print(0)
else:
    print(math.floor(budget))