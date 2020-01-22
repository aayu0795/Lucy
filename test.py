import winsound
import time
from datetime import datetime


now = datetime.now()
h = int(now.strftime('%H'))
m = int(now.strftime('%M'))
print(m)
if h == 12 or h == 0:
    time = ('12:{}'.format(str(m)))
elif h > 12:
    time = ('{}:{}'.format(h-12, m))
else:
    time = ('{}:{}'.format(h, m))

print(time)
print('Date')
date = now.strftime("%A %d. %B %Y")
print(date)