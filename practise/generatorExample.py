import random
from contextlib import redirect_stdout
import time

class generatorexample(object):
    def __init__(self,fileName):
        self.fileName = fileName
        
    def dataGeneration(self):
        '''
        Creation of log files similar to server log files.
        1. ttms = Is the time taken in seconds for the response from the server
        2. chi = Ip address of the client hostname
        3. crc = hit/miss
        FOR FURTHER REFERENCES USE THE LINK BELOW:
        https://docs.trafficserver.apache.org/en/6.2.x/admin-guide/monitoring/
        logging/log-formats.en.html
        
        steps to generate log files and to write into a file:
        1. create a random values for all the three fields. random is a module in python.
        Please do check the module.
        2. Write it in a file line by line.
        
        Tasks:
        redirect_Stdout is the module for writing lines into files instead of printing on terminal.(WILL explain in next class')
        Add some more fields and try the code. 
        '''
       
        Ip = ['10.10.10.10','10.10.10.11','10.10.10.12','10.10.10.13']
        ttms,phi,crc=[],[],[]
        
        with open(self.fileName,'a') as f:
            with redirect_stdout(f):
                for i in  range(100):
                    ttms = (random.randint(1,10))
                    phi = (random.choice(Ip))
                    crc = (random.choice(['hit','miss']))
                    print('ttms = {},phi = {},crc = {}'.format(ttms,phi,crc))
            
    
    
    def FollowFile(self,f):
        '''
        It is a generator written to yield the fields from the text file
        1. open the file 
        2. read the file
        3. yield the lines in the file
        4. break if no lines in file
        '''
        
        while True:
            for line in f.readlines():
                yield line
            else:
                break
                
            
    
        
        
    def readLines(self):
        '''
        This function is written to read the lines from the follow function and do the processing
        1. call the follow function
        2. Process the data
        '''
        time.sleep(5)
        with open(self.fileName,'r') as f:
            for line in self.FollowFile(f):
                print(line)
 
 
if __name__ == '__main__':
    # this is the entry point from where the code is going to get excecuted           
    obj = generatorexample('test.txt')
    obj.dataGeneration()
    obj.readLines()
            
        