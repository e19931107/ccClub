id1 = input()
id2 = input()

d = {id1: 0, id2: 0}

for i,j in d.items():
    if i[0] == 'a' and i[3:9] == 901:
        d[i] += 100
    elif i[0] == 'a' and i[3:9] == 902:
        d[i] += 70

    if i[0:3] == 'a04':
        d[i] += 10

    if int(i[6:9])%3 == 0 or int(i[6:9])%5 == 0 or int(i[6:9])%7 == 0:
        d[i] += 1

if list(d.values())[0] == list(d.values())[1]:
    print('tie')
elif list(d.values())[0] > list(d.values())[1]:
    print(list(d.keys())[0])
else:
    print(list(d.keys())[1])