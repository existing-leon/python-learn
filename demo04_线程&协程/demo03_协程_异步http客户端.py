import asyncio
import aiohttp

'''
示例：一个简单的异步 HTTP 客户端，使用 Python 的asyncio和aiohttp库来同时发起多个 HTTP 请求。
在这个例子中，协程可以在等待一个 HTTP 请求响应的同时，去处理其他请求，避免了线程切换的开销，提高了并发处理能力。
'''


# 异步函数，用于发起 HTTP 请求
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


# 异步函数，用于并发执行多个请求
async def main():
    urls = [
        # 'https://www.example.com',
        # 'https://www.python.org',
        # 'https://www.github.com'
        'https://www.baidu.com',
        'https://www.bing.com',
        'https://www.sougou.com'
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(len(result))


# 运行异步程序
asyncio.run(main())
