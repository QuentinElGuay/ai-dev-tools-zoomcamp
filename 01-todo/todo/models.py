from django.db import models
from django.urls import reverse

class TodoItem(models.Model):
    """
    Model for a single To-Do item.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['resolved', 'due_date'] # Resolved tasks go to the bottom

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Redirect to the list view after successful creation/update
        return reverse('todo_list')

# NOTE: After creating this, run 'python manage.py makemigrations' and 'python manage.py migrate'
