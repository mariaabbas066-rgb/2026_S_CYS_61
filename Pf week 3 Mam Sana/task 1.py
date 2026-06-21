def fact(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f

n = int(input("enter n value: "))
r = int(input("enter r value: "))

# Formulas
permutation = fact(n) / fact(n - r)
combination = fact(n) / (fact(r) * fact(n - r))

print("Permutation:", permutation)
print("Combination:", combination)