start = int(input("Start range: "))
end = int(input("End range: "))

prime_sum = 0
print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        # Check karne ke liye ke number kisi aur se divide toh nahi hota
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        # Agar prime hai toh print karein aur sum mein add karein
        if is_prime:
            print(num, end=" ")
            prime_sum = prime_sum + num

print("\nSum of prime numbers:", prime_sum)