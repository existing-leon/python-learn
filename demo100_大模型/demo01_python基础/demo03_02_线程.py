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

"""
# 交替打印 00000 和 11111
def func():
    flag = 0
    while True:
        print(threading.current_thread().name, f'{flag}' * 5)
        flag = flag ^ 1 # 替换0和1
        time.sleep(0.5)


if __name__ == '__main__':
    t1 = threading.Thread(target=func, name='线程1')
    t2 = threading.Thread(target=func, name='线程2')
    t1.start()
    t2.start()
"""

"""
# 自定义Thread子类创建线程
import time
import threading


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        flag = 0
        while True:
            print(f'\r{self.name}:{str(flag) * 5}', end='')
            flag = flag ^ 1  # 替换0和1
            time.sleep(0.5)


if __name__ == '__main__':
    t1 = Worker('线程1')
    t2 = Worker('线程2')
    t1.start()
    t2.start()
"""

"""
# 案例：3个线程, 每个线程都将字符串列表中的每个字符与1异或
import concurrent.futures


def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f'{tname}: {word}\n', end='')
    return word


if __name__ == '__main__':
    word = list('idmmn!vnsme')
    # 使用with语句来确保线程被迅速清理
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future1 = executor.submit(func, '线程1')
        future2 = executor.submit(func, '线程2')
        future3 = executor.submit(func, '线程3')
        word = future1.result()
        word = future2.result()
        word = future3.result()

    print(''.join(word))
"""

# 互斥锁
import time
import threading


def func():
    global g_num
    for _ in range(10):
        lock.acquire()  # 获取锁
        tmp = g_num + 1
        time.sleep(0.1)
        g_num = tmp  # 释放锁
        lock.release()
        print(f"{threading.current_thread().name}: {g_num}\n", end="")


if __name__ == '__main__':
    g_num = 0
    lock = threading.Lock()
    threads = [threading.Thread(target=func, name=f'线程{i}') for i in range(3)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(g_num)
