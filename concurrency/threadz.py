from threading import Thread
import time


# code to execute in an independent thread
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# create a launch a thread
t = Thread(target=countdown, args=(10,))
t.start()
