import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import ChatMessage

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        logger.debug(f"Attempting to connect to room: {self.room_group_name}")

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        logger.info(f"Successfully connected to room: {self.room_group_name}")

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        logger.info(f"WebSocket disconnected from room: {self.room_group_name}")

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            receiver_id = text_data_json['receiver_id']
            sender_id = self.scope["user"].id
            
            logger.debug(f"Received message: {message} from {sender_id} to {receiver_id}")

            # Save message to database
            await self.save_message(sender_id, receiver_id, message)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat.message',
                    'message': message,
                    'sender_id': sender_id,
                    'receiver_id': receiver_id
                }
            )
            logger.info(f"Message sent to group {self.room_group_name}")
        except Exception as e:
            logger.error(f"Error in receive: {str(e)}")
            raise

    async def chat_message(self, event):
        try:
            message = event['message']
            sender_id = event['sender_id']
            receiver_id = event['receiver_id']

            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'sender_id': sender_id,
                'receiver_id': receiver_id
            }))
            logger.info(f"Message broadcast to client: {message}")
        except Exception as e:
            logger.error(f"Error in chat_message: {str(e)}")
            raise

    @database_sync_to_async
    def save_message(self, sender_id, receiver_id, message):
        try:
            sender = User.objects.get(id=sender_id)
            receiver = User.objects.get(id=receiver_id)
            msg = ChatMessage.objects.create(
                sender=sender,
                receiver=receiver,
                message=message
            )
            logger.info(f"Message saved to database: {msg.id}")
            return msg
        except Exception as e:
            logger.error(f"Error saving message: {str(e)}")
            raise