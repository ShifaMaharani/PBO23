print("Konversi Suhu Celcius")

def get_celsius(suhu_fahrenheit):
    C = 5/9 * (float(suhu_fahrenheit) - 32)
    return round(C, 2)  # Bulatkan nilai Celsius ke dua tempat desimal

def get_reamur(suhu_fahrenheit):
    R = 4/9 * (float(suhu_fahrenheit) - 32)
    return round(R, 2)  # Bulatkan nilai Reamur ke dua tempat desimal

def get_kelvin(suhu_fahrenheit):
    K = 5/9 * (float(suhu_fahrenheit) - 32) + 273
    return round(K, 2)  # Bulatkan nilai Kelvin ke dua tempat desimal

# Input
suhu_fahrenheit = input("Masukkan suhu dalam Fahrenheit:")

# Konversi Fahrenheit ke Celsius, Reamur, dan Kelvin
C = get_celsius(suhu_fahrenheit)
R = get_reamur(suhu_fahrenheit)
K = get_kelvin(suhu_fahrenheit)

# Output
print(suhu_fahrenheit + " Fahrenheit sama dengan: ")
print(str(C) + " Celsius ")
print(str(R) + " Reamur ")
print(str(K) + " Kelvin ")
