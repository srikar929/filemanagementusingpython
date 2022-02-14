import asyncio
import signal
from login_code import login_code
from register_code import register_code
"""importing functions with import functions, time, os, etc.
"""
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def choose(getting, putting):
    """defining  async def for getting and reading
    """
    message = """1. Register  2. Login\nEnter your choice :"""
    putting.write(message.encode())
    msggg = await getting.read(100)
    choice = msggg.decode().strip()
    if choice == '1':
        await register_code(getting, putting)
    else:
        await login_code(getting, putting)

async def maincode():
    """ this is the main code for the server
    """
    service = await asyncio.start_server(choose, '127.0.0.1', 9974)

    addr = service.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with service:
        await service.serve_forever()

asyncio.run(maincode())
