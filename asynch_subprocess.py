"""
this is a document for asyncio's subprocesses

"""

import asyncio
import sys

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    print(f"proc.pid is {proc.pid}")
    print(f"proc.stdout is {proc.stdout}")
    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


async def get_date():
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    return line


async def main():
    results = await asyncio.gather(
        run('ls'),
        run('sleep 1; echo "hello"'),
        get_date())
    print(f"results are : {results}")
    print(f"Current date : {results[2]}")

asyncio.run(main())