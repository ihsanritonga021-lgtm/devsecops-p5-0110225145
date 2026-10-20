"""Validasi input agar data tugas sesuai aturan."""

MAX_TITLE_LENGTH = 80


def validate_title(title: str) -> str:
    """Validasi judul tugas dan kembalikan versi yang sudah dirapikan."""
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Judul tugas tidak boleh kosong.")
    if len(cleaned) > MAX_TITLE_LENGTH:
        raise ValueError(f"Judul maksimal {MAX_TITLE_LENGTH} karakter.")
    if any(ord(char) < 32 for char in cleaned):
        raise ValueError("Judul mengandung karakter kontrol yang tidak diizinkan.")
    return cleaned
