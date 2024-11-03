from datetime import datetime, timedelta

day1 = [int(i) for i in input().split(' ')]
day2 = [int(i) for i in input().split(' ')]

day1_m = datetime(day1[0], day1[1], day1[2]).date()
day2_m = datetime(day2[0], day2[1], day2[2]).date()

print(abs((day1_m-day2_m).days))
