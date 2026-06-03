import tkinter as tk
from tkinter import ttk, messagebox

class LayoutBuku:
    def __init__(self, root, switch_page_callback, app_manager):
        self.root = root
        self.switch_page = switch_page_callback
        self.app = app_manager  

    def clear_window(self, title):
        self.root.title(title)
        for w in self.root.winfo_children(): w.destroy()
        tk.Label(self.root, text=title, font=("Poppins", 13, "bold")).pack(pady=10)

    def create_nav_buttons(self, submit_cmd, submit_text="Simpan"):
        fr = tk.Frame(self.root); fr.pack(pady=15)
        tk.Button(fr, text=submit_text, font=("Poppins", 10), width=12, command=submit_cmd).pack(side="left", padx=5)
        tk.Button(fr, text="Kembali", font=("Poppins", 10), width=10, bg="red", fg="white", command=self.home).pack(side="right", padx=5)

    def build_treeview(self):
        cols = ('judul', 'penulis', 'genre', 'tahun', 'rating')
        tree = ttk.Treeview(self.root, columns=cols, show='headings', height=10)
        hdrs = {'judul': ('Judul Buku', 140), 'penulis': ('Penulis', 110), 'genre': ('Genre', 130), 'tahun': ('Tahun', 70), 'rating': ('Rating', 60)}
        for k, (txt, w) in hdrs.items():
            tree.heading(k, text=txt)
            tree.column(k, width=w, anchor="center" if k in ['tahun', 'rating'] else "w")
        tree.pack(padx=15, pady=10, fill="both", expand=True)
        return tree

    def home(self):
        self.clear_window("Sistem Rekomendasi Buku")
        fr = tk.Frame(self.root); fr.pack(pady=10)
        menus = [
            ('Tampilkan Buku', self.display), ('Tambah Buku Baru', self.newBook),
            ('Hapus Buku', self.deleteBook), ('Ubah Rating Buku', self.changeRating),
            ('Rekomendasi Buku', self.recommendation)
        ]
        for txt, cmd in menus:
            tk.Button(fr, text=txt, font=("Poppins", 10), width=25, command=cmd).pack(pady=4)
        tk.Button(fr, text="Keluar", font=("Poppins", 10, "bold"), width=25, bg="red", fg="white", command=self.root.quit).pack(pady=15)

    def display(self):
        self.clear_window("Daftar Buku di Sistem")
        top = tk.Frame(self.root); top.pack(fill="x", padx=15)
        tk.Button(top, text="Kembali", font=("Poppins", 9), command=self.home).pack(side="left")
        
        sort_var = tk.StringVar()
        box = ttk.Combobox(top, textvariable=sort_var, state="readonly", values=("Berdasarkan Alfabet", "Berdasarkan Rating Tertinggi"), width=25)
        box.current(0); box.pack(side="right")
        
        tree = self.build_treeview()
        def update_data(*args):
            for r in tree.get_children(): tree.delete(r)
            
            if sort_var.get() == "Berdasarkan Rating Tertinggi":
                data = self.app.byRating()
            else:
                raw_data = []
                for v in self.app.db.values():
                    raw_data.append((v.judul, v.penulis, ", ".join(v.genre), v.tahun_terbit, v.rating))
                data = sorted(raw_data, key=lambda x: x[0])
                
            for item in data: 
                tree.insert('', 'end', values=item)
        
        box.bind("<<ComboboxSelected>>", update_data); update_data()

    def newBook(self):
        self.clear_window("Tambah Buku Baru")
        fr = tk.Frame(self.root); fr.pack(pady=5)
        lbls = ["Judul Buku:", "Penulis:", "Genre (pisahkan dengan koma):", "Tahun Terbit:", "Rating:"]
        entries = {}
        for l in lbls:
            row = tk.Frame(fr); row.pack(fill="x", pady=3)
            tk.Label(row, text=l, font=("Poppins", 9), width=25, anchor="w").pack(side="left")
            entries[l] = tk.Entry(row, font=("Poppins", 9), width=30); entries[l].pack(side="right", fill="x")

        def save():
            vals = [entries[k].get().strip() for k in lbls]
            if any(v == "" for v in vals): return messagebox.showerror("Error", "Semua kolom harus diisi!")
            try:
                if self.app.add(vals[0].title(), vals[1].title(), [g.strip().title() for g in vals[2].split(',')], int(vals[3]), float(vals[4])):
                    messagebox.showinfo("Sukses", "Buku berhasil ditambahkan!"); self.home()
                else: messagebox.showerror("Error", "Buku sudah ada!")
            except ValueError: messagebox.showerror("Error", "Format Tahun (Angka) atau Rating (Desimal) Salah!")
        self.create_nav_buttons(save)

    def deleteBook(self):
        self.clear_window("Hapus Buku dari Sistem")
        fr = tk.Frame(self.root); fr.pack(pady=15)
        tk.Label(fr, text="Masukkan Judul Buku:", font=("Poppins", 10)).pack(side="left", padx=5)
        ent = tk.Entry(fr, font=("Poppins", 10), width=30); ent.pack(side="right", padx=5)
        
        def drop():
            j = ent.get().strip().title()
            if not j: return messagebox.showerror("Error", "Masukkan judul!")
            if self.app.remove(j): messagebox.showinfo("Sukses", "Buku dihapus!"); self.home()
            else: messagebox.showerror("Error", "Buku tidak ditemukan!")
        self.create_nav_buttons(drop, "Hapus")

    def changeRating(self):
        self.clear_window("Ubah Rating Buku")
        fr = tk.Frame(self.root); fr.pack(pady=10)
        tk.Label(fr, text="Judul Buku:").grid(row=0, column=0, sticky="w", pady=4)
        e_j = tk.Entry(fr, width=30); e_j.grid(row=0, column=1, pady=4)
        tk.Label(fr, text="Rating Baru:").grid(row=1, column=0, sticky="w", pady=4)
        e_r = tk.Entry(fr, width=30); e_r.grid(row=1, column=1, pady=4)

        def update():
            j, r = e_j.get().strip().title(), e_r.get().strip()
            if not j or not r: return messagebox.showerror("Error", "Semua kolom wajib diisi!")
            try:
                if self.app.update_rating(j, float(r)): messagebox.showinfo("Sukses", "Rating diperbarui!"); self.home()
                else: messagebox.showerror("Error", "Buku tidak ditemukan!")
            except ValueError: messagebox.showerror("Error", "Rating harus angka desimal!")
        self.create_nav_buttons(update)

    def recommendation(self):
        self.clear_window("Cari Rekomendasi Buku")
        tk.Label(self.root, text="Masukkan genre favorit Anda (misal: Fiksi, Sejarah):", font=("Poppins", 9)).pack(pady=5)
        ent = tk.Entry(self.root, font=("Poppins", 10), width=40); ent.pack(pady=5)
        
        def find():
            g = ent.get().strip()
            if not g: return messagebox.showerror("Error", "Masukkan genre!")
            self.recommendationResult(self.app.byGenre([x.strip().title() for x in g.split(',')]))
        self.create_nav_buttons(find, "Rekomendasikan")

    def recommendationResult(self, data):
        self.clear_window("Hasil Rekomendasi Buku Untuk Anda")
        tk.Button(self.root, text="Kembali", font=("Poppins", 9), command=self.recommendation).pack(anchor="w", padx=15)
        tree = self.build_treeview()
        for item in data: tree.insert('', 'end', values=item)