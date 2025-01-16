from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'messages', views.ChatMessageViewSet, basename='chat-message')

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', views.chat_room, name='chat_room_default'),
    path('chat/<int:receiver_id>/', views.chat_room, name='chat_room'),
]