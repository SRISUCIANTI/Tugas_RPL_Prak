#from Controllers.anggota_controllers import AnggotaController
from Controllers.buku_controllers import BukuController

if __name__ == "__main__":
    # Kamu bisa ubah menjadi "admin" atau "anggota" sesuai kebutuhan pengujian
    role_pengguna = "admin"  
    
    # Menjalankan aplikasi melalui controller dengan role pengguna
    app = BukuController(user_role=role_pengguna)
    app.run()