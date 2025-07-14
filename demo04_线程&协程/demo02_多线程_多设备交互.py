import threading
import time

'''
示例：
一个机器人控制系统，需要同时控制多个电机。每个电机的控制操作可能需要一定的时间来完成，
并且可能会因为电机的状态不同而产生不同的响应时间。可以使用多线程来分别控制每个电机，避免一个电机的操作阻塞其他电机的控制。
'''


# 模拟电机控制函数
def control_motor(motor_id):
    print(f"Starting control of motor {motor_id}")
    # 模拟电机控制操作，可能会阻塞一段时间
    time.sleep(2)
    print(f"Motor {motor_id} control completed")


# 电机数量
num_motors = 3
threads = []

# 创建并启动线程来控制每个电机
for i in range(num_motors):
    thread = threading.Thread(target=control_motor, args=(i,))
    threads.append(thread)
    thread.start()

# 等待所有线程执行完毕
for thread in threads:
    thread.join()

print("All motors are controlled.")
