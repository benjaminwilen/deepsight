import asyncio
import websockets

async def receive_messages():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

async def main():
    await receive_messages()

if __name__ == "__main__":
    asyncio.run(main())