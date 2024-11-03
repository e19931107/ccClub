lst = input().split(' ')
cc = lst[0:int(len(lst)/2)]
yoyo = lst[int(len(lst)/2):]

new_arrange = []
for i,j in zip(cc, yoyo):
        new_arrange.append(i)
        new_arrange.append(j)

print(' '.join(str(i) for i in new_arrange))