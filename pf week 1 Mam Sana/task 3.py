n = int(input("Number likhein: "))

original = n
r = 0

# Number ko ulta (reverse) karne ka loop
while n > 0:
    rem = n % 10
    r = (r * 10) + rem
    n = n // 10

if original == r:
    print("Yes, Palindrome hai!")
else:
    print("No, Palindrome nahi hai!")