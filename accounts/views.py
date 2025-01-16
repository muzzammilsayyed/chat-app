from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from .serializers import UserSerializer, UserRegistrationSerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    template_name = 'registration/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('chat_room_default')
        return render(request, self.template_name, {'errors': serializer.errors})

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    template_name = 'registration/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('chat_room_default')
        return render(request, self.template_name)

    @method_decorator(csrf_protect)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('chat_room_default')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, self.template_name)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('login')

    def post(self, request):
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('login')

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)