dict = {}
i = 1

while True:
    x = input().split()
    sum_score = sum(int(i) for i in x)
    dict[i] = sum_score
    i += 1
    if dict[i-1] == 0:
        break

print(max(dict, key = dict.get),dict[max(dict, key = dict.get)],sep = ' ')