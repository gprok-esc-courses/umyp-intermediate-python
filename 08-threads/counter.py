import time
import random

def count(id):
    for i in range(10):
        print(id, ":", i)
        time.sleep(random.randint(1, 5))

for t in range(5):
    count(t)