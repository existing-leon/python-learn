import asyncio


# 定义一个协程函数
async def print_numbers():
    for i in range(5):
        print(f'number: {i}')
        await asyncio.sleep(0.5)


# 定义另一个协程函数
async def print_letters():
    for letter in 'abcde':
        print(f'letter: {letter}')
        await asyncio.sleep(0.5)


# 创建事件循环
async def main():
    # 并发执行多个协程
    await asyncio.gather(print_numbers(), print_letters())


if __name__ == '__main__':
    # 创建事件循环
    asyncio.run(main())

'''
代码解释：
asyncio.gather()：并发运行多个可等待对象，并等待所有对象完成。
asyncio.run()：是 Python 3.7 及以上版本提供的一个便捷函数，用于创建事件循环并运行协程。
'''
