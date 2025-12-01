from django.test import TestCase
from django.urls import reverse
from .models import TodoItem
from datetime import date

class TodoItemModelTest(TestCase):
    """
    Tests for the TodoItem model to ensure fields and methods work correctly.
    """

    def setUp(self):
        """
        Set up a reusable TodoItem instance for the tests.
        """
        self.todo_item = TodoItem.objects.create(
            title="Buy Groceries",
            description="Need milk, eggs, and bread.",
            due_date=date(2025, 12, 31)
        )

    def test_todo_creation(self):
        """
        Test that a TodoItem object is created correctly.
        """
        self.assertEqual(self.todo_item.title, "Buy Groceries")
        self.assertEqual(self.todo_item.description, "Need milk, eggs, and bread.")
        self.assertEqual(self.todo_item.due_date, date(2025, 12, 31))
        # Check that the default value for 'resolved' is False
        self.assertFalse(self.todo_item.resolved)
        # Check that the object exists in the database
        self.assertTrue(TodoItem.objects.exists())

    def test_resolved_default(self):
        """
        Test the default value of the resolved field.
        """
        # Create a new item without specifying resolved status
        new_item = TodoItem.objects.create(title="Default Check")
        self.assertFalse(new_item.resolved)

    def test_absolute_url(self):
        """
        Test the get_absolute_url method returns the correct reverse URL.
        """
        expected_url = reverse('todo_list')
        actual_url = self.todo_item.get_absolute_url()
        self.assertEqual(actual_url, expected_url)

    def test_string_representation(self):
        """
        Test the __str__ method returns the title.
        """
        self.assertEqual(str(self.todo_item), "Buy Groceries")

    def test_ordering(self):
        """
        Test the custom ordering defined in the Meta class.
        Resolved tasks should come last.
        """
        TodoItem.objects.create(title="Unresolved Task", resolved=False, due_date=date(2026, 1, 1))
        TodoItem.objects.create(title="Resolved Task", resolved=True, due_date=date(2024, 1, 1))
        
        # Query all tasks, ordered by the model's Meta class
        ordered_tasks = TodoItem.objects.all()

        # The model is ordered by 'resolved' (False comes first) then 'due_date'
        # Since we set resolved tasks to go to the bottom, the order should be:
        # 1. Buy Groceries (resolved=False, due_date=2025-12-31)
        # 2. Unresolved Task (resolved=False, due_date=2026-01-01)
        # 3. Resolved Task (resolved=True) 

        self.assertEqual(ordered_tasks[0].title, "Buy Groceries")
        self.assertEqual(ordered_tasks[1].title, "Unresolved Task")
        self.assertEqual(ordered_tasks[2].title, "Resolved Task")
