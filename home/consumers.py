from channels.generic.websocket import websocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(websocketConsumer):
    async def connect(self):
        self.room_name="test_consumer"
        self.room_group_name="test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':'connected'}))

    def receive(self):
        pass

    def disconnect(self):
        pass