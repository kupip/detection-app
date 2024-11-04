import tkinter as tk
from tkinter import messagebox

def main_screen():
    root = tk.Tk()
    root.title("Object Detected App")

    # Judul
    title = tk.Label(root, text="Object Detected App", font=("Georgia", 20))
    title.pack(pady=20)

    # Tombol Menu Utama
    btn_jalan = tk.Button(root, text="Deteksi Jalan Berlubang", width=30, command=lambda: show_message("Deteksi Jalan Berlubang"))
    btn_jalan.pack(pady=10)
    
    btn_buah = tk.Button(root, text="Deteksi Buah Busuk", width=30, command=lambda: show_message("Deteksi Buah Busuk"))
    btn_buah.pack(pady=10)
    
    btn_manusia = tk.Button(root, text="Deteksi Manusia", width=30, command=lambda: show_message("Deteksi Manusia"))
    btn_manusia.pack(pady=10)

    root.geometry("900x700")
    root.mainloop()

def show_message(deteksi_type):
    messagebox.showinfo("Informasi", f"Memulai {deteksi_type}")

if __name__ == "__main__":
    main_screen()