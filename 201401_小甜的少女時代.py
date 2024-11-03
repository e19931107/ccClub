n = int(input())
mylist = [int(x) for x in input().split()]
lst1 = []

for i in range(24-n+1):
    result = 1
    for j in mylist[i:i+n]:
        result = j * result
    

# lst2 = []
# for j in lst1:
#     result = 1
#     for k in j:
#         result = k * result
#     lst2.append(result)

# print(lst2.index(min(lst2)))