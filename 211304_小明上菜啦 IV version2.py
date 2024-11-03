x = [int(i) for i in input().split(',')]
x.sort(reverse = True)
avg = sum(x)//4
side1, side2, side3, side4 = [], [], [], []

n = 0
while sum(x)%4 == 0:
    if len(side1) == 0:
        side1.append(x[n])
        x.pop(x[n])
        if x[n+1] + sum(side1) <= avg:
            side1.append(i)
            x.pop(x[n+1])
        continue

    if len(side2) == 0:
        side2.append(x[0])