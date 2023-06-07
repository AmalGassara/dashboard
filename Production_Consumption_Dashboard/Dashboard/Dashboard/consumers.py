import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class MapConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            # Send updates to the client
            await self.send(json.dumps({
                'latitude': 37.7749,
                'longitude': -122.4194,
            }))

            # Wait for a short period before sending the next update
            await asyncio.sleep(1)
