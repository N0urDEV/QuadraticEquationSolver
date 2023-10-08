import math
def solve_quadratic_equation():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    discriminant = (b * b) - (4 * a * c)

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two real solutions: x1 =", x1, "and x2 =", x2)
    elif discriminant == 0:
        x1 = -b / (2 * a)
        print("One real solution: x1 =", x1)
    else:
        print("No real solution")
solve_quadratic_equation()
