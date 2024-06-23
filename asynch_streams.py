"""
This is the document to learn asyncio Streams
Streams are high-level async/await-ready primitives to work with
network connections. Streams allow sending and receiving data 
without using callbacks or low-level protocols and transports.

"""

import asyncio
import urllib.parse
import sys
import socket


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


async def wait_for_data():
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()

    # Create a pair of connected sockets.
    rsock, wsock = socket.socketpair()
    print(f"rsock is {rsock.getsockname()} \n wsock is {wsock} ")

    # Register the open socket to wait for data.
    reader, writer = await asyncio.open_connection(sock=rsock)
    print(f" reading is {reader}, writer is {writer}")
    
    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'hello world from wait_for_data!'.encode())
    
    # Wait for data
    data = await reader.read(100)

    # Got data, we are done: close the socket
    print("Received:", data.decode())
    writer.close()
    await writer.wait_closed()

    # Close the second socket
    wsock.close()


async def main():
    # start a server on socket 127.0.0.1 with port 8888
    # the client should send message to this socket
    # example command line on client:
    # echo "foo" | nc localhost 1234
    # so server will revoke function handle_echo.
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

# this is for the test for asyncio.start_server
# asyncio.run(main())


# asyncio.run(wait_for_data())


async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80)

    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            print(f'HTTP header> {line}')

    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()

url = sys.argv[1]
asyncio.run(print_http_headers(url))