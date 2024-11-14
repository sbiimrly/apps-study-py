from tkinter import *
import tkinter as tk 
import pygame as py

# create root window
root = Tk()

# root window title and dimension
root.title("Belajar Bahasa Jepang")
# Set geometry (widthxheight)
root.geometry('240x600') #430x934

label = tk.Label(root, text="Selamat Datang di Belajar Bahasa Jepang!") 
label.pack()  # Menampilkan label di jendela 

# Fungsi button
def on_button_click(): 
    label.config(text="Tombol telah diklik!") 

button = tk.Button(root, text="Mulai Belajar", command=on_button_click) 
button.pack()  # Menampilkan tombol di jendela 

button = tk.Button(root, text="Keluar", command=root.destroy) 
button.pack()  # Menampilkan tombol di jendela 

# all widgets will be here
# Execute Tkinter
root.mainloop()