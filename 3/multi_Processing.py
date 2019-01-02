import multiprocessing
from time import sleep,ctime

#定义说和写的方法
def talk(content,loop):
    for i in range(loop):
        print("start talk:%s%s"%(content,ctime()))
        sleep(2)
def write(content,loop):
    for i in range(loop):
        print("start writr:%s%s"%(content,ctime()))
        sleep(3)
#定义和加载线程
process=[]
t1=multiprocessing.Process(target=talk,args=("Hello 51zxw",2))
process.append(t1)
t2=multiprocessing.Process(target=write,args=("life is short",2))
process.append(t2)

#执行多线程
if __name__=='__main__':
    for t in process:
        t.start()
    for t in process:
        t.join()
    print("All process is ex %s"%ctime())
