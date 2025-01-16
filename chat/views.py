from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



@login_required(login_url='login')
def chat_room(request, receiver_id=None):
    # Get all users except the current user
    users = User.objects.exclude(id=request.user.id).order_by('username')
    
    context = {
        'users': users,
    }
    
    if receiver_id:
        try:
            receiver = User.objects.get(id=receiver_id)
            room_name = f"chat_{min(request.user.id, receiver_id)}_{max(request.user.id, receiver_id)}"
            messages = ChatMessage.objects.filter(
                (Q(sender=request.user, receiver_id=receiver_id) |
                 Q(sender_id=receiver_id, receiver=request.user))
            ).order_by('timestamp')
            
            context.update({
                'room_name': room_name,
                'receiver_id': receiver_id,
                'receiver_username': receiver.username,
                'messages': messages,
                'active_user': receiver
            })
        except User.DoesNotExist:
            pass
    
    return render(request, 'chat/chat_room.html', context)

class ChatMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ChatMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ChatMessage.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by('timestamp')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)