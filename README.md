\# Sistem Manajemen Perpustakaan



\## 1. Deskripsi Aplikasi



Sistem Manajemen Perpustakaan merupakan aplikasi desktop berbasis Python yang dirancang untuk membantu pengelolaan data perpustakaan. Aplikasi ini menggunakan CustomTkinter untuk membangun antarmuka pengguna dan MySQL sebagai sistem manajemen basis data.



Aplikasi ini menerapkan arsitektur Model-View-Controller (MVC) untuk memisahkan pengelolaan data, tampilan antarmuka, dan logika pengendali aplikasi. Dengan penerapan MVC, struktur kode menjadi lebih terorganisasi, mudah dipahami, dan lebih mudah dikembangkan.



\## 2. Teknologi yang Digunakan



Teknologi dan perangkat yang digunakan dalam pengembangan aplikasi ini meliputi:



\- \*\*Python\*\*: bahasa pemrograman untuk mengembangkan aplikasi.

\- \*\*CustomTkinter\*\*: pustaka untuk membangun antarmuka aplikasi desktop.

\- \*\*MySQL\*\*: sistem manajemen basis data untuk menyimpan data aplikasi.

\- \*\*mysql-connector-python\*\*: pustaka untuk menghubungkan Python dengan MySQL.

\- \*\*pytest\*\*: alat untuk menjalankan pengujian otomatis.

\- \*\*flake8\*\*: alat untuk memeriksa kesalahan kode dan kualitas penulisan Python.

\- \*\*Git\*\*: sistem pengelolaan versi kode sumber.

\- \*\*GitHub\*\*: platform untuk menyimpan repositori dan mengelola kolaborasi kode.

\- \*\*GitHub Actions\*\*: layanan otomatisasi untuk menjalankan pemeriksaan dan pengujian kode melalui CI Pipeline.



\## 3. Struktur Direktori Proyek



```text

Tugas RPL prak/

├── .github/

│   └── workflows/

├── config/

├── Controllers/

├── models/

├── tests/

├── views/

├── main.py

├── requirements.txt

├── test\_model.py

├── README.md

└── .gitignore

```



Keterangan direktori dan berkas:



\- \*\*`.github/workflows/`\*\*: menyimpan konfigurasi GitHub Actions untuk menjalankan CI Pipeline secara otomatis.

\- \*\*`config/`\*\*: menyimpan konfigurasi aplikasi, termasuk pengaturan koneksi basis data.

\- \*\*`Controllers/`\*\*: berisi komponen pengendali yang mengatur alur aplikasi dan menghubungkan Model dengan View.

\- \*\*`models/`\*\*: berisi komponen yang menangani pengelolaan data dan interaksi dengan basis data.

\- \*\*`tests/`\*\*: menyediakan tempat untuk berkas pengujian otomatis.

\- \*\*`views/`\*\*: berisi komponen antarmuka pengguna aplikasi.

\- \*\*`main.py`\*\*: berkas utama untuk menjalankan aplikasi.

\- \*\*`requirements.txt`\*\*: mencatat pustaka Python yang diperlukan oleh proyek.

\- \*\*`test\_model.py`\*\*: berkas untuk menjalankan pengujian model.

\- \*\*`README.md`\*\*: berisi dokumentasi proyek.

\- \*\*`.gitignore`\*\*: menentukan berkas dan direktori yang tidak perlu dilacak oleh Git.



\## 4. Persiapan Lingkungan



Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki:



1\. Python yang telah terinstal.

2\. MySQL yang telah terinstal dan dapat dijalankan.

3\. Pustaka Python yang tercantum dalam `requirements.txt`.

4\. Kode sumber aplikasi yang telah tersedia secara lengkap.



\## 5. Konfigurasi Basis Data



Aplikasi menggunakan MySQL sebagai tempat penyimpanan data. Konfigurasi koneksi basis data disimpan dalam direktori `config/`.



Langkah konfigurasi:



1\. Jalankan layanan MySQL melalui Laragon atau perangkat lunak pengelola MySQL yang digunakan.

2\. Siapkan basis data sesuai dengan nama yang ditentukan dalam konfigurasi aplikasi.

3\. Pastikan tabel yang dibutuhkan aplikasi telah dibuat.

4\. Periksa pengaturan koneksi pada direktori `config/`.

5\. Sesuaikan host, port, username, password, dan nama basis data dengan konfigurasi MySQL pada komputer.

