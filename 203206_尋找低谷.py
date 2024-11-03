lst1 = [int(x) for x in input().split(' ')]
lst2 = sorted(lst1)

first = lst1.index(lst2[0])
second = lst1.index(lst2[1])
third = lst1.index(lst2[2])

if 0 < lst1.index(lst2[0]) < len(lst1)-1:
    print(first)
elif lst1.index(lst2[0]) == 0 or lst1.index(lst2[0]) == len(lst1)-1:
    print(second)
else:
    print(third)
