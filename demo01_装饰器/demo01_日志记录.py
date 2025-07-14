import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        # 记录函数开始执行的日志
        logging.info(f"开始执行函数 {func.__name__}，参数: args={args}, kwargs={kwargs}")
        # 调用原函数
        result = func(*args, **kwargs)
        # 记录函数执行结束的日志
        logging.info(f"函数 {func.__name__} 执行结束，结果: {result}")
        return result

    return wrapper


@log_decorator
def add(a, b):
    return a + b


# 调用被装饰的函数
result = add(3, 5)
