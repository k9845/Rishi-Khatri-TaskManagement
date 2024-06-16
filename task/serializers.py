from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.

    Meta
    ----
    model : Task
        The model that is being serialized.
    fields : str
        Specifies that all fields of the Task model should be included in the serialized output.
    """

    class Meta:
        model = Task
        fields = '__all__'
