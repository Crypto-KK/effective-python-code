from datetime import datetime, timezone, timedelta
from time import mktime

now = datetime.now()
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_utc)
print(now_local)
print('=' * 100)


time_str = '2019-06-01 11:11:11'
time_str = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
time_tuple = time_str.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)
print('=' * 100)


import pytz
'''任意时间地区转换'''
arrival_time = '2019-08-08 11:11:11'
datetime_native = datetime.strptime(arrival_time, '%Y-%m-%d %H:%M:%S')
china = pytz.timezone('Asia/Shanghai')
print(china.localize(datetime_native))
utc_dt = pytz.utc.normalize(china.localize(datetime_native).astimezone(pytz.utc))
print(utc_dt)

pacific = pytz.timezone('US/Pacific')
print(pacific.normalize(utc_dt.astimezone(pacific)))