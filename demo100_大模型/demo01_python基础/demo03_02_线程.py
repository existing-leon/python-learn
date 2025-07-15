"""
线程：线程是处理器任务调度和执行的基本单元
    一个进程至少有一个线程, 也可以运行多个线程
    多个线程之间可共享数据
    线程运行出错异常后, 如果没有捕获, 会导致整个进程崩溃
    多线程是指在同一进程中同时执行多个任务
"""

# 两线程分别交替打印
import time
import threading


# 交替打印 00000 和 11111
def func():
    flag = 0
    while True:
        print(threading.current_thread().name, f'{flag}' * 5)
        flag = flag ^ 1
        time.sleep(0.5)


if __name__ == '__main__':
    t1 = threading.Thread(target=func, name='线程1')
    t2 = threading.Thread(target=func, name='线程2')
    t1.start()
    t2.start()
