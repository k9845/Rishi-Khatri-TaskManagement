from rest_framework import generics, permissions

from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of tasks or create a new task.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the new task with the logged-in user as the owner.

        Parameters
        ----------
        serializer : TaskSerializer
            The serializer instance for the task being created.
        """
        serializer.save()


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a task instance.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
