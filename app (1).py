"""
============================================================
  SISTEM REGISTRASI DAN LOGIN MENGGUNAKAN SHA-256
  Mata Kuliah : Kriptografi
  Dosen       : Desi Anggreani, S.Kom.,M.T.
  Tugas       : Mahasiswa No Urut 1-15
============================================================
"""

import hashlib
import json
import os
from datetime import datetime

# ── File penyimpanan data user ──────────────────────────────
DATA_FILE = "users.json"


# ════════════════════════════════════════════════════════════
#  FUNGSI HASH SHA-256
# ════════════════════════════════════════════════════════════

def hash_password(password: str) -> str:
    """
    Mengubah password teks menjadi hash SHA-256.

    Args:
        password (str): Password dalam bentuk teks asli.

    Returns:
        str: Nilai hash SHA-256 (64 karakter hexadecimal).
    """
    return hashlib.sha256(password.encode()).hexdigest()


# ════════════════════════════════════════════════════════════
#  FUNGSI PENYIMPANAN DATA
# ════════════════════════════════════════════════════════════

def load_users() -> dict:
    """Membaca data user dari file JSON."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_users(users: dict) -> None:
    """Menyimpan data user ke file JSON."""
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)


# ════════════════════════════════════════════════════════════
#  FUNGSI REGISTRASI
# ════════════════════════════════════════════════════════════

def register() -> None:
    """
    Proses registrasi user baru:
    1. Meminta username dan password.
    2. Mengubah password menjadi hash SHA-256.
    3. Menyimpan username + hash ke file.
    4. Menampilkan hasil hash password.
    """
    print("\n" + "=" * 50)
    print("         REGISTRASI USER BARU")
    print("=" * 50)

    users = load_users()

    # Input username
    username = input("Masukkan username : ").strip()
    if not username:
        print("[!] Username tidak boleh kosong.")
        return

    if username in users:
        print(f"[!] Username '{username}' sudah terdaftar.")
        return

    # Input password
    password = input("Masukkan password  : ").strip()
    if not password:
        print("[!] Password tidak boleh kosong.")
        return

    # Hash password dengan SHA-256
    hashed = hash_password(password)

    # Simpan ke file
    users[username] = {
        "hash_password": hashed,
        "tanggal_daftar": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    save_users(users)

    # Tampilkan hasil
    print("\n" + "─" * 50)
    print("  ✅  REGISTRASI BERHASIL")
    print("─" * 50)
    print(f"  Username      : {username}")
    print(f"  Password Asli : {password}")
    print(f"  Hash SHA-256  : {hashed}")
    print(f"  Terdaftar     : {users[username]['tanggal_daftar']}")
    print("─" * 50)
    print("  Password disimpan dalam bentuk hash, bukan teks asli.")
    print("─" * 50)


# ════════════════════════════════════════════════════════════
#  FUNGSI LOGIN
# ════════════════════════════════════════════════════════════

def login() -> None:
    """
    Proses login user:
    1. Meminta username dan password.
    2. Mengubah password input menjadi hash SHA-256.
    3. Membandingkan hash dengan yang tersimpan.
    4. Menampilkan status login (berhasil / gagal).
    """
    print("\n" + "=" * 50)
    print("              LOGIN USER")
    print("=" * 50)

    users = load_users()

    username = input("Masukkan username : ").strip()
    password = input("Masukkan password  : ").strip()

    # Hash password yang dimasukkan saat login
    hashed_input = hash_password(password)

    print("\n" + "─" * 50)
    print("  PROSES VERIFIKASI")
    print("─" * 50)
    print(f"  Username         : {username}")
    print(f"  Hash Input       : {hashed_input}")

    # Verifikasi
    if username not in users:
        print("\n  ❌  LOGIN GAGAL — Username tidak ditemukan.")
    elif users[username]["hash_password"] == hashed_input:
        print(f"  Hash Tersimpan   : {users[username]['hash_password']}")
        print("\n  ✅  LOGIN BERHASIL — Selamat datang, " + username + "!")
    else:
        print(f"  Hash Tersimpan   : {users[username]['hash_password']}")
        print("\n  ❌  LOGIN GAGAL — Password salah.")
    print("─" * 50)


# ════════════════════════════════════════════════════════════
#  FUNGSI LIHAT DAFTAR USER (opsional / demo)
# ════════════════════════════════════════════════════════════

def lihat_users() -> None:
    """Menampilkan semua user yang terdaftar beserta hash password-nya."""
    print("\n" + "=" * 50)
    print("       DAFTAR USER TERDAFTAR")
    print("=" * 50)

    users = load_users()
    if not users:
        print("  Belum ada user yang terdaftar.")
        return

    for i, (uname, data) in enumerate(users.items(), start=1):
        print(f"\n  [{i}] Username      : {uname}")
        print(f"      Hash SHA-256  : {data['hash_password']}")
        print(f"      Terdaftar     : {data['tanggal_daftar']}")
    print("─" * 50)


# ════════════════════════════════════════════════════════════
#  DEMO HASH (edukasi)
# ════════════════════════════════════════════════════════════

def demo_hash() -> None:
    """Mendemonstrasikan cara kerja hashing SHA-256 pada teks."""
    print("\n" + "=" * 50)
    print("       DEMO HASH SHA-256")
    print("=" * 50)

    teks = input("Masukkan teks yang ingin di-hash : ").strip()
    hasil = hash_password(teks)

    print("\n" + "─" * 50)
    print("  === HASIL HASH ===")
    print(f"  Teks Asli  : {teks}")
    print(f"  SHA-256    : {hasil}")
    print(f"  Panjang    : {len(hasil)} karakter hexadecimal ({len(hasil) * 4} bit)")
    print("─" * 50)


# ════════════════════════════════════════════════════════════
#  MENU UTAMA
# ════════════════════════════════════════════════════════════

def menu() -> None:
    while True:
        print("\n" + "╔" + "═" * 48 + "╗")
        print("║   SISTEM REGISTRASI & LOGIN — SHA-256          ║")
        print("╠" + "═" * 48 + "╣")
        print("║  [1] Registrasi User Baru                      ║")
        print("║  [2] Login                                     ║")
        print("║  [3] Lihat Daftar User                         ║")
        print("║  [4] Demo Hash SHA-256                         ║")
        print("║  [5] Keluar                                    ║")
        print("╚" + "═" * 48 + "╝")

        pilihan = input("Pilih menu [1-5] : ").strip()

        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            lihat_users()
        elif pilihan == "4":
            demo_hash()
        elif pilihan == "5":
            print("\n  Terima kasih. Program selesai.\n")
            break
        else:
            print("\n  [!] Pilihan tidak valid. Masukkan angka 1-5.")


# ════════════════════════════════════════════════════════════
#  ENTRY POINT
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    menu()
