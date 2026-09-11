import math

target = float(input("Enter the amount you want for the downpayment: "))
r = float(input("Enter the annual interest rate (as a decimal): "))

k = 12
n = 24 * k

d = target / (((1 + r / k) ** n - 1) / (r / k))

print("You need to deposit", d, "each month.")

