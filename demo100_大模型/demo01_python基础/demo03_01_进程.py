"""
并发：单个CPU处理多个任务, 各个任务交替执行一段之间
并行：多个CPU同时执行多个任务
"""

"""
进程：是操作系统中进行资源分配的基本单位
    操作系统中一个正在运行的程序或软件就是一个进程
    每个进程都有自己独立的一块内存空间
    一个进程崩溃后, 在保护模式下不会对其他进程产生影响
    多进程是指在操作系统中同时运行多个程序
"""

"""
# 同时读写文件
import time
import multiprocessing


# 向文件中写入数据
def write_file():
    with open('test.txt', 'a') as f:
        while True:
            f.write('hello world\n')
            f.flush()
            time.sleep(0.5)


# 从文件中读取数据
def read_file():
    with open('test.txt', 'r') as f:
        while True:
            time.sleep(0.1)
            print(f.read(1))


if __name__ == '__main__':
    # 创建一个子进程用于写文件
    p1 = multiprocessing.Process(target=write_file)
    # 创建一个子进程用于读文件
    p2 = multiprocessing.Process(target=read_file)
    # 启动子进程
    p1.start()
    # 启动子进程
    p2.start()
"""

"""
# 自定义 Process 子类创建进程
import os
import multiprocessing


class Worker(multiprocessing.Process):
    def run(self):
        print('进程id：', os.getpid(), '\t父进程id：', os.getppid())


if __name__ == '__main__':
    for i in range(5):
        p = Worker()
        p.start()
"""

"""
# 进程池
import os
import time
import multiprocessing


# 打印10个数字, 每次间隔0.5s
def func():
    for i in range(10):
        print(os.getpid(), i)
        time.sleep(0.5)


if __name__ == '__main__':
    # 指定进程池大小
    process_num = 5
    pool = multiprocessing.Pool(processes=process_num)
    for p in range(process_num):
        # 阻塞式
        # pool.apply(func)
        # 非阻塞式
        pool.apply_async(func)
    pool.close()
    pool.join()
    print('end')
"""

"""
# 进程间通信
import os
import multiprocessing


# 向list1 中添加10个元素
def func(list1):
    for i in range(10):
        list1.append(i)
        print(os.getpid(), list1)


if __name__ == '__main__':
    list1 = []
    p1 = multiprocessing.Process(target=func, args=(list1,))
    p2 = multiprocessing.Process(target=func, args=(list1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(os.getpid(), list1)
"""
