from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only tasks of the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the logged-in user as the task owner
        serializer.save(user=self.request.user)

