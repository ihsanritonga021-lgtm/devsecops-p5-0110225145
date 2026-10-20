# SecureTask — Aplikasi Manajemen Tugas

SecureTask adalah aplikasi CLI sederhana berbasis Python untuk mengelola daftar tugas. Pengguna dapat menambah, melihat, menyelesaikan, dan menghapus tugas. Proyek ini digunakan sebagai contoh integrasi DevSecOps dan Static Application Security Testing (SAST) pada GitHub Actions.

## Teknologi
- Python 3.11+
- `unittest` untuk pengujian otomatis
- Semgrep untuk analisis kode statis (SAST)
- GitHub Actions untuk otomatisasi CI

## Struktur proyek

```text
securetask-devsecops/
├── app.py
├── task_manager.py
├── validators.py
├── utils.py
├── config.py
├── test_app.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── devsecops.yml
```

## Cara menjalankan aplikasi

1. Pastikan Python 3.11 atau lebih baru terpasang.
2. Clone repository:
   ```bash
   git clone https://github.com/USERNAME/securetask-devsecops.git
   cd securetask-devsecops
   ```
3. Jalankan aplikasi:
   ```bash
   python app.py
   ```

Aplikasi menyimpan tugas di memori selama program berjalan; data tidak disimpan setelah aplikasi ditutup.

## Menjalankan unit test

```bash
python -m unittest -v
```

## Overview pipeline CI/CD

Workflow pada `.github/workflows/devsecops.yml` dipicu saat ada `push` ke branch `main` atau `pull_request` menuju `main`. Job `build` memeriksa versi Python dan menjalankan unit test. Job `sast-scan` berjalan setelah `build` berhasil (`needs: build`) dan menjalankan Semgrep untuk memeriksa pola kode yang berpotensi bermasalah.

Pipeline memakai `ubuntu-latest`. Hasil scan dapat digunakan sebagai Quality Gate: jika aturan keamanan yang dikonfigurasi menemukan temuan dengan tingkat yang ditetapkan, job SAST dapat dibuat gagal. Temuan perlu ditinjau karena alat SAST dapat menghasilkan false positive dan tidak menjamin aplikasi sepenuhnya aman.

## Catatan
Proyek ini untuk pembelajaran. Pemeriksaan SAST melengkapi, bukan menggantikan, code review, unit test, pengujian keamanan dinamis, dan praktik pengamanan lain.
