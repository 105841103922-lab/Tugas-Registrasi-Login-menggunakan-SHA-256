# 🔐 Sistem Registrasi & Login — SHA-256

Tugas Mahasiswa No Urut **1–15**
Mata Kuliah: kriptografi
Dosen: Desi Anggreani, S.Kom., M.T.

---

## 📌 Deskripsi

Program Python sederhana yang mengimplementasikan sistem **registrasi** dan **login** user menggunakan algoritma hash **SHA-256**. Password tidak pernah disimpan dalam bentuk teks asli — hanya hash-nya yang disimpan.

---

## 🛠️ Fitur Program

| No | Fitur | Keterangan |
|----|-------|------------|
| 1 | **Registrasi User** | Mendaftarkan username dan password baru |
| 2 | **Hash Password** | Mengubah password menjadi hash SHA-256 (64 karakter hex) |
| 3 | **Simpan Data** | Menyimpan username + hash ke file `users.json` |
| 4 | **Tampilkan Hash** | Menampilkan hasil hash password saat registrasi |
| 5 | **Login** | Verifikasi password dengan membandingkan hash |
| 6 | **Status Login** | Menampilkan "Login Berhasil" atau "Login Gagal" |

---

## ▶️ Cara Menjalankan

### 1. Clone repository
```bash
git clone https://github.com/105841103922-lab/Tugas-Registrasi-Login-menggunakan-SHA-256.git
cd tugas-hash-sha256
```

### 2. Jalankan program
```bash
python app.py
```

> ✅ **Tidak perlu install library tambahan** — hanya menggunakan `hashlib` dan `json` yang sudah built-in Python.

---

## 📂 Struktur File

```
tugas-hash-sha256/
├── app.py        ← Program utama
├── users.json    ← Database user (dibuat otomatis saat pertama kali register)
└── README.md     ← Dokumentasi ini
```

---

## 🖥️ Contoh Output

### Registrasi
```
==================================================
         REGISTRASI USER BARU
==================================================
Masukkan username : budi
Masukkan password  : admin123

──────────────────────────────────────────────────
  ✅  REGISTRASI BERHASIL
──────────────────────────────────────────────────
  Username      : budi
  Password Asli : admin123
  Hash SHA-256  : 240be518fabd2724ddb6f04eeb1cb3975af0a0f2d4a8f7f4e2f7b5c8d9e1f2a
  Terdaftar     : 2025-07-10 09:15:30
──────────────────────────────────────────────────
  Password disimpan dalam bentuk hash, bukan teks asli.
──────────────────────────────────────────────────
```

### Login Berhasil
```
==================================================
              LOGIN USER
==================================================
Masukkan username : budi
Masukkan password  : admin123

──────────────────────────────────────────────────
  PROSES VERIFIKASI
──────────────────────────────────────────────────
  Username         : budi
  Hash Input       : 240be518fabd2724ddb6f04eeb1cb3975af0a0f2d4a8f7f4e2f7b5c8d9e1f2a
  Hash Tersimpan   : 240be518fabd2724ddb6f04eeb1cb3975af0a0f2d4a8f7f4e2f7b5c8d9e1f2a

  ✅  LOGIN BERHASIL — Selamat datang, budi!
──────────────────────────────────────────────────
```

### Login Gagal
```
  ❌  LOGIN GAGAL — Password salah.
```

---

## 🔬 Cara Kerja SHA-256

```
Password Asli  →  hashlib.sha256(password.encode()).hexdigest()  →  Hash (64 hex)

"admin123"     →  SHA-256  →  240be518fabd2724ddb6f04eeb1cb3975af...
```

- Output **selalu 64 karakter** hexadecimal (256 bit)
- Hash yang sama untuk input yang sama (**deterministik**)
- Tidak bisa dikembalikan ke teks asli (**one-way**)
- Dua input berbeda **tidak akan menghasilkan hash yang sama** (collision-resistant)

---

## 📝 Penjelasan Kode

```python
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
```

| Langkah | Penjelasan |
|---------|------------|
| `password.encode()` | Mengubah string ke bytes (UTF-8) |
| `hashlib.sha256(...)` | Membuat objek hash SHA-256 |
| `.hexdigest()` | Mengambil hasil hash dalam format hexadecimal |

---

## ⚠️ Catatan Keamanan

- SHA-256 lebih aman daripada MD5 untuk penyimpanan password
- Untuk keamanan lebih tinggi di produksi, gunakan **bcrypt** atau **argon2** yang menyertakan *salt* otomatis
- Program ini dibuat untuk keperluan **pembelajaran** konsep hashing

---

## 📋 Perbandingan MD5 vs SHA-256

| Aspek | MD5 | SHA-256 |
|-------|-----|---------|
| Panjang output | 128 bit | 256 bit |
| Karakter hex | 32 | 64 |
| Keamanan | Lemah | Lebih kuat |
| Collision | Rentan | Jauh lebih sulit |
| Rekomendasi | ❌ Tidak | ✅ Ya |

---

## 👨‍💻 Teknologi

- **Python 3.x**
- `hashlib` — library hashing bawaan Python
- `json` — penyimpanan data user

---

*Tugas Pertemuan 7 — Keamanan Jaringan*
