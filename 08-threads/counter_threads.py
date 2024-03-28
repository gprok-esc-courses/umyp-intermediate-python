import time
import random
from threading import Thread

def count(id):
    for i in range(10):
        msg = str(id) + ": " + str(i)
        print(msg)
        time.sleep(random.randint(1, 5))

threads = []
for t in range(5):
    th = Thread(target=count, args=(t,))
    threads.append(th)
    th.start()
for th in threads:
    th.join()
print("DONE")