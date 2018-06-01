from multiprocessing import Process
from threading import Thread
import random
from contextlib import redirect_stdout
import logging
import time


class generatorexample:
    def __init__(self):
        pass
        
        
    def dataGeneration(self,filename):
         
        IP=['11.192.16.2','12.11.176.1','10.123.15.5','1.134.56.7','12.145.1.15']
         
        with open(filename,'a') as f:
            with redirect_stdout(f):
                for i in range(10000):
                    ttms=(random.randint(5,12))
                    crc=(random.choice(IP))
                    phi=(random.choice(['hit','miss']))
                    psql=(random.randint(10,25))
                    print('ttms {},crc {},phi {},psql {}'.format(ttms,crc,phi,psql))
                    
                    
                    
obj= generatorexample()
# for i in range(2):
#     p=Thread(target=obj.dataGeneration)
#     p.start()
#obj.dataGeneration() 

if __name__ == '__main__' :
    p = Process(target=obj.dataGeneration,args=('test1.txt',))
    p1 = Process(target=obj.dataGeneration,args=('test2.txt',))
    time.sleep(5)
    p.start()
    p1.start()             
                    
                                      
            
        
    
 