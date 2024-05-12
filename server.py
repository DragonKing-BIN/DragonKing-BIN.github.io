import asyncio
import websockets

connected = set()

async def handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            await asyncio.wait([ws.send(message) for ws in connected])
    finally:
        connected.remove(websocket)

start_server = websockets.serve(handler, "", 8765)

print("WebSocket chatroom server started. Listening on port 8765.")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
