import sys
import os

# Menambahkan direktori utama (root) proyek ke system path Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.user_model import UserModel

# Inisialisasi UserModel
model = UserModel()

# Coba daftarkan user baru
username = "mahasiswa_uji"
password_asli = "kampusmerdeka"
role = "anggota"

sukses = model.register_user(username, password_asli, role)

if sukses:
    print(f"Berhasil mendaftarkan user '{username}'!")
    print("Silakan cek tabel 'users' di database untuk melihat hasil hash password-nya.")
else:
    print("Gagal mendaftarkan user.")