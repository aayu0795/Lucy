import time

c10 =  int(time.time() + 10)
print('c10', c10)

while c10 != int(time.time()):
    time.sleep(1)
    print(time.time())