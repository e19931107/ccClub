from collections import defaultdict
nums = input().split()
d = defaultdict(int)
for i in nums:
    d[i] += 1
[print(i) for i in d if d[i]%2 == 1]