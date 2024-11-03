x = int(input())

step = 0

while x != 0:
    if x%2 == 1:
        step += 1
        x -= 1
    elif x%2 == 0:
        step += 1
        x = x/2
    else:
        step += 1
        x -= 1

print(step)