from collections import defaultdict
x = input().split()

d = defaultdict(int)

for i in x:
    for j in i.lower():
        d[i] += ord(j)-96

d = dict(sorted(d.items(), key = lambda items:items[1]))
print(list(d.keys()))

