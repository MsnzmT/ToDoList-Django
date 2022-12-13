from rest_framework import serializers
from .models import *

class TaskSeializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('text', )


class ListDetailSerializer(serializers.ModelSerializer):
    tasks = TaskSeializer(read_only=True, many=True)

    class Meta:
        model = List
        fields = ('name', 'user', 'tasks')

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('name', )

class TaskEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('text', )