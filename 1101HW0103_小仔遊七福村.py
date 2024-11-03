import math
lst = []
while True:
    try:
        x = input()
        lst.append(x)
    except:
        break

price = 0
#一般人的基本票價是 699 元，新竹市民(身分證開頭字母為 O)基本票價為 599 元
for i in range(len(lst)):
    if lst[i][0] == 'O':
        price += 599
    else:
        price += 699

price_range = []
price_range.append(price)

price1 = price
#七福村有兩種的門票優惠活動，兩個活動不能重複使用
#solution 1
#三人行團體優惠，若三人同性別，總金額可打八折
#若三人不同出生地，總金額可打八折，兩者可同時使用，總金額無條件進位到整數位
if (lst[0][1] == lst[1][1]) and (lst[1][1] == lst[2][1]) and (lst[0][1] == lst[2][1]):
    price1 *= 0.8

if (lst[0][0] != lst[1][0]) and (lst[1][0] != lst[2][0])  and (lst[0][0] != lst[2][0]):
    price1 *=0.8

price1 = math.ceil(price1)
price_range.append(price1)

#solution 2
#好事七七，如果身分證字號中有每有一個 7 ，門票減 70 元
#身分證字號後三位如果是 7 的倍數，門票減 77 元，兩者可同時使用
seven = 0
price2 = price
for i in lst:
    seven = seven + i.count('7')

seventime = 0
for i in lst:
    if int(i[7:11])%7 == 0:
        seventime += 77

price2 = price2 - seven*70 - seventime
price_range.append(price2)

price_range.sort()
print(price_range[0])


