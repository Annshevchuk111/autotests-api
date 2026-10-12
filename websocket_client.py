import asyncio
from email import message

import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message ="Hi server"
        print(f"sending {message} ")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f"Received from server: {response}")

asyncio.run(client())