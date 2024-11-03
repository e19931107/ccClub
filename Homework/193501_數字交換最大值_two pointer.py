from collections import defaultdict
x = [int(i) for i in input()]

#左到右的順序，找到下一位[n+1]比這一位數[n]還要大的數字和他的位置
m = True
left = x
for i in range(0,len(left)-1):
    if left[i] < left[i+1]:
        m = False
        min_position = i
        min_value = left[i]
        break
if m == True:
    min_position = len(left)
    min_value = left[len(left)-1]

stop = i

#然後從右到左，找到這一位比下一位數字還要大的
n = True
right = x[stop:]

for i in range(1,len(right)-1):
    if right[-i] > right[-i-1]:
        n = False
        max_position = -i
        max_value = right[-i]
        break
if n == True:
    max_position =  -1
    max_value = right[-1]
    
#從左到右的順序，找到比max_value小的值及可進行交換
temp = []
if min_value == max_value:
    print(''.join(str(i) for i in x))
else:
    for j in range(0,min_position+1):
        if x[j] < max_value:
            break
    minpositionneedtobereplaced = j
    minvalueneedtobereplaced = x[j]

    for j in range(1,len(x)):
        if x[-j] >= x[-j-1]:
            break
    maxpositionneedtobereplaced = len(x)-j
    maxvalueneedtobereplaced = x[-j]

    answer = {}
    for k in range(len(x)):
        answer[k] = x[k]
    answer[maxpositionneedtobereplaced] = minvalueneedtobereplaced
    answer[minpositionneedtobereplaced] = maxvalueneedtobereplaced
    print(''.join(str(i)for i in list(answer.values())))