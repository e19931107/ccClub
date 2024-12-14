lst = []
while True:
    try:
        x = input()
        lst.append(x)
    except:
        break

print(''.join(str(i) for i in lst))