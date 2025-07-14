def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@cache_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# 调用被装饰的函数
print(factorial(5))
print(factorial(5))  # 第二次调用会直接从缓存中获取结果
