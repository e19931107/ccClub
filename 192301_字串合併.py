s1 = [*input()]
s2 = [*input()]

lst = []
for i, j in zip(s1,s2):
    lst.append(i)
    lst.append(j)

if len(s1) > len(s2):
    lst.extend(s1[-abs(len(s2)-len(s1)):])
    print(''.join(str(i) for i in lst))
elif len(s2) > len(s1):
    lst.extend(s2[-abs(len(s2)-len(s1)):])
    print(''.join(str(i) for i in lst))
else:
    print(''.join(str(i) for i in lst))