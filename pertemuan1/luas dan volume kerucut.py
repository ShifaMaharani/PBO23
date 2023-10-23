from math import pi
print("Menghitung Luas dan Volume Kerucut")

# variabel
jari_jari = 5
tinggi = 12
garis_pelukis = 13

# masukan nilai pi
# Rumus luas permukaan kerucut
luas_permukaan = pi * jari_jari * (jari_jari + garis_pelukis)

# Rumus volume kerucut
volume = (1/3) * pi * (jari_jari ** 2) * tinggi

# Output
print("Luas Permukaan Kerucut: ", luas_permukaan)
print("Volume Kerucut: ", volume)
