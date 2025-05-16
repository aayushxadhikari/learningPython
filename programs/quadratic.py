import math

a = float(input("Enter any first number:"))
b = float(input("Enter any second number:"))
c = float(input("Enter any third number:"))

discriminant = (b**2) -(4*a*c)

if a == 0:
    print("This is not a quadratic equation.")
else:
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)/(2*a))
        root2 = (-b - math.sqrt(discriminant)/(2*a))
        print(root1,root2)
    elif discriminant == 0:
        r = (-b +math.sqrt(discriminant))/(2*a)
        print(r)
    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(-discriminant)/(2*a)
        print(f"Two complex roots : {real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i")