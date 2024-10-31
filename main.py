import asyncio

from socket_cyg.socket_server_asyncio import CygSocketServerAsyncio

if __name__ == '__main__':
    cyg = CygSocketServerAsyncio()
    asyncio.run(cyg.run_socket_server())