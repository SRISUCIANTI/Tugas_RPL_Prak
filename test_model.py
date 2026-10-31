
from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

# PENGUJIAN BUKU
model = BukuModel()

print("=== PENGUJIAN BUKU MODEL ===")

print("\n[+] Menambahkan data buku...")
model.create_buku(
    "Pemrograman Python MVC",
    "Guido van Rossum",
    2023
)

print("\n=== Daftar Buku Terkini ===")
data_buku = model.get_all_buku()

for buku in data_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )

# PENGUJIAN ANGGOTA
anggota = AnggotaModel()

print("\n=== PENGUJIAN ANGGOTA MODEL ===")

print("\n[+] Menambahkan data anggota...")
anggota.create_anggota(
    "Sri Sucianti",
    "Palu"
)

print("\n=== Daftar Anggota Terkini ===")
data_anggota = anggota.get_all_anggota()

for data in data_anggota:
    print(
        f"[{data['id_anggota']}] "
        f"{data['nama']} - "
        f"{data['alamat']}"
    )
