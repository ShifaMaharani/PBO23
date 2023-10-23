print("Menghitung Luas dan Volume Limas Segitiga")

# variabel
alas = 6
T_limas = 8
T_segitiga = 4

# rumus luas permukaan limas segitiga
luas_permukaan = (alas * T_limas) / 2 + 3 * (0.5 * alas * T_segitiga)

# Menghitung volume limas segitiga
volume = (alas ** 2 * T_segitiga) / 6

# Menampilkan hasil
print("Luas Permukaan Limas Segitiga: ", luas_permukaan)
print("Volume Limas Segitiga: ", volume)
