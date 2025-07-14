def validate_input_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("输入参数必须为整数")
        for value in kwargs.values():
            if not isinstance(value, int):
                raise ValueError("输入参数必须为整数")
        return func(*args, **kwargs)

    return wrapper


@validate_input_decorator
def multiply(a, b):
    return a * b


# 调用被装饰的函数
try:
    result = multiply(3, 5)
    print(result)
    multiply(3, "5")  # 会抛出 ValueError 异常
except ValueError as e:
    print(e)
