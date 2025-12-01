from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'resolved', 'created_at')
    list_filter = ('resolved', 'due_date')
    search_fields = ('title', 'description')
