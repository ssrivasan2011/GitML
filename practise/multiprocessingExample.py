from multiprocessing import Process

def worker(num):
    print('worker %d'%(num))
    
if __name__ == '__main__':
    for i in range(2):
        p = Process(target = worker,args=(i,))
        p.start()