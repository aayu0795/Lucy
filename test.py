import time
from datetime import datetime


now = datetime.now()
date = now.strftime('%d_%m_%y_')
time = time.strftime('%H_%M')
print(('{}{}').format(date, time))