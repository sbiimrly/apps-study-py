import pygame
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# Inisialisasi pygame untuk suara
pygame.mixer.init()

# Daftar soal
soal_list = [
    {
        "gambar": "hiragana.png",  # Ganti dengan path gambar
        "teks": "Apa arti kata ini?",  # Teks soal
        "jawaban": "besar",  # Jawaban yang benar
        "opsi": ["besar", "kecil", "tinggi"]  # Opsi jawaban
    },
    {
        "gambar": "mijika.png",  # Ganti dengan path gambar
        "teks": "Apa arti kata ini?",
        "jawaban": "pendek",
        "opsi": ["tinggi", "pendek", "cantik"]
    },
        {
        "gambar": "anzen.png",  # Ganti dengan path gambar
        "teks": "Apa arti kata ini?",
        "jawaban": "aman",
        "opsi": ["aman", "enak", "lapar"]
    },
    # Tambahkan soal-soal lainnya di sini
]

# Inisialisasi window Tkinter
root = tk.Tk()
root.title("Aplikasi Belajar Bahasa Jepang")
root.geometry("600x400")

# Variabel skor
skor = 0

# Fungsi untuk memainkan suara "Hore!"
def play_sound():
    pygame.mixer.music.load("horw.mp3")  # Ganti dengan file suara "hore" Anda
    pygame.mixer.music.play()

# Fungsi untuk memperbarui soal
def next_question():
    global soal
    soal = random.choice(soal_list)  # Pilih soal secara acak
    image = Image.open(soal["gambar"])
    image = image.resize((250, 250))  # Sesuaikan ukuran gambar
    photo = ImageTk.PhotoImage(image)

    # Update gambar soal
    label_gambar.config(image=photo)
    label_gambar.image = photo

    # Update teks soal
    label_soal.config(text=soal["teks"])

    # Acak dan tampilkan opsi jawaban
    random.shuffle(soal["opsi"])
    for i, btn in enumerate(btn_opsi):
        btn.config(text=soal["opsi"][i])

# Fungsi untuk mengecek jawaban
def cek_jawaban(jawaban):
    global skor
    if jawaban == soal["jawaban"]:
        skor += 10
        play_sound()  # Mainkan suara "Hore!"
        messagebox.showinfo("Benar!", f"Jawaban benar! Skor Anda: {skor}")
    else:
        messagebox.showinfo("Salah!", f"Jawaban salah. Skor Anda: {skor}")
    
    # Tampilkan soal berikutnya
    next_question()

# Label untuk menampilkan soal gambar
label_gambar = tk.Label(root)
label_gambar.pack(pady=20)

# Label untuk menampilkan soal teks
label_soal = tk.Label(root, text="", font=("Arial", 16))
label_soal.pack(pady=10)

# Tombol untuk memilih opsi jawaban
btn_opsi = []
for i in range(3):  # Misalnya ada 3 opsi jawaban
    btn = tk.Button(root, text="", font=("Arial", 14), command=lambda i=i: cek_jawaban(btn_opsi[i].cget("text")))
    btn.pack(pady=5)
    btn_opsi.append(btn)

# Tampilkan soal pertama
next_question()

# Mulai aplikasi
root.mainloop()
