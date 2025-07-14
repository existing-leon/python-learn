# 模拟用户权限
user_permissions = ["admin"]
# user_permissions = ["sadmin"]


def permission_required(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if permission not in user_permissions:
                raise PermissionError("没有权限调用该函数")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@permission_required("admin")
def sensitive_operation():
    print("执行敏感操作")


# 调用被装饰的函数
try:
    sensitive_operation()
except PermissionError as e:
    print(e)