6\. Pastikan layanan MySQL aktif sebelum menjalankan aplikasi.



Nama basis data, struktur tabel, dan pengaturan koneksi harus mengikuti implementasi yang digunakan dalam kode sumber proyek.



\## 6. Instalasi Dependensi



Ikuti langkah berikut untuk menyiapkan lingkungan Python.



\### 6.1 Membuka Proyek



Buka folder proyek `Tugas RPL prak` melalui Visual Studio Code, kemudian buka terminal pada direktori tersebut.



\### 6.2 Mengaktifkan Virtual Environment



Jika menggunakan virtual environment bernama `env313`, jalankan perintah berikut pada PowerShell:



```powershell

.\\env313\\Scripts\\Activate.ps1

```



Jika virtual environment belum tersedia, buat terlebih dahulu menggunakan perintah:



```powershell

python -m venv env313

```



\### 6.3 Menginstal Dependensi



Setelah virtual environment aktif, jalankan perintah:



```powershell

pip install -r requirements.txt

```



Perintah tersebut digunakan untuk memasang pustaka yang tercantum dalam berkas `requirements.txt`.



\## 7. Menjalankan Aplikasi



Setelah dependensi terpasang dan konfigurasi basis data selesai, jalankan aplikasi melalui terminal menggunakan perintah:



```powershell

python main.py

```



Pastikan terminal berada pada direktori utama proyek dan layanan MySQL telah aktif sebelum menjalankan aplikasi.



\## 8. Pengujian Aplikasi



Pengujian dilakukan untuk memeriksa fungsi aplikasi dan membantu menemukan kesalahan pada kode sumber.



\### 8.1 Menjalankan Pengujian dengan Pytest



Gunakan perintah berikut pada terminal:



```powershell

pytest -v

```



Pytest akan menjalankan pengujian yang ditemukan sesuai dengan konfigurasi dan pola penamaan berkas pengujian.



\### 8.2 Pemeriksaan Kode dengan Flake8



Flake8 digunakan untuk memeriksa kesalahan kode tertentu pada direktori Model dan Controller.



Contoh perintah pemeriksaan:



```powershell

flake8 models/ Controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics

```



Pemeriksaan ini membantu mendeteksi kesalahan kritis pada kode Python sebelum perubahan dikirimkan ke repositori.



\## 9. Continuous Integration (CI Pipeline)



Proyek ini menggunakan GitHub Actions untuk menjalankan proses pemeriksaan kode dan pengujian secara otomatis.



CI Pipeline membantu memastikan bahwa perubahan kode dapat diperiksa sebelum digunakan lebih lanjut. Proses pemeriksaan mencakup instalasi dependensi, pemeriksaan kode menggunakan Flake8, dan pengujian menggunakan Pytest sesuai konfigurasi workflow proyek.



Hasil pelaksanaan pipeline dapat dilihat melalui tab \*\*Actions\*\* pada repositori GitHub.



\## 10. Pengelolaan Versi dengan Git dan GitHub



Git digunakan untuk mencatat perubahan kode sumber, sedangkan GitHub digunakan untuk menyimpan repositori proyek secara daring.



Perintah dasar untuk mengirimkan perubahan ke repositori adalah:



```powershell

git add .

git commit -m "Memperbarui dokumentasi proyek"

git push origin main

```



Perintah tersebut digunakan untuk menambahkan perubahan, membuat commit, dan mengirimkan perubahan ke branch `main` pada repositori GitHub.



\## 11. Pengembangan dan Distribusi Aplikasi



Aplikasi dapat dikembangkan lebih lanjut dengan menambahkan fitur, meningkatkan validasi data, memperbaiki antarmuka, dan mengembangkan pengujian otomatis.



Untuk distribusi pada sistem operasi Windows, aplikasi dapat dikemas menjadi berkas executable `.exe` menggunakan PyInstaller. Berkas hasil pengemasan dapat didistribusikan melalui GitHub Releases setelah proses pembuatan dan pengujian aplikasi selesai.



\## 12. Penutup



Dokumentasi ini menjelaskan gambaran umum aplikasi, struktur direktori, persiapan lingkungan, konfigurasi basis data, cara menjalankan aplikasi, pengujian, dan pengelolaan kode sumber.



Dokumentasi dapat diperbarui sesuai dengan perubahan fitur, struktur kode, dan konfigurasi aplikasi selama proses pengembangan.



