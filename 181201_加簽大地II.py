id_list = input().split()
list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12 = [], [], [], [], [], [], [], [], [], [], [], []
#優先順序為：台大資訊學群 (aXX902XXX) > 台大電機學群 (aXX901XXX) > 台大其他系所 (aXXXXXXXX)
#在同一個優先順位內，大四的學生優先於其他年級的學生
#在這裡我們規定為學號開頭為 "a04" 的學生（a04303XXX 優先於 a05303XXX 以及 a03303XXX）
#除此之外，接續規則 2 的優先順序
#如果在同個優先順位之內，該同學的學號末三碼是 3, 5, 7 其中一個數字的倍數，將優先於其他同學進行加簽
#(a05502018 優先於 a05705019)

# 1. 台大資訊＋大四＋3,5,7倍數
# 2. 台大資訊＋大四
# 3. 台大資訊＋3,5,7倍數
# 4. 台大資訊
# 5. 台大電機＋大四＋3,5,7倍數
# 6. 台大電機＋大四
# 7. 台大電機＋3,5,7倍數
# 8. 台大電機
# 9. 台大＋大四＋3,5,7倍數
# 10.台大＋大四
# 11.台大＋3,5,7倍數
# 12.台大

for id in id_list:
    last = int(id[6:9])
    # 901
    if id[3:6] == '902' and id[0:3] == 'a04' and ((last%3) == 0 or (last%5) == 0 or (last%7) == 0):
        list1.append(id)
        continue
    
    elif id[3:6] == '902' and id[0:3] == 'a04':
        list2.append(id)
        continue

    elif id[0:1] == 'a' and id[3:6] == '902' and ((last%3) == 0 or (last%5) == 0 or (last%7) == 0):
        list3.append(id)
        continue
    
    elif id[0:1] == 'a' and id[3:6] == '902':
        list4.append(id)
        continue

    # 902
    if id[3:6] == '901' and id[0:3] == 'a04' and ((last%3) == 0 or (last%5) == 0 or (last%7) == 0):
        list5.append(id)
        continue
    
    elif id[3:6] == '901' and id[0:3] == 'a04':
        list6.append(id)
        continue

    elif id[0:1] == 'a' and id[3:6] == '901' and ((last%3) == 0 or (last%5) == 0 or (last%7) == 0):
        list7.append(id)
        continue

    elif id[0:1] == 'a' and id[3:6] == '901':
        list8.append(id)
        continue

    # other
    if id[0:3] == 'a04' and ((last%3) == 0 or (last%5) == 0 or (last%7) == 0):
        list9.append(id)
        continue
    
    elif id[0:3] == 'a04':
        list10.append(id)
        continue

    elif id[0:1] == 'a' and ((last%3) == 0 or (last%5) == 0 or (last%7) == 0):
        list11.append(id)
        continue

    elif True:
        list12.append(id)
        continue

print('\n'.join(str(i) for i in list1+list2+list3+list4+list5+list6+list7+list8+list9+list10+list11+list12))