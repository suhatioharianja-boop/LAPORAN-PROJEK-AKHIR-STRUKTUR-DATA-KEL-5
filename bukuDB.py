import os
import shelve
from buku import Buku

PATH = "database\\books.db"

folder_db = os.path.dirname(PATH)
if folder_db and not os.path.exists(folder_db):
    os.makedirs(folder_db)

def muat_database():
    """Membaca seluruh data dari shelve dan mengembalikannya dalam bentuk dictionary objek Buku"""
    buku_db_hashmap = {}
    with shelve.open(PATH) as db:
        for judul in db:
            data_mentah = db[judul]
            
            theBuku = Buku(
                judul=data_mentah['judul'],
                penulis=data_mentah['penulis'],
                genre=data_mentah['genre'],
                tahun_terbit=data_mentah['tahun_terbit'],
                rating=data_mentah['rating']
            )
            buku_db_hashmap[judul] = theBuku
    return buku_db_hashmap

def simpan_buku(buku_objek):
    """Menyimpan atau memperbarui objek Buku ke dalam shelve"""
    with shelve.open(PATH) as db:
        db[buku_objek.judul] = buku_objek.data()

def hapus_buku(judul):
    """Menghapus buku dari database shelve"""
    with shelve.open(PATH) as db:
        if judul in db:
            del db[judul]
            return True
        return False
