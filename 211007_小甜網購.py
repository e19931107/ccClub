from datetime import timezone, datetime,timedelta
import pytz

time1 = input()
time2 = input()
time3 = input()
print(time1)
print(time2)
print(datetime.fromtimestamp(float(time3),timezone.utc))
time4 = datetime.fromtimestamp(float(time3),timezone.utc)
print(time4+timedelta(hours = 8))
