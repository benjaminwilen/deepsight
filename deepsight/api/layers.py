import asyncio
import websockets
import time

async def send_time(websocket):
    while True:
        data = f"Current time: {time.ctime()}"
        await websocket.send(data)
        await asyncio.sleep(1)

async def receive_messages(websocket):
    try:
        async for message in websocket:
            print(f"Received from client: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def handle_connection(websocket, path):
    print("Client connected")
    send_task = asyncio.create_task(send_time(websocket))
    receive_task = asyncio.create_task(receive_messages(websocket))
    await asyncio.gather(send_task, receive_task)

async def main():
    print("WebSocket server is running")
    server = await websockets.serve(handle_connection, "localhost", 6789)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())