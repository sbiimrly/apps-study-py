import tkinter as tk
from tkinter import messagebox
import pygame

# Inisialisasi pygame
pygame.init()

# Setting ukuran window untuk pygame
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aplikasi Belajar Bahasa Jepang")

# Warna yang digunakan
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font untuk pygame dan tkinter
font_pygame = pygame.font.SysFont("Arial", 30)
font_tkinter = ("Arial", 14)

# Data untuk soal
soal = {
    "gambar": "hiragana.png",  # Ganti dengan path gambar kanji Anda
    "jawaban_benar": "おおきい",  # Misalnya jawaban yang benar dalam hiragana
}

# Variabel poin
poin = 0

# Fungsi untuk menampilkan gambar dan teks di pygame
def tampilkan_gambar():
    gambar = pygame.image.load(soal["gambar"])
    gambar = pygame.transform.scale(gambar, (400, 400))
    screen.fill(WHITE)
    screen.blit(gambar, (200, 100))
    # Menampilkan teks instruksi
    teks = font_pygame.render("Masukkan jawaban Anda:", True, BLACK)
    screen.blit(teks, (300, 520))

# Fungsi untuk mengecek jawaban
def cek_jawaban(jawaban):
    global poin
    if jawaban == soal["jawaban_benar"]:
        poin += 5
        messagebox.showinfo("Jawaban Benar!", f"Jawaban Anda benar! Poin: {poin}")
    else:
        messagebox.showwarning("Jawaban Salah", f"Jawaban Anda salah. Poin: {poin}")

# Fungsi untuk membuat jendela Tkinter dan menangani input teks
def create_tkinter_window():
    global poin
    
    def kirim():
        jawaban = entry.get()
        cek_jawaban(jawaban)
        entry.delete(0, tk.END)  # Kosongkan input setelah kirim
        root.after(1000, main_game)  # Kembali ke tampilan utama setelah 1 detik

    # Membuat jendela tkinter
    root = tk.Tk()
    root.title("Input Jawaban")
    
    label = tk.Label(root, text="Arti kata tersebut (Latin):", font=font_tkinter)
    label.pack(pady=10)

    entry = tk.Entry(root, font=font_tkinter)
    entry.pack(pady=10)

    button = tk.Button(root, text="Kirim", font=font_tkinter, command=kirim)
    button.pack(pady=20)
    
    root.mainloop()

# Fungsi utama untuk menjalankan aplikasi
def main_game():
    tampilkan_gambar()
    pygame.display.update()
    
    # Membuka jendela Tkinter untuk input jawaban
    create_tkinter_window()

# Menjalankan aplikasi
main_game()

# Menutup pygame saat aplikasi ditutup
pygame.quit()
