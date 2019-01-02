import threading
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
threads=[]
t1=threading.Thread(target=talk,args=("Hello 51zxw",2))
threads.append(t1)


t2=threading.Thread(target=write,args=("life is short",2))
threads.append(t2)

#执行多线程
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All thread is ex")
