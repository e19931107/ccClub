num = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
alpha = {'I': 1, 
         'V': 5, 
         'X': 10, 
         'L': 50, 
         'C': 100, 
         'D': 500, 
         'M': 1000
         }

lst = []

n = int(input())
if n//1000 != 0:
    lst.append((n//1000)*'M')
    n = n-(n//1000)*1000

if n//500 != 0:
    lst.append((n//500*'D'))

print(lst)