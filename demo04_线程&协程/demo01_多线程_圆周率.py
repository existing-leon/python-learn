import threading
import random

'''
计算圆周率 π 的近似值。可以使用蒙特卡罗方法，通过随机投点来估算 π 的值。以下是一个使用多线程实现的示例代码：
'''


# 每个线程要执行的任务
def monte_carlo_pi(num_points, result_list, index):
    inside_circle = 0
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    result_list[index] = (inside_circle / num_points) * 4


# 线程数量
num_threads = 4
# 每个线程的投点数量
num_points_per_thread = 1000000

# 存储每个线程的计算结果
results = [0] * num_threads
threads = []

# 创建并启动线程
for i in range(num_threads):
    thread = threading.Thread(target=monte_carlo_pi, args=(num_points_per_thread, results, i))
    threads.append(thread)
    thread.start()

# 等待所有线程执行完毕
for thread in threads:
    thread.join()

# 计算最终结果
pi_approx = sum(results) / num_threads
print(f"Approximation of pi: {pi_approx}")
