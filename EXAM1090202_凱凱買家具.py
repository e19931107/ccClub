#line 1
budget = int(input())

#line 2
desk_n = [str(i) for i in input().split()]
desk_p = [int(i) for i in input().split()]
desk = list(zip(desk_n, desk_p))

#line 4
chair_n = [str(i) for i in input().split()]
chair_p = [int(i) for i in input().split()]
chair = list(zip(chair_n, chair_p))

#line 6
cabinet_n = [str(i) for i in input().split()]
cabinet_p = [int(i) for i in input().split()]
cabinet = list(zip(cabinet_n, cabinet_p))

lst = {}
for i in range(len(desk)):
    for j in range(len(chair)):
        for k in range(len(cabinet)):
            if desk[i][1]+chair[j][1]+cabinet[k][1] <= budget:
                print(f"{desk[i][0]}/{chair[j][0]}/{cabinet[k][0]}:{desk[i][1]+chair[j][1]+cabinet[k][1]}")
            else:
                continue