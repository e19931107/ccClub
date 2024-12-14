def judge(id):
    depart = id[3:6]
    if depart == '902':
        depart = 3
    elif depart == '901':
        depart = 2
    else:
        depart = 1

    grade = id[0:3]
    if grade == 'a04':
        grade = 2
    else:
        grade = 1

    num = int(id[6:9])
    if num%3 == 0 or num%5 == 0 or num%7 == 0:
        num = 1
    else:
        num = 0

    return (depart, grade, num)

id1 = input()
id2 = input()

id1_final = judge(id1)
id2_final = judge(id2)

if id1_final > id2_final:
    print(id1)
elif id1_final < id2_final:
    print(id2)
else:
    print('tie')