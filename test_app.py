"""Unit test untuk validasi dan logika pengelolaan tugas."""

import unittest

from task_manager import TaskManager
from validators import validate_title


class ValidateTitleTests(unittest.TestCase):
    def test_trims_title(self):
        self.assertEqual(validate_title("  Belajar Python  "), "Belajar Python")

    def test_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_rejects_title_over_limit(self):
        with self.assertRaises(ValueError):
            validate_title("x" * 81)


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_and_list_task(self):
        task = self.manager.add_task("Mengerjakan tugas")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Membaca materi")
        completed = self.manager.complete_task(task.task_id)
        self.assertTrue(completed.completed)

    def test_complete_unknown_task_raises_error(self):
        with self.assertRaises(KeyError):
            self.manager.complete_task(999)

    def test_delete_task(self):
        task = self.manager.add_task("Tugas sementara")
        self.manager.delete_task(task.task_id)
        self.assertEqual(self.manager.list_tasks(), [])


if __name__ == "__main__":
    unittest.main()
