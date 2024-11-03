n = int(input()) #N 層的積木塔
k = int(input()) #最上面那層的積木數量

#大寫：chr(i+65)
#小寫：chr(i+97)
num = 0
lst = []
upper = []
x = 0
lower = []
y = 0
number = []
z = 0

while num!=n:
    while num != n:
        x += len(upper)
        upper = []
        for a in range(k):
            upper.append(chr(((a+x)%26)+65))
        print(''.join(str(a) for a in upper))
        num += 1
        break
    k += 1
#----------------------------------------------------
    while num != n:
        y += len(lower)
        lower = []
        for b in range(k):
            lower.append(chr(((b+y)%26)+97))
        print(''.join(str(b) for b in lower))
        num += 1
        break
    k += 1
#----------------------------------------------------
    while num != n:
        z += len(number)
        number = []
        for c in range(k):
            number.append((c+z+1)%10)
        print(''.join(str(c) for c in number))
        num += 1
        break
    k += 1