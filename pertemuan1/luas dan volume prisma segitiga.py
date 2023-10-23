print("Menghitung Luas dan Volume Prisma Segitiga")

# variabel
A_segitiga = 4
T_segitiga = 2
T_prisma = 6

# Rumus Luas permukaan
luas_permukaan = (A_segitiga * T_prisma) + 2 * (0.5 * A_segitiga * T_segitiga)

# Rumus volume prisma segitiga
volume = 0.5 * A_segitiga * T_segitiga * T_prisma

# Output
print("Luas Permukaan Prisma Segitiga: ", luas_permukaan)
print("Volume Prisma Segitiga: ", volume)
