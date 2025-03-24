import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Game
from .views import generate_random_build

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_slug = self.scope['url_route']['kwargs']['game_slug']
        self.room_group_name = f'game_{self.game_slug}'

        # Присоединяемся к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от группы
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message == 'generate_build':
            # Генерируем новую сборку
            build_data = await self.generate_build()
            # Отправляем данные всем в группе
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'build_update',
                    'build_data': build_data
                }
            )

    async def build_update(self, event):
        # Отправляем данные в WebSocket
        await self.send(text_data=json.dumps(event['build_data']))

    @database_sync_to_async
    def generate_build(self):
        game = Game.objects.get(slug=self.game_slug)
        return generate_random_build(game) 