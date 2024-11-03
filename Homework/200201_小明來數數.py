x = [int(i) for i in input().split()]
first, last, gap = x[0], x[1], x[2]

num = first
lst = []
while num < last:
    lst.append(num)
    num = num + gap

print(*lst)
print(sum(lst))