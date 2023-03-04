import math
a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))
# Calculate discriminant
discriminant = b**2 - 4*a*c
if discriminant > 0:
 # Two real roots
 root1 = (-b + math.sqrt(discriminant)) / (2*a)
 root2 = (-b - math.sqrt(discriminant)) / (2*a)
 print("The roots are", root1, "and", root2)
elif discriminant == 0:
 # One real root
 root = -b / (2*a)
 print("The root is", root)
else:
 # Two complex roots
 real_part = -b / (2*a)
 imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
 print("The roots are", real_part, "+", imaginary_part, "i and", real_part, "-", imaginary_part, "i")
