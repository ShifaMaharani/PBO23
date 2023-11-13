import math
import tkinter as tk
from tkinter import Label, Entry, Button, END, W
from module import luas_bola, volume_bola

def hitung_volume_dan_luas_permukaan():
    r = float(txtradius.get())
    volume =volume_bola (r )
    l_permukaan = luas_bola (r)

    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

    txtLuasP.delete(0, END)
    txtLuasP.insert(END, l_permukaan)


# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Volume dan Luas Permukaan Bola")

# Windows
frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama_label = Label(frame, text="Nama : Shifa Maharani : 220511052")
nama_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# Label Radius
radius_label = Label(frame, text="Radius:")
radius_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Radius
txtradius = Entry(frame)
txtradius.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung",
                       command=hitung_volume_dan_luas_permukaan)
hitung_button.grid(row=2, column=0, columnspan=2, pady=5)

# Output Label Volume
volume_label = Label(frame, text="Volume: ")
volume_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan_label = Label(frame, text="Luas Permukaan: ")
luas_permukaan_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuasP = Entry(frame)
txtLuasP.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
