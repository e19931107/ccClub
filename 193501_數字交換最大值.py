from collections import defaultdict
original_lst = [int(i) for i in input()]

d = defaultdict(list)
for i in range(len(original_lst)):
    # print(i, original_lst[i])
    d[i] = original_lst[i]

d_dict = defaultdict(list)
n = 0
while n < 10:
    for i, j in d.items():
        if j == n:
            d_dict[j].append(i)
    n += 1
print(dict(d_dict))

# 從左邊數來，遇到低谷就停，就是斜坡的那個數字
# 從右邊數來，遇到尖峰就停，就是最高的那個數字要交換