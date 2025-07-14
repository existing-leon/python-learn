import asyncio


# 定义一个协程函数
async def hello():
    print('hello')
    # 模拟一个异步操作, 暂停当前协程
    await asyncio.sleep(1)
    print('world')


if __name__ == '__main__':
    # 创建事件循环
    loop = asyncio.get_event_loop()
    # 运行协程
    loop.run_until_complete(hello())
    # 关闭事件循环
    loop.close()

'''
代码解释：
async def：用于定义一个协程函数，协程函数在调用时不会立即执行，而是返回一个协程对象。
await：用于暂停当前协程的执行，等待一个可等待对象（如另一个协程或asyncio.Future对象）完成。
asyncio.get_event_loop()：获取当前线程的事件循环，事件循环负责调度和执行协程。
loop.run_until_complete()：运行协程直到完成。
loop.close()：关闭事件循环。
'''
