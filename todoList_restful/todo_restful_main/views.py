from django.shortcuts import render
from .models import TodoList
from .serializers import TodoSerializer, TodoCreateSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

# Create your views here.
class Todo_restful_main(ListAPIView):
    queryset = TodoList.objects.all()
    serializer = TodoSerializer(queryset)
    serializer_class = TodoSerializer

class Todo_restful_update(UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer = TodoSerializer(queryset)
    serializer_class = TodoSerializer

class Todo_restful_delete(DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer = TodoSerializer(queryset)
    serializer_class = TodoSerializer

class Todo_restful_create(CreateAPIView):
    queryset = TodoList.objects.all()
    serializer = TodoCreateSerializer(queryset)
    serializer_class = TodoCreateSerializer