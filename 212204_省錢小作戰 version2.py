import re

dicti = {'s':0, 'c':0 , 'p':0, 'm':0}
n = 0
while n < 4:
    store = input().split()
    new_store = []
    for items in store:
        try:
            new_store.append(int(items))
        except:
            discount = items.split(',')
            for items in discount:
                new_store.append(items)
    if n == 0:
        dicti['s'] = new_store
        n += 1
    elif n ==1:
        dicti['c'] = new_store
        n += 1
    elif n ==2:
        dicti['p'] = new_store
        n += 1
    elif n ==3:
        dicti['m'] = new_store
        n += 1
# print(dicti)
final_decision = {}
for key, value in dicti.items():
    quantity = 0
    price = 0
    credit = 0
    shipping = 0
    amount = 0
    discounts = []

    for item in value:
        if re.search('^[0-9]*$', str(item)):
            if quantity == 0:
                quantity = int(item)
            else:
                price = int(item)

        if re.search('運費', str(item)):
            shipping = int(item[2:])
            continue
        elif re.search('免運', str(item)):
            shopping = 0
            continue

        if re.search('[0-9]%', str(item)):
            credit = float(item[0:len(item)-1])
            continue
        
        if re.search(r'滿(\d+)打(\d+)折', str(item)):
            match = re.search(r'滿(\d+)打(\d+)折', str(item))
            amount = match.group(1)
            discount = match.group(2)
            if len(discount) == 1:
                discount = float(discount)/10
            else:
                discount = float(discount)/100
            discounts.append([int(amount), discount])
    
    # print('-'*20)
    # print(key)
    # print(f'貨量:{quantity}')
    # print(f'價格:{price}')
    # print(f'信用卡:{credit}')
    # print(f'運費:{shipping}')
    # discounts = sorted(discounts)
    # print(f'折價:{discounts}')

    if quantity == 0:
        continue
    
    if len(discounts) == 0:
        final_decision[key.upper()+'商店'] = ((price+shopping)+shipping)*(100-credit)/100
    
    else:
        temp = []
        for i in discounts:
            if i[0] < price:
                temp.append(((price*i[1]+shopping)+shipping)*(100-credit)/100)
            else:
                temp.append(((price+shopping)+shipping)*(100-credit)/100)
        temp.sort()
        final_decision[key.upper()+'商店'] = min(temp)

final_decision = sorted(final_decision.items(), key = lambda x:x[1])
print(final_decision[0][0], int(round(final_decision[0][1],0)), sep = ' ')