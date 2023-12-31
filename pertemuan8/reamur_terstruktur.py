print("Konversi Suhu Reamur")

def get_celsius(suhu):
    C = (5/4 * float(suhu))
    return C

def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

def get_kelvin(suhu):
    K = (5/4 * float(suhu)) + 273
    return K

# Input
suhu = input("Masukkan suhu dalam Reamur: ")

# Formulas
C = get_celsius(suhu)
F = get_fahrenheit(suhu)
K = get_kelvin(suhu)

# Output
print(str(suhu) + " Reamur, sama dengan: ")
print(str(C) + " Celsius ")
print(str(F) + " Fahrenheit ")
print(str(K) + " Kelvin ")
