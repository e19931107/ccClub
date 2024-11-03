weapon_dict_num = int(input())

n = 1
weapon_dict = {}
while n <= int(weapon_dict_num):
    weapon = input().split()
    if len(weapon) == 2:
        weapon_dict[weapon[0]] = [int(weapon[1])]
    else:
        weapon_dict[weapon[0]] = [int(weapon[1])] + weapon[2:]
    n += 1

def find(x):
    temp = []
    if len(weapon_dict[x]) == 1:
        return int(weapon_dict[x][0])
    else:
        temp.append(weapon_dict[x][0])
        redeem_lst = weapon_dict[x][1:]
        for i in redeem_lst:
            temp.append(find(i))
        return sum(temp)

num_item = int(input())

m = 0
while m < num_item:
    x = input()
    print(find(x))
    m += 1
