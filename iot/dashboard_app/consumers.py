from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({"val1":randint(0, 50), "val2":randint(0, 50), "val3":randint(0, 50)}))
            await sleep(1)