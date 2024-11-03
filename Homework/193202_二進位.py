x = int(input())
original = x
lst = []
num = 0
while num < original:
    x = x//2
    lst.append(x%2)
    num += 1
print(lst)