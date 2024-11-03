x = int(input())

lst = [0, 1]
if x == 0:
    print([0])
elif x == 1:
    print(lst)
else:
    while len(lst) <= x+1:
        n = lst[-1]+lst[-2]
        lst.append(n)
    print(lst[:len(lst)-1])


# n = int(input())  # 讀入 n

# # 若 n 為 0，則直接輸出 [0]
# if n == 0:
#     print([0])
#     exit()

# # 初始化費氏數列的前兩個值
# fib = [0, 1]

# # 使用迴圈計算費氏數列的其他值
# for i in range(2, n+1):
#     fib.append(fib[i-1] + fib[i-2])

# print(fib)
