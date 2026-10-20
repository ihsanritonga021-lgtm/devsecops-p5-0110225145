"""Fungsi bantuan untuk tampilan SecureTask."""


def format_task(task) -> str:
    """Ubah objek tugas menjadi teks yang mudah dibaca."""
    status = "Selesai" if task.completed else "Belum selesai"
    return f"[{task.task_id}] {task.title} — {status}"


def print_message(message: str) -> None:
    """Cetak pesan aplikasi dengan awalan yang konsisten."""
    print(f"[SecureTask] {message}")
