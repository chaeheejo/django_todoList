from rest_framework import serializers
from .models import TodoList

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'complete', 'created_at', 'updated_at', 'summary', 'tag', 'due_date')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('title', 'complete', 'summary', 'tag', 'due_date')