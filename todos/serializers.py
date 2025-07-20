from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for Todo model
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_overdue = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = [
            'id', 'user', 'title', 'description', 'status', 'priority',
            'due_date', 'created_at', 'updated_at', 'is_overdue'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'is_overdue']
    
    def create(self, validated_data):
        # Set the user to the current authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class TodoCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new todos
    """
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'priority', 'due_date']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class TodoUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating todos
    """
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'priority', 'due_date']
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.save()
        return instance


class TodoListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing todos (simplified version)
    """
    is_overdue = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'status', 'priority', 'due_date', 'is_overdue', 'created_at'] 