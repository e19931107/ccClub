from datetime import datetime,timedelta
x = [int(i) for i in input().split(' ')]
delta = int(input())
print((datetime(x[0], x[1], x[2]) + timedelta(days = delta)).date())