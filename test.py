import winsound
import time
from datetime import datetime

now = datetime.now()

while True:
    print(time.strftime('%H:%M:%S'))
    time.sleep(1)