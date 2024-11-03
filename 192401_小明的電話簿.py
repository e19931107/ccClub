tele = []
name = []
search = []

while True:
    x = input().split()
    if x[0] == 'a':
        tele.append(x[2])
        name.append(x[1])
    elif x[0] == 's':
        search.append(x[1])
    else:
        break

    for i in range(len(search)):
        if search[i] in tele:
            print(name[tele.index(search[i])])
        elif search[i] in name:
            print(tele[name.index(search[i])])
        else:
            print(f"Cannot find {search[i]}")

#dictionary