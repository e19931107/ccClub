from collections import defaultdict
x = input().split()
x = [int(i) for i in x]
lst = []
for i, j in enumerate(x):
    lst.append((j,i))
lst.sort()

print(' '.join(str(k[1]) for k in lst))
