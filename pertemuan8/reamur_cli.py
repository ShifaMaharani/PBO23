print("Konversi Suhu Reamur ke Celcius, Fahrenheit, dan Kelvin")

# Input
suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))

# Formulas
C = (5/4 * suhu_reamur)
F = (9/4 * suhu_reamur) + 32
K = (5/4 * suhu_reamur) + 273

# Output
print(str(suhu_reamur) + " Reamur sama dengan ")
print(str(C) + " Celsius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")
