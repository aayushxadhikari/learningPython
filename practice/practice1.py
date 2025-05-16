a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a == b == c:
    print("All are equal.")
elif a >= b and a >= c:
    print("a is the greatest number")
elif b >= a and b >= c:
    print("b is the greatest number")
else:
    print("c is the greatest number")
