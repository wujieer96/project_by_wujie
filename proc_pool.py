from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))
if __name__=='__main__':
    print('parent process %s.'% os.getpid())
    p=Pool(4)   #同时执行4个进程,数字是Pool有意设计的限制，并不是操作系统的限制，Pool=5同时跑5个进程
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')
