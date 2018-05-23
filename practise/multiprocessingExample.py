from multiprocessing import Process
from multiprocessing import cpu_count
def worker(num):
    print(cpu_count())
    print('worker %d'%(num))
    
if __name__ == '__main__':
    for i in range(cpu_count()):
        p = Process(target = worker,args=(i,))
        p.start()