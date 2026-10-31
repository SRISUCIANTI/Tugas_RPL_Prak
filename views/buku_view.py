import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self, role="admin"):
        super().__init__()
        self.role = role
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("800x480")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1) # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=2) # Kolom Kanan (Tabel lebih lebar)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # FRAME KIRI: FORMULIR INPUT BUKU
        # ==========================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Input
        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Judul Buku")
        self.entry_judul.pack(pady=10, padx=15, fill="x")

        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Penulis")
        self.entry_penulis.pack(pady=10, padx=15, fill="x")

        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tahun Terbit (Misal: 2024)")
        self.entry_tahun.pack(pady=10, padx=15, fill="x")
        
        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green"
        )
        self.btn_simpan.pack(pady=10, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data",
            fg_color="orange"
        )
        self.btn_update.pack(pady=10, padx=15, fill="x")

        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data",
            fg_color="red"
        )
        self.btn_hapus.pack(pady=10, padx=15, fill="x")

        # Tombol Logout
        self.btn_logout = ctk.CTkButton(
            self.frame_kiri,
            text="Logout",
            fg_color="#D9534F",
            command=self.logout
        )
        self.btn_logout.pack(pady=20, padx=15, fill="x")

        # ==========================================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # ==========================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Tabel (Treeview dari tkinter standar)
        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        # Konfigurasi Header Tabel
        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        # Konfigurasi Lebar Kolom
        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("judul", width=150)
        self.tabel.column("penulis", width=120)
        self.tabel.column("tahun", width=80, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

        # Event Binding Tabel
        self.tabel.bind("<<TreeviewSelect>>", self.item_dipilih)    

        # Jalankan pengecekan otorisasi role
        self.terapkan_otorisasi()

    def terapkan_otorisasi(self):
        """Mengunci tombol Perbarui dan Hapus jika role pengguna adalah anggota"""
        if self.role.lower() == "anggota":
            self.btn_update.configure(state="disabled", fg_color="gray")
            self.btn_hapus.configure(state="disabled", fg_color="gray")

    def logout(self):
        """Menutup jendela BukuView dan kembali ke LoginView"""
        self.destroy()
        try:
            from views.login_view import LoginView
            app_login = LoginView()
            app_login.mainloop()
        except ImportError:
            pass

    def item_dipilih(self, event):
        """Fungsi otomatis untuk mengisi form di sebelah kiri saat baris tabel diklik"""
        selected_item = self.tabel.selection()
        if selected_item:
            item = self.tabel.item(selected_item)
            record = item['values']
            
            self.entry_judul.delete(0, "end")
            self.entry_judul.insert(0, record[1])
            
            self.entry_penulis.delete(0, "end")
            self.entry_penulis.insert(0, record[2])
            
            self.entry_tahun.delete(0, "end")
            self.entry_tahun.insert(0, record[3])

    def ambil_id_terpilih(self):
        selected_item = self.tabel.selection()
        if selected_item:
            item = self.tabel.item(selected_item)
            return item['values'][0]
        return None

    def bersihkan_form(self):
        self.entry_judul.delete(0, "end")
        self.entry_penulis.delete(0, "end")
        self.entry_tahun.delete(0, "end")