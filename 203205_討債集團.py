name = input().split()
money = input().split()
d = {}

for i, j in zip(name, money):
    d[i] = int(j)

while True:
    try:
        name_again = input()
        print(d[name_again])
    except:
        break