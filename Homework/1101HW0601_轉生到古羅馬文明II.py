lst = {'I': 1,
       'V': 5,
       'X': 10,
       'L': 50,
       'C': 100,
       'D': 500,
       'M': 1000
       }

n = [*input()]
m = len(n)//2
loop = 0
number = 0

while loop < m:
    try:
        for i in range(m):
            if lst.get(n[i*2]) == lst.get(n[i*2+1]):
                print(lst.get(n[i*2]))
                print(lst.get(n[i*2+1]))
                number += lst.get(n[i*2])*2
            elif lst.get(n[i*2]) <= lst.get(n[i*2+1]):
                print(lst.get(n[i*2]))
                print(lst.get(n[i*2+1]))
                number += lst.get(n[i*2]) + lst.get(n[i*2+1])
            else:
                print(lst.get(n[i*2]))
                print(lst.get(n[i*2+1]))
                number = number + (lst.get(n[i*2]) - lst.get(n[i*2+1]))
        loop += 1
    except:
        break

print(number)