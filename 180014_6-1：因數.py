x = int(input())

answer = []
for i in range(x):
    if x%(i+1) == 0:
        answer.append(i+1)

print('\n'.join(str(i) for i in answer))