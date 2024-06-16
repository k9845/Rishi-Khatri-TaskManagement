from django.db import models


class Task(models.Model):
    """
    Task model to store task details.

    Attributes
    ----------
    title : str
        The title of the task (max length 200).
    description : str
        A detailed description of the task.
    completed : bool
        Status indicating whether the task is completed or not (default is False).
    created_at : datetime
        The date and time when the task was created (automatically set).
    updated_at : datetime
        The date and time when the task was last updated (automatically set).

    Methods
    -------
    __str__()
        Returns the string representation of the task (title).
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
