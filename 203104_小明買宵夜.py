item = input().split()
price = input().split()
price = [int(i) for i in price]
budget = int(input())

for i in range(len(item)):
    for j in range(len(item)):
        if (int(price[i])+int(price[j])) == budget:
            if i>j:
                print(item[j],item[i],sep = ' ')
                break
            else:
                print(item[i],item[j],sep = ' ')
                break
        break

#def
#one loop

#dictionary