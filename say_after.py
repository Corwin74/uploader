import asyncio
import time


async def archive():
    proc = await asyncio.create_subprocess_exec("echo", "Hello World!", stdout=asyncio.subprocess.PIPE)
    while True:
        if proc.stdout.at_eof():
            break
        data = await proc.stdout.read(1)
        print(f'Received: {data.decode()!r}')
        print('\n')


async def main():

    await archive()

asyncio.run(main())
