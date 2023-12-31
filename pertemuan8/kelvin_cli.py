print("Konversi Suhu Kelvin")

# Input
suhu_kelvin = float(input("Masukkan suhu dalam Kelvin: "))

# Formulas
R = 4/5 * (suhu_kelvin - 273)  # Kelvin to Reamur
F = 9/5 * (suhu_kelvin - 273) + 32  # Kelvin to Fahrenheit
C = suhu_kelvin - 273  # Kelvin to Celsius

# Round the results
R = round(R, 2)
F = round(F, 2)
C = round(C, 2)

# Output
print(str(suhu_kelvin) + " Kelvin sama dengan: ")
print(str(R) + " Reamur ")
print(str(F) + " Fahrenheit ")
print(str(C) + " Celsius ")
