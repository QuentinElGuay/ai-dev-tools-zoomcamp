from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy
from .models import TodoItem
from .forms import TodoForm

# 1. READ (List View)
class TodoListView(ListView):
    """
    Displays a list of all To-Do items.
    """
    model = TodoItem
    template_name = 'todo_list.html'
    context_object_name = 'todos'

# 2. CREATE (Create View)
class TodoCreateView(CreateView):
    """
    Handles creating a new To-Do item.
    """
    model = TodoItem
    form_class = TodoForm
    template_name = 'todo_form.html'
    # Success URL is defined in the model's get_absolute_url

# 3. UPDATE (Edit View)
class TodoUpdateView(UpdateView):
    """
    Handles editing an existing To-Do item.
    """
    model = TodoItem
    form_class = TodoForm
    template_name = 'todo_form.html'
    # Success URL is defined in the model's get_absolute_url

# 4. DELETE (Delete View)
class TodoDeleteView(DeleteView):
    """
    Handles deleting a To-Do item.
    """
    model = TodoItem
    template_name = 'todo_confirm_delete.html' # Create this template for confirmation
    success_url = reverse_lazy('todo_list')
