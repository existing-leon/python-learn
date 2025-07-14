import asyncio


# 定义一个协程函数, 可能会抛出异常
async def error_coroutine():
    try:
        await asyncio.sleep(1)
        raise ValueError('An error occurred')
    except ValueError as e:
        print(f'Caught an error: {e}')


if __name__ == '__main__':
    # 运行事件循环
    asyncio.run(error_coroutine())
