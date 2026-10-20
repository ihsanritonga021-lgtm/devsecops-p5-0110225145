"""Logika bisnis untuk mengelola daftar tugas."""

from dataclasses import dataclass


@dataclass
class Task:
    """Representasi satu tugas."""
    task_id: int
    title: str
    completed: bool = False


class TaskManager:
    """Mengelola tugas selama aplikasi berjalan."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        """Tambahkan tugas baru dengan ID unik."""
        task = Task(task_id=self._next_id, title=title)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        """Kembalikan seluruh tugas berdasarkan urutan ID."""
        return [self._tasks[key] for key in sorted(self._tasks)]

    def complete_task(self, task_id: int) -> Task:
        """Tandai tugas sebagai selesai."""
        if task_id not in self._tasks:
            raise KeyError(f"ID tugas {task_id} tidak ditemukan")
        self._tasks[task_id].completed = True
        return self._tasks[task_id]

    def delete_task(self, task_id: int) -> None:
        """Hapus tugas berdasarkan ID."""
        if task_id not in self._tasks:
            raise KeyError(f"ID tugas {task_id} tidak ditemukan")
        del self._tasks[task_id]
