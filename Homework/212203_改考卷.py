from collections import defaultdict
from decimal import Decimal
x = input().split()
test = {}
n = 0
for i in x:
    for j in i:
        test[n] = j
        n += 1
d_rate = {}
ppl = int(input())
for m in range(ppl):
    y = input().split()
    name = y[0]
    reply = y[1:]
    student = {}
    n = 0
    for k in reply:
        for l in k:
            student[n] = l
            n += 1
    # print(name, student, sep = ' ')
    score = 0
    lst = []
    for answer, reply in zip(test.values(),student.values()):
        if answer == reply:
            score += 100/len(test.values())
            lst.append(1/ppl)
        else:
            lst.append(0)
    d_rate[m] = lst
    print(name, int(score), sep = ' ')
# print(list(d_rate.values()))

check_rate = defaultdict(int)
for i in list(d_rate.values()):
    for j in range(len(i)):
        check_rate[j] += i[j]

final = [f'{float(Decimal(round(i*100,2)))}%' for i in list(check_rate.values())]
print(' '.join(str(i) for i in final))

# final = [f'{round(i*100,2)}%' for i in list(check_rate.values())]
# print(' '.join(str(i) for i in final))