default = [int(x) for x in input().split(' ')]

x = default[0]
y = default[1]
r = default[2]
d = default[3]

n = 0
dicti = {}
while n < y+1:
    pig = [int(x) for x in input().split(' ')]
    dicti[y-n] = pig
    n += 1

# print(dicti)

count_mom = 0
for mom in dicti.values():
    for count in mom:
        if count == 0:
            count_mom += 1

sum_mini = 0
for mini in dicti.values():
    sum_mini += sum(mini)

print(count_mom, sum_mini, sep = ',')

lst = []
for key, value in dicti.items():
    for pign in range(len(value)):
        lst.append([value[pign], [pign, key]])
print(lst)

# print('-'*30)

mom_position = []
new_lst = []
for animal in lst:
    if animal[0] == 0:
        mom_position.append(animal)
    else:
        new_lst.append(animal)

# print(new_lst)
# print(mom_position)

minpig_num = 0
for mom in mom_position:
    mom_x = mom[1][0]
    mom_y = mom[1][1]
    for minipig in new_lst:
        # print(minipig[1])
        minipig_x = minipig[1][0]
        minipig_y = minipig[1][1]
        if r >= ((minipig_x - mom_x)**(2)+(minipig_y - mom_y)**(2))**(0.5):
            minpig_num += minipig[0]

# print(minpig_num)

if (minpig_num/sum_mini)*100 > d:
    print(0)
else:
    print(1)