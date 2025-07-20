from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Todo(models.Model):
    """
    Todo model for managing user tasks
    """
    STATUS_CHOICES = [
        ('PENDING', _('Pending')),
        ('IN_PROGRESS', _('In Progress')),
        ('COMPLETED', _('Completed')),
    ]
    
    PRIORITY_CHOICES = [
        ('LOW', _('Low')),
        ('MEDIUM', _('Medium')),
        ('HIGH', _('High')),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos',
        help_text=_('User who owns this todo')
    )
    title = models.CharField(
        max_length=200,
        help_text=_('Title of the todo')
    )
    description = models.TextField(
        blank=True,
        help_text=_('Detailed description of the todo')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
        help_text=_('Current status of the todo')
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='MEDIUM',
        help_text=_('Priority level of the todo')
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_('Due date for the todo')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('todo')
        verbose_name_plural = _('todos')
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    @property
    def is_overdue(self):
        """Check if the todo is overdue"""
        if self.due_date and self.status != 'COMPLETED':
            from django.utils import timezone
            return timezone.now() > self.due_date
        return False
