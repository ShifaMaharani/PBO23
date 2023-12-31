class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_fahrenheit(self):
        val = self.suhu
        return val
    
    def get_celsius(self):
        val = 5/9 * (self.suhu - 32)
        return round(val, 2)  # Round Celsius value to two decimal places
    
    def get_reamur(self):
        val = 4/9 * (self.suhu - 32)
        return round(val, 2)  # Round Reamur value to two decimal places
    
    def get_kelvin(self):
        val = 5/9 * (self.suhu - 32) + 273
        return round(val, 2)  # Round Kelvin value to two decimal places

# Input
suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
F = Fahrenheit(suhu_fahrenheit)

# Obtain converted values
val = F.get_fahrenheit()
C = F.get_celsius()
R = F.get_reamur()
K = F.get_kelvin()

# Output
print(str(val) + " Fahrenheit, sama dengan: ")
print(str(C) + " Celsius ")
print(str(R) + " Reamur ")
print(str(K) + " Kelvin ")
