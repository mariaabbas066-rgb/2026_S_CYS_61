import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

# Distance Formula
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", d)

# Point 1 ka Quadrant
if x1 > 0 and y1 > 0: print("Point 1: Quadrant 1")
if x1 < 0 and y1 > 0: print("Point 1: Quadrant 2")
if x1 < 0 and y1 < 0: print("Point 1: Quadrant 3")
if x1 > 0 and y1 < 0: print("Point 1: Quadrant 4")

# Point 2 ka Quadrant
if x2 > 0 and y2 > 0: print("Point 2: Quadrant 1")
if x2 < 0 and y2 > 0: print("Point 2: Quadrant 2")
if x2 < 0 and y2 < 0: print("Point 2: Quadrant 3")
if x2 > 0 and y2 < 0: print("Point 2: Quadrant 4")