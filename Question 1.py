import math

P0 = float(input("Enter the initial investment: "))
t = float(input("Enter the length of the investment in years: "))
r = float(input("Enter the annual interest rate (as a decimal): "))

Pt = P0 * math.exp(r * t)

print("The value of the investment after", t, "years is", Pt)
