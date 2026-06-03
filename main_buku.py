import tkinter as tk
import BukuManager as bm  
from LayoutBuku import LayoutBuku  

app = bm.BukuManager()

def main():
    root = tk.Tk()
    root.title("Sistem Rekomendasi Buku")
    
    window_width = 600
    window_height = 450
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(False, False)

    def alur_sistem(halaman_tujuan, data=None):
        if halaman_tujuan == 'home':
            app_interface.home()
        elif halaman_tujuan == 'display':
            app_interface.display()
        elif halaman_tujuan == 'add_book':
            app_interface.newBook()
        elif halaman_tujuan == 'delete_book':
            app_interface.deleteBook()
        elif halaman_tujuan == 'change_rating':
            app_interface.changeRating()
        elif halaman_tujuan == 'recommendation':
            app_interface.recommendation()
        elif halaman_tujuan == 'result' and data is not None:
            app_interface.recommendationResult(data)

    app_interface = LayoutBuku(root, alur_sistem, app)
    app_interface.home()
    root.mainloop()

if __name__ == "__main__":
    main()
