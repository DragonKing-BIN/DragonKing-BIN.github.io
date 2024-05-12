import asyncio
import websockets

# 存储连接的客户端
connected = set()

# 处理新连接
async def handler(websocket, path):
    # 连接建立时将其加入到已连接的客户端集合中
    connected.add(websocket)
    try:
        async for message in websocket:
            # 当接收到消息时
            # 将消息发送给所有连接的客户端
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    finally:
        # 当连接关闭时将其从已连接的客户端集合中移除
        connected.remove(websocket)

# 启动 WebSocket 服务器
start_server = websockets.serve(handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
