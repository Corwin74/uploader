import asyncio
import sys


async def run_blocker():
    blocking_code = "import time; print('Hello', flush=True); time.sleep(10);\
        print('World!', flush=True)"
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', blocking_code, stdout=asyncio.subprocess.PIPE,
    )
    print('Ping')
    while True:
        if proc.stdout.at_eof():
            break
        data = await proc.stdout.read(5)
        print(data.decode())
    await proc.wait()
    print('Pong')
    return


asyncio.run(run_blocker())
