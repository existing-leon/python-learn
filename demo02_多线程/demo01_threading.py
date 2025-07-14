import threading
import time


# 定义一个线程要执行的任务
def print_numbers():
    for i in range(5):
        print(f' Thread 1: {i}')
        time.sleep(1)


# 定义另一个线程要执行的任务
def print_letters():
    for letter in 'abcde':
        print(f' Thread 2: {letter}')
        time.sleep(1)


if __name__ == '__main__':
    # 创建线程对象
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待线程执行完毕
    thread1.join()
    thread2.join()

    print("Main thread finished")

'''
代码解释：
threading.Thread(target=function)：创建一个线程对象，target参数指定线程要执行的函数。
start()：启动线程，使其开始执行任务。
join()：等待线程执行完毕，确保主线程在所有子线程执行完毕后再继续执行。
'''
