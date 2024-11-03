n = int(input()) #N 層的積木塔
k = 1

#大寫：chr(i+65)
#小寫：chr(i+97)
num = 0
lst = []
upper = []
x = 0

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