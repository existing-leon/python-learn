import concurrent.futures


# 定义一个任务函数
def square(x):
    return x * x


if __name__ == '__main__':
    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务
        results = [executor.submit(square, i) for i in range(5)]

        # 获取任务结果
        for future in concurrent.futures.as_completed(results):
            print(future.result())

'''
代码解释：
ThreadPoolExecutor(max_workers=3)：创建一个包含 3 个线程的线程池。
executor.submit(square, i)：向线程池提交任务，返回一个Future对象。
future.result()：获取任务的结果。
通过以上介绍，你可以了解 Python 多线程的基本使用方法、线程同步和线程池的使用。在实际应用中，需要根据具体情况选择合适的并发方式。
'''
