def one(x):
    x.sort(reverse = True)
    return x

def zero(x):
    x.sort(reverse = False)
    return x

n = input()
x = [int(i) for i in input().split()]

if n == '1':
    print(' '.join(str(i) for i in one(x)))
else:
    print(' '.join(str(i) for i in zero(x)))