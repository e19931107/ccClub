d = {}
lst = []
for i in input().split(','):
    lst.append(int(i))
    lst.sort()

for key, value in enumerate(lst):
    d[key] = value

judger = [True]

if sum(list(d.values())) %4 != 0:
    judger.append(False)

def find(value):
    side = {}
    for i, j in d.items():
        try:
            if sum(side.values())+j <= sum(list(d.values()))/4:
                side[i]= j
        except:
            continue
        try:
            if sum(side.values())+d[int(len(d))-i-1] <= sum(list(d.values()))/4:
                side[int(len(d))-i-1]= d[int(len(d))-i-1]
        except:
            continue
        
    if sum(side.values()) == sum(list(d.values()))/4:
        judger.append(True)
    else:
        judger.append(False)
        return judger
    print(d)
    print(side)
    for i in side.keys():
        del d[i]
    print(d)
    return find(value)

find(value)

