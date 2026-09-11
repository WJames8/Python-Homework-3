import math

d = float(input("Enter the amount deposited each month: "))
r = float(input("Enter the annual interest rate (as a decimal): "))
k = 12

P24 = d * (((1 + r / k) ** (24 * k) - 1) / (r / k))

print("The final balance after two years is", P24)

