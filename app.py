"""Antarmuka CLI sederhana untuk aplikasi SecureTask."""

from task_manager import TaskManager
from validators import validate_title
from utils import format_task, print_message
from config import APP_NAME


def main() -> None:
    """Jalankan menu interaktif SecureTask."""
    manager = TaskManager()
    print(f"=== {APP_NAME} ===")

    while True:
        print("\n1. Tambah tugas\n2. Lihat tugas\n3. Selesaikan tugas\n4. Hapus tugas\n5. Keluar")
        choice = input("Pilih menu (1-5): ").strip()

        if choice == "1":
            title = input("Judul tugas: ").strip()
            try:
                title = validate_title(title)
                task = manager.add_task(title)
                print_message(f"Tugas ditambahkan: {format_task(task)}")
            except ValueError as exc:
                print_message(str(exc))
        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print_message("Belum ada tugas.")
            for task in tasks:
                print(format_task(task))
        elif choice == "3":
            try:
                task_id = int(input("ID tugas yang diselesaikan: "))
                task = manager.complete_task(task_id)
                print_message(f"Tugas selesai: {format_task(task)}")
            except (ValueError, KeyError) as exc:
                print_message(f"Gagal menyelesaikan tugas: {exc}")
        elif choice == "4":
            try:
                task_id = int(input("ID tugas yang dihapus: "))
                manager.delete_task(task_id)
                print_message(f"Tugas dengan ID {task_id} dihapus.")
            except (ValueError, KeyError) as exc:
                print_message(f"Gagal menghapus tugas: {exc}")
        elif choice == "5":
            print_message("Terima kasih telah menggunakan SecureTask.")
            break
        else:
            print_message("Pilihan tidak valid. Masukkan angka 1 sampai 5.")


if __name__ == "__main__":
    main()
