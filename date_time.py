import datetime

dt1 = datetime.datetime(2023, 10, 12)
dt2 = datetime.datetime(2023, 10, 10)

delta = datetime.timedelta(days = 730)

print((dt1-dt2).total_seconds())

print(dt1+delta)