print("Menghitung Luas dan Volume Limas Segi Empat")

# variabel
tinggi = 10
sisi = 12

# rumus sisi miring
sisi_miring = ((sisi*0.5)*(sisi*0.5)+(tinggi*tinggi))
segitiga = 0.5*sisi*sisi_miring

# perhitungan rumus
luas = (sisi*sisi)+(4*segitiga)
volume = (1/3)*(sisi*sisi)*tinggi

# output
print("Luas Limas =", luas)
print("Volume Limas =", volume)
