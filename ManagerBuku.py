import bukuDB
from buku import Buku

class BukuManager:
    def __init__(self):
        # Memuat data dari database fisik ke memori aplikasi
        self.db = bukuDB.muat_database()
            
        # Suntik data awal jika database masih kosong (Data Mocking)
        if len(self.db) == 0:
            print("Database kosong, menyuntikkan data buku awal...")
            data_awal = [
                ("Bumi Manusia", "Pramoedya Ananta Toer", ["Fiksi", "Sejarah"], 1980, 4.9),
                ("Laskar Pelangi", "Andrea Hirata", ["Fiksi", "Inspiratif"], 2005, 4.7),
                ("Laut Bercerita", "Leila S. Chudori", ["Fiksi", "Sejarah", "Drama"], 2017, 4.8),
                ("Filosofi Teras", "Henry Manampiring", ["Pengembangan Diri", "Filsafat"], 2018, 4.6),
                ("Atomic Habits", "James Clear", ["Pengembangan Diri", "Psikologi"], 2018, 4.8),
                ("Sherlock Holmes", "Arthur Conan Doyle", ["Misteri", "Detektif"], 1887, 4.5),
                ("Gadis Kretek", "Ratih Kumala", ["Fiksi", "Sejarah", "Romansa"], 2012, 4.4),
                ("Cantik Itu Luka", "Eka Kurniawan", ["Fiksi", "Misteri", "Sejarah"], 2002, 4.6),
                ("Sapiens", "Yuval Noah Harari", ["Sains", "Sejarah", "Antropologi"], 2011, 4.8),
                ("Sebuah Seni untuk Bersikap Bodo Amat", "Mark Manson", ["Pengembangan Diri", "Psikologi"], 2016, 4.3),
                ("Dunia Sophie", "Jostein Gaarder", ["Fiksi", "Filsafat"], 1991, 4.5),
                ("Pulang", "Leila S. Chudori", ["Fiksi", "Sejarah", "Drama"], 2012, 4.7),
                ("Hujan", "Tere Liye", ["Fiksi", "Sci-Fi", "Romansa"], 2016, 4.5),
                ("Ronggeng Dukuh Paruk", "Ahmad Tohari", ["Fiksi", "Sejarah", "Budaya"], 1982, 4.6),
                ("Dikta & Hukum", "Dhia'an Farah", ["Romansa", "Drama"], 2021, 4.2),
                ("Negeri 5 Menara", "Ahmad Fuadi", ["Fiksi", "Inspiratif", "Edukasi"], 2009, 4.4),
                ("Gitanjali", "Rabindranath Tagore", ["Puisi", "Sastra"], 1910, 4.7),
                ("A Brief History of Time", "Stephen Hawking", ["Sains", "Fisika", "Astronomi"], 1988, 4.8),
                ("Totto-chan: Gadis Kecil di Jendela", "Tetsuko Kuroyanagi", ["Edukasi", "Memoar", "Anak"], 1981, 4.9),
                ("The Da Vinci Code", "Dan Brown", ["Misteri", "Thriller", "Fiksi"], 2003, 4.4)
            ]
            for judul, penulis, genre, tahun, rating in data_awal:
                buku_baru = Buku(judul, penulis, genre, tahun, rating)
                bukuDB.simpan_buku(buku_baru)
            
            # Refresh memory setelah disuntik data awal
            self.refresh_db()

    def byTitle(self, judul_dicari):
        """Mencari buku berdasarkan judul (case-insensitive)
           Mengembalikan objek Buku jika ketemu, atau None jika tidak ketemu"""
        judul_clean = judul_dicari.strip().lower()
        for judul_key, objek_buku in self.db.items():
            if judul_key.lower() == judul_clean:
                return objek_buku
        return None
        
    def refresh_db(self):
        """Menyinkronkan data di memori aplikasi dengan database fisik"""
        self.db = bukuDB.muat_database()

    def add(self, judul, penulis, genre, tahun, rating):
        """Logika validasi sebelum menambah buku baru"""
        if judul in self.db:
            return False
        
        buku_baru = Buku(judul, penulis, genre, tahun, rating)
        bukuDB.simpan_buku(buku_baru)
        self.refresh_db()
        return True

    def remove(self, judul):
        """Logika validasi sebelum menghapus buku"""
        if judul not in self.db:
            return False
        
        hasil = bukuDB.hapus_buku(judul)
        self.refresh_db()
        return hasil

    def update_rating(self, judul, rating_baru):
        """Logika validasi sebelum memperbarui rating buku"""
        if judul not in self.db:
            return False
        
        buku = self.db[judul]
        buku.rating = rating_baru
        bukuDB.simpan_buku(buku) # Menimpa data lama dengan data baru
        self.refresh_db()
        return True

    def byRating(self):
        """Mengurutkan buku berdasarkan rating tertinggi"""
        raw_data = []
        for v in self.db.values():
            raw_data.append((v.judul, v.penulis, ", ".join(v.genre), v.tahun_terbit, v.rating))
        return sorted(raw_data, key=lambda x: x[4], reverse=True)

    def byGenre(self, genre_dicari):
        """Rekomendasi buku berdasarkan kecocokan genre"""
        raw_data = []
        for v in self.db.values():
            genre_buku_lowercase = [g.lower() for g in v.genre]
            if any(g.lower() in genre_buku_lowercase for g in genre_dicari):
                raw_data.append((v.judul, v.penulis, ", ".join(v.genre), v.tahun_terbit, v.rating))
        return raw_data
