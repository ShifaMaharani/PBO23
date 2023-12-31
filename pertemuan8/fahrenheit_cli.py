print("Konversi Suhu Fahrenheit ke Celsius, Reamur, dan Kelvin")

# Input
suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

# Formulas
C = 5/9 * (suhu_fahrenheit - 32)  # Fahrenheit to Celsius
R = 4/9 * (suhu_fahrenheit - 32)  # Fahrenheit to Reamur
K = 5/9 * (suhu_fahrenheit - 32) + 273  # Fahrenheit to Kelvin

# Round the values to two decimal places
C = round(C, 2)
R = round(R, 2)
K = round(K, 2)

# Output
print(str(suhu_fahrenheit) + " Fahrenheit sama dengan: ")
print(str(C) + " Celsius ")
print(str(R) + " Reamur ")
print(str(K) + " Kelvin ")
