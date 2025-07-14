import threading

# 共享资源
counter = 0

# 创建一个锁对象
lock = threading.Lock()


# 定义一个线程要执行的任务
def increment():
    global counter
    for _ in range(100000):
        # 获取锁
        lock.acquire()
        try:
            counter += 1
        finally:
            # 释放锁
            lock.release()


if __name__ == '__main__':
    # 创建线程对象
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=increment)

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待线程执行完成
    thread1.join()
    thread2.join()

    print(f'Final counter value: {counter}')

'''
代码解释：
lock.acquire()：获取锁，如果锁已经被其他线程占用，则当前线程会阻塞，直到锁被释放。
lock.release()：释放锁，允许其他线程获取锁。
'''
