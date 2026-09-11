import math

P0 = float(input("Enter the amount you want to borrow: "))
r = float(input("Enter the annual interest rate (as a decimal): "))
N = int(input("Enter the term of the loan in years: "))

k = 12

d = P0 / ((1 - (1 + r / k) ** (-N * k)) / (r / k))

print("Your monthly payment is", d)
