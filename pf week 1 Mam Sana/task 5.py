import math

a = float(input("a ki value: "))
b = float(input("b ki value: "))
c = float(input("c ki value: "))

# Discriminant formula
disc = (b**2) - (4*a*c)
print("Discriminant:", disc)

if disc == 0:
    print("Roots are real, equal and rational.")
    root = -b / (2*a)
    print("Root:", root)
elif disc > 0:
    print("Roots are real, distinct.")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    print("Roots are imaginary.")