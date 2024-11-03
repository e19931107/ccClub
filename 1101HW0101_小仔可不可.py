# blacktea coffaine 50mg sugar 10g
# milktea coffaine 20mg sugar 30g

#1 day coffaine < 300mg 3 days coffaine < 700mg
#1 day sugar < 60g 3 days < 150g

lst = []
while True:
    try:
        x = input()
        lst.append(x)
    except:
        break

dict = {}
for i in range(len(lst)):
    dict[i] = [lst[i][0],lst[i][1:]]

day = list(dict.keys())
item = list(dict.values())
drink = [item[i][0] for i in range(len(item))]
volumn = [item[i][1] for i in range(len(item))]

#先處理3天的咖啡因和糖
coffaine = 0
sugar = 0
three_day = True

for i in day:
    if drink[i] == 'B':
        coffaine += 50 * int(volumn[i])
        sugar += 10 * int(volumn[i])
    elif drink[i] == 'M':
        coffaine += 20 * int(volumn[i])
        sugar += 30 * int(volumn[i])
    
    if coffaine > 700 or sugar > 150:
        three_day = False
        break
    else: #coffaine < 700 or sugar < 150:
        continue

#再處理1天的咖啡因和糖
coffaine = 0
sugar = 0
one_day = True

for i in day:
    if drink[i] == 'B':
        coffaine = 50 * int(volumn[i])
        sugar = 10 * int(volumn[i])
    elif drink[i] == 'M':
        coffaine = 20 * int(volumn[i])
        sugar = 30 * int(volumn[i])
    
    if coffaine > 300 or sugar > 60:
        one_day = False
        break
    else: #coffaine < 300 or sugar < 60:
        continue

if one_day and three_day:
    print('可')
else:
    print('不可')
