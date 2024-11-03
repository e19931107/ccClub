values = [int(i) for i in input().split(' ')]
keys = [str(j) for j in input().split(' ')]

d = {}
for key, value in zip(keys, values):
    if key not in d:
        d[key] = [value]
    elif key in d:
        d[key].append(value)
sorted_d = dict(sorted(d.items()))
# print(sorted_d)

count = []
for i in keys:
    count.append(keys.count(i))

final = []
l = 0
for k in range(max(count)):
    temp = []
    for value in sorted_d.values():
        try:
            temp.append(value[k])
        except:
            continue

    if l%2 == 0:
        l += 1
        final.append(temp)
        continue
    else:
        l += 1
        temp = [i for i in temp[::-1]]
        final.append(temp)

final_lst = []
for item in final:
    for i in item:
        final_lst.append(i)

print(' '.join(str(i)for i in final_lst))
