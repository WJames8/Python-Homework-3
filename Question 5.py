import math

r = float(input("Enter the annual interest rate (as a decimal): "))
d = float(input("Enter the monthly payment you can afford: "))

k = 12

# 15 year mortgage
N = 15
P0_15 = d * ((1 - (1 + r / k) ** (-N * k)) / (r / k))

# 30 year mortgage
N = 30
P0_30 = d * ((1 - (1 + r / k) ** (-N * k)) / (r / k))

print("You can afford to borrow", P0_15, "for a 15-year mortgage.")
print("You can afford to borrow", P0_30, "for a 30-year mortgage.")
