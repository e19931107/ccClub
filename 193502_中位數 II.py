x = [int(i) for i in input().split(' ')]
x.sort()

if len(x)%2 == 1:
    print(float(x[int((len(x)/2)-0.5)]))
elif len(x)%2 == 0:
    print(((x[int((len(x)/2)+0.5)])+(x[int((len(x)/2)-0.5)]))/2)
else:
    print(0)