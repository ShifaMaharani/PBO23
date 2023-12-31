import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from module import luas_segiempat, volume_segiempat

def hitung_luas():
    sisi = float(txtsisi.get())
    tinggilimas = float(txttinggilimas.get())
    tinggisegitiga = float(txttinggisegitiga.get())

    Luas = luas_segiempat(tinggilimas,sisi, tinggisegitiga)

    txtluas.delete(0, END)
    txtluas.insert(END, Luas)


def hitung_volume():
    sisi = float(txtsisi.get())
    tinggilimas = float(txttinggilimas.get())
    tinggisegitiga = float(txttinggisegitiga.get())

    Volume = volume_segiempat(tinggilimas,sisi, tinggisegitiga)

    txtvolume.delete(0, END)
    txtvolume.insert(END, Volume)


def hitung():
    hitung_luas()
    hitung_volume()


# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Limas Segiempat")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Sisi
sisi = Label(frame, text="Sisi:")
sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Limas
tinggilimas = Label(frame, text="Tinggi Limas:")
tinggilimas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga
tinggisegitiga = Label(frame, text="Tinggi Segitiga:")
tinggisegitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Sisi
txtsisi = Entry(frame)
txtsisi.grid(row=0, column=1)

# Textbox Tinggi Limas
txttinggilimas = Entry(frame)
txttinggilimas.grid(row=1, column=1)

# Textbox Tinggi Segitiga
txttinggisegitiga = Entry(frame)
txttinggisegitiga.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtluas = Entry(frame)
txtluas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
