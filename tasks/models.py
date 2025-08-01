from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
