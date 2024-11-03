x = input().split()
d = {}
for i in x:
    lst = [int(j) for j in[*i]]
    lst.sort(reverse = True)
    d[int(i)] = int(''.join(str(k)for k in lst))

d= dict(sorted(d.items(), key=lambda item: item[1]))
print([str(i)for i in d.keys()])
