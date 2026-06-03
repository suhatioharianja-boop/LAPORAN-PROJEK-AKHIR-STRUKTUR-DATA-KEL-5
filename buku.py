class Buku:
    def __init__(self, judul, penulis, genre, tahun_terbit, rating):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre          # Berupa list, misal: ['Fiksi', 'Misteri']
        self.tahun_terbit = tahun_terbit
        self.rating = rating

    def __str__(self):
        return f'{self.judul} ({self.tahun_terbit}) oleh {self.penulis} | {", ".join(self.genre)} | Rating: {self.rating}'

    def data(self):
        return {
            'judul': self.judul,
            'penulis': self.penulis,
            'genre': self.genre,
            'tahun_terbit': self.tahun_terbit,
            'rating': self.rating
        }