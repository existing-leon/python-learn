import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        # 记录开始时间
        start_time = time.time()
        # 调用原函数
        result = func(*args, **kwargs)
        # 记录结束时间
        end_time = time.time()
        # 计算执行时间
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时间: {execution_time} 秒")
        return result

    return wrapper


@timer_decorator
def heavy_computation():
    total = 0
    for i in range(1000000):
        total += i
    return total


# 调用被装饰的函数
result = heavy_computation()
