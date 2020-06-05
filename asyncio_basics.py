# this is a simple code which read files asynchronously using asyncio.

import asyncio

async def read_text(file_name):
    print(f"Reading file: {file_name}")
    with open(file_name) as my_file:
        text = my_file.read()
        for i in range(len(text)):  # this is created to have delay as in actual server
            if i % 50 == 0:
                await asyncio.sleep(0.1)  
    print(f"Done reading: {file_name}")
    return text

async def main():  # coroutine
    file1 = loop.create_task(read_text('text1.txt'))
    file2 = loop.create_task(read_text('text2.txt'))
    file3 = loop.create_task(read_text('text3.txt'))
    file4 = loop.create_task(read_text('text4.txt'))
    await asyncio.wait([file1, file2, file3, file4])  # asynchronizing all the file


if __name__ == "__main__":
    loop = asyncio.get_event_loop()  # initializing our event loop
    loop.run_until_complete(main())
    loop.close()  
