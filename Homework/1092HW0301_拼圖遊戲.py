lst = []
while True:
    try:
        lst = lst + [*input()]
    except:
        lst = lst[:-1]
        break

d = {}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] =  d[i] + 1
        
for i, j in d.items():
    print(i*j)
