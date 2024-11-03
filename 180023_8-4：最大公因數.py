import math

math1 = [int(i) for i in input().split()]
math2 = [int(i) for i in input().split()]

lst = []
for i in math1:
    for j in math2:
        lst.append(math.gcd(i,j))
        math2.pop(0)
        break

print(lst)
