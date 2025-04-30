import asyncio
import websockets
import json
import subprocess

async def handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        print(f"Received schedule: {data}")

        mqtt_payload = f"{data['on']},{data['off']}"
        subprocess.run(["mosquitto_pub", "-t", "light/control", "-m", mqtt_payload])
        print("Published to MQTT")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

asyncio.run(main())
