from decimal import Decimal
import math
x = [int(i) for i in input().split(' ')]
i = x[0]
x0 = x[1]
T = x[2]
L = x[3]

egg = 0
num = 0
for j in range(1,T+1):
    num = num + (1 + 0.5*j)
    if (x0-(num)) >= L:
        egg = egg + math.ceil(Decimal(i*(x0-(num))*0.01))
    elif (x0-(num)) < L:
        egg = egg + math.ceil(Decimal(i*L*0.01))

print(int(egg))