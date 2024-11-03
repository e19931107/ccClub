def find(ttl_length):
    ttl_length = list(map(int, ttl_length.split(',')))
    total_length = sum(ttl_length)
    if total_length % 4 != 0:
        return False
    ttl_length.sort(reverse=True)
    side_lengths = [0] * 4
    return dfs(ttl_length, side_lengths, 0, total_length // 4)

def dfs(ttl_length, side_lengths, index, target):
    if index == len(ttl_length):
        return all(side == target for side in side_lengths)

    current_length = ttl_length[index]

    for i in range(4):
        if side_lengths[i] + current_length <= target:
            side_lengths[i] += current_length
            if dfs(ttl_length, side_lengths, index + 1, target):
                return True
            side_lengths[i] -= current_length

    return False

# 讀取輸入
ttl_length = input()

# 輸出結果
print(find(ttl_length))
