def to_celsius(f):
    return (f - 32) * 5 / 9

def to_fahrenheit(c):
    return (c * 9 / 5) + 32

# Dono convertors ko test karne ke liye simple inputs
fah = float(input("Fahrenheit temperature : "))
print("Celsius mein:", to_celsius(fah))

cel = float(input("Celsius temperature : "))
print("Fahrenheit mein:", to_fahrenheit(cel))