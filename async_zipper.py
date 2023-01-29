import asyncio


async def run_zip():
    proc = await asyncio.create_subprocess_exec(
        'zip',
        '-r',
        '-',
        '/home/alex/dvmn/uploader/to_zip/',
        stdout=asyncio.subprocess.PIPE,
    )
    with open('archive.zip', 'wb') as f:
        counter = 0
        while True:
            if proc.stdout.at_eof():
                break
            data = await proc.stdout.read(1024*400)
            print(f'Iteration: {counter}')
            counter += 1
            f.write(data)
    await proc.wait()
    return


asyncio.run(run_zip())
