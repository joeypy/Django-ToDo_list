from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('complete',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
