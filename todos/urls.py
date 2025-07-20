from django.urls import path
from .views import (
    TodoListView, TodoDetailView, TodoStatusUpdateView,
    TodoBulkOperationsView, TodoStatsView
)

app_name = 'todos'

urlpatterns = [
    # Todo CRUD endpoints
    path('', TodoListView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('<int:pk>/status/', TodoStatusUpdateView.as_view(), name='todo-status'),
    
    # Bulk operations
    path('bulk/', TodoBulkOperationsView.as_view(), name='todo-bulk'),
    
    # Statistics
    path('stats/', TodoStatsView.as_view(), name='todo-stats'),
] 