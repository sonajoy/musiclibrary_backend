
# Create your views here.
from django.shortcuts import render
from .models import song
from .serializers import songSerializer, Userserializer
from rest_framework import generics
from rest_framework.filters import SearchFilter

from django.contrib.auth.models import User


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

class songListCreateView(generics.ListCreateAPIView):
    queryset = song.objects.all()
    serializer_class = songSerializer
    filter_backends = [SearchFilter]
    permission_classes = [IsAuthenticated]

class songDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = song.objects.all()
    serializer_class = songSerializer
    permission_classes = [IsAuthenticated]
    
    
#usser creation view 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]