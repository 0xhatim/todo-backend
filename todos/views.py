from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Todo
from .serializers import (
    TodoSerializer, TodoCreateSerializer, TodoUpdateSerializer, TodoListSerializer
)


class TodoListView(generics.ListCreateAPIView):
    """
    List and create todos for the authenticated user
    """
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TodoCreateSerializer
        return TodoListSerializer
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            todo = serializer.save()
            return Response({
                'message': 'Todo created successfully',
                'todo': TodoSerializer(todo).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete a todo
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = TodoUpdateSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            todo = serializer.save()
            return Response({
                'message': 'Todo updated successfully',
                'todo': TodoSerializer(todo).data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            'message': 'Todo deleted successfully'
        }, status=status.HTTP_200_OK)


class TodoStatusUpdateView(APIView):
    """
    Update todo status only
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk, user=request.user)
            new_status = request.data.get('status')
            if new_status in dict(Todo.STATUS_CHOICES):
                todo.status = new_status
                todo.save()
                return Response({
                    'message': 'Todo status updated successfully',
                    'todo': TodoSerializer(todo).data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Invalid status value'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response({
                'error': 'Todo not found'
            }, status=status.HTTP_404_NOT_FOUND)


class TodoBulkOperationsView(APIView):
    """
    Bulk operations on todos (delete multiple, update status)
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        action = request.data.get('action')
        todo_ids = request.data.get('todo_ids', [])
        
        if not todo_ids:
            return Response({
                'error': 'No todo IDs provided'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        todos = Todo.objects.filter(id__in=todo_ids, user=request.user)
        
        if action == 'delete':
            count = todos.count()
            todos.delete()
            return Response({
                'message': f'{count} todos deleted successfully'
            }, status=status.HTTP_200_OK)
        
        elif action == 'update_status':
            new_status = request.data.get('status')
            if new_status in dict(Todo.STATUS_CHOICES):
                count = todos.update(status=new_status)
                return Response({
                    'message': f'{count} todos status updated successfully'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Invalid status value'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({
                'error': 'Invalid action. Use "delete" or "update_status"'
            }, status=status.HTTP_400_BAD_REQUEST)


class TodoStatsView(APIView):
    """
    Get todo statistics for the user
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user_todos = Todo.objects.filter(user=request.user)
        
        stats = {
            'total_todos': user_todos.count(),
            'pending_todos': user_todos.filter(status='PENDING').count(),
            'in_progress_todos': user_todos.filter(status='IN_PROGRESS').count(),
            'completed_todos': user_todos.filter(status='COMPLETED').count(),
            'overdue_todos': sum(1 for todo in user_todos if todo.is_overdue),
            'high_priority_todos': user_todos.filter(priority='HIGH').count(),
        }
        
        return Response(stats, status=status.HTTP_200_OK)
