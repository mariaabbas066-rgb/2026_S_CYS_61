import random

length = int(int(input("Password length kitni chahiye? ")))
use_upper = input("Uppercase shamil karein? (y/n): ").lower()
use_digits = input("Digits shamil karein? (y/n): ").lower()
use_special = input("Special characters shamil karein? (y/n): ").lower()

# Default lowercase har haal mein hoga
pool = "abcdefghijklmnopqrstuvwxyz"

if use_upper == 'y':
    pool = pool + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if use_digits == 'y':
    pool = pool + "0123456789"
if use_special == 'y':
    pool = pool + "!@#$%^&*()"

password = ""
# Loop chala kar random characters select karna
for i in range(length):
    password = password + random.choice(pool)

print("Generated Password:", password)