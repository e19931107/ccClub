x = int(input())

lst = []
while len(lst) <= 3:
    if x%2 == 1:
        x = 3*x + 1
        lst.append(int(x))
        if x == 1:
            break
    elif x%2 == 0:
        x = x/2
        lst.append(int(x))
        if x == 1:
            break

print(','.join(str(i) for i in lst))