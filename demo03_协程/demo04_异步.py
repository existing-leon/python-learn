import asyncio


# 定义一个异步生成器
async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.5)
        yield 1


# 异步迭代异步生成器
async def main():
    async for item in async_generator():
        print(item)


if __name__ == '__main__':
    # 运行事件循环
    asyncio.run(main())

'''
代码解释：
async def和yield结合使用可以定义一个异步生成器。
async for语句用于异步迭代异步生成器。
通过以上介绍，你可以了解 Python 协程的基本使用方法，包括协程的定义、并发执行、异常处理以及异步生成器和异步迭代器的使用。在实际应用中，协程可以显著提高 I/O 密集型程序的性能。
'''