x = [i for i in input().split(',')]
y = list(dict.fromkeys(x))

d = {}
for i in y:
    d[i] = x.count(i)

lst = []
for i, j in d.items():
    if j == 1:
        lst.append(i)

print(','.join(i for i in lst))