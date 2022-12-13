from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('text', )


class ListDetailSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = List
        fields = ('id', 'name', 'user', 'tasks')

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('name', )

