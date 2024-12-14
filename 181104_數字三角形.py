n = int(input()) #N 層的積木塔
k = 1

num = 0
lst = []
number = []
z = 0

while num!=n:
    while num != n:
        z += len(number)
        number = []
        for c in range(k):
            number.append((c+z+1)%10)
        print(''.join(str(c) for c in number))
        num += 1
        break
    k += 1