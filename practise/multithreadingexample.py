from threading import Thread
import time

def threadexp():
    print('I am going to sleep')
    time.sleep(0.5)
    print(' i am back')
    
def threadexp1():
    print('i am running')
    
p=Thread(target=threadexp)
p1=Thread(target=threadexp1)
p.start()
p1.start()
    