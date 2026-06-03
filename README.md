# 📚 Sistem Rekomendasi Buku (Book Recommendation System)

Dinata Hendra Ramadani     2517052022

Akbar Rohman Fadilah       2517052001

Suhatio Harianja           2517052033

Ricky Darmawan             2517052015


Sistem Rekomendasi Buku adalah aplikasi desktop berbasis Python yang dirancang untuk mengelola data buku serta memberikan rekomendasi literatur terbaik secara cerdas. Aplikasi ini dibangun dengan menerapkan konsep struktur data **Hashmap (Dictionary)**, **Array (List)**, serta algoritma **Filtering & Sorting** untuk menjamin efisiensi pengolahan data berskala besar.

Aplikasi ini menggunakan **Tkinter** sebagai antarmuka grafis (GUI) yang interaktif dan **Shelve** sebagai sistem basis data lokal yang persisten.

---

## ✨ Fitur Utama

* **Manajemen Data Buku (CRUD):** * **Tambah Buku:** Menambahkan buku baru dengan validasi data ganda untuk mencegah duplikasi judul.
    * **Tampilkan Buku:** Menyajikan seluruh koleksi dalam bentuk tabel grafis (`Treeview`) dengan fitur dinamis pengurutan (Sorting) berdasarkan Alfabet maupun Rating Tertinggi.
    * **Ubah Rating:** Memperbarui skor rating buku yang sudah tersimpan di dalam database.
    * **Hapus Buku:** Menghapus data buku secara permanen dari sistem berdasarkan judul.
* **Sistem Rekomendasi Cerdas:**
    * **Rekomendasi via Genre:** Menyaring data buku secara akurat menggunakan pencocokan multi-genre (*case-insensitive*) sesuai preferensi pengguna.
    * **Rekomendasi via Rating:** Menampilkan daftar buku terbaik berdasarkan urutan prioritas rating tertinggi.
* **Penyimpanan Persisten:** Mengintegrasikan modul `shelve` sehingga data tidak hilang saat aplikasi ditutup (*persistent storage*).
* **UI Dinamis & Responsif:** Mengatur posisi jendela aplikasi otomatis berada tepat di tengah layar pengguna secara matematis.

---

## 🛠️ Struktur Data & Algoritma yang Digunakan

1.  **Hashmap / Map (Python Dictionary):** Digunakan sebagai arsitektur penyimpanan memori utama (`self.db`). Judul buku bertindak sebagai *key* unik, sedangkan objek `Buku` bertindak sebagai *value* untuk memotong waktu pencarian (*O(1) time complexity*).
2.  **Array (Python List):** Digunakan untuk menampung sekumpulan kategori pada atribut genre dan sebagai wadah data temporer sebelum dimuat ke dalam tabel antarmuka.
3.  **Algoritma Filtering:** Memanfaatkan fungsi iterasi dikombinasikan dengan operasi `any()` untuk menyaring daftar kecocokan genre secara fleksibel.
4.  **Algoritma Sorting:** Mengurutkan struktur data berbentuk *list of tuple* menggunakan metode pengurutan berbasis kunci (rating/indeks alfabet) secara menurun (*descending*).

---

## 📂 Struktur Direktori Proyek

```text
├── database/
│   └── books.db          # File basis data lokal (Dibuat otomatis oleh sistem)
├── buku.py               # Blueprint/Class model objek Buku
├── bukuDB.py             # Data Access Object (DAO) untuk manipulasi file Shelve
├── BukuManager.py        # Controller/Logika bisnis sistem rekomendasi
├── LayoutBuku.py         # Presenter/Komponen antarmuka grafis Tkinter
├── main.py               # Titik masuk utama aplikasi (Main Entry Point)
└── README.md             # Dokumentasi proyek
