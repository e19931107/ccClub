x = [int(x) for x in input().split(' ')]
a = x[0]
b = x[1]

import math
if a >= 0 and b >= 0:
    print(math.floor(b**(0.5))-math.ceil(a**(0.5))+1)
elif b >= 0:
    print(math.floor(b**(0.5))+1)
else:
    print(0)
    