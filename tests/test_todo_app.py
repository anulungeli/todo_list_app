import unittest
from app.todo_app import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertEqual(len(self.todo_list.tasks), 1)

    # Add more test cases for other methods

if __name__ == '__main__':
    unittest.main()
