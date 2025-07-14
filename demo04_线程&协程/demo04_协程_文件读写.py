import asyncio
import aiofiles

'''
示例：异步读取多个文件的内容。
在这个例子中，协程可以在等待一个文件读取完成的同时，去读取其他文件，充分利用了等待时间。
'''


# 异步函数，用于读取文件内容
async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
        return content


# 异步函数，用于并发读取多个文件
async def main():
    file_paths = ['./data/file1.txt', './data/file2.txt', './data/file3.txt']
    tasks = [read_file(file_path) for file_path in file_paths]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(len(result))


# 运行异步程序
asyncio.run(main())
