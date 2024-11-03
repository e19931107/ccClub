n = int(input())

lst = []
while True:
    try:
        x = input().split(',')
        lst.append(x)

    except:
        break
lst.reverse()

for i in range(n):
    new_lst = []
    for j in range(n):
        x = lst[j][i]
        new_lst.append(x)
    print(','.join(str(i) for i in new_lst))