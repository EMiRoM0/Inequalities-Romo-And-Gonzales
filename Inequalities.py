import math

def obcoefficient(term):
    return int(input(f"Write the coefficient of the {term} term: "))

def termtype():
    while True:
        x = int(input("Write 0 for a constant, 1 for x^1, or 2 for x^2: "))
        if x in (0, 1, 2):
            return x

def inequalitytype():
    inequality_types = {
        1: (">=", "Your choice is: >="),
        2: ("<=", "Your choice is: <="),
        3: (">", "Your choice is: >"),
        4: ("<", "Your choice is: <")
    }
    while True:
        type_of = int(input("Choose the type of inequality by entering the corresponding number: \n1. '>='\n2. '<='\n3. '>'\n4. '<' "))
        if type_of in inequality_types:
            return inequality_types[type_of]

def solvequadraticinequality():
    print("Solving a quadratic inequality\n")
    num_terms = int(input("How many numbers are in the first part of the inequality? "))

    constant = 0
    lineal = 0
    square = 0

    for i in range(num_terms):
        coef = obcoefficient(i + 1)
        x = termtype()
        if x == 0:
            constant += coef
        elif x == 1:
            lineal += coef
        elif x == 2:
            square += coef

    print(f"{square}x² + {lineal}x + {constant}")

    ineq_type, ineq_message = inequalitytype()
    print(ineq_message)

    num_terms = int(input("How many numbers are in the second part of the inequality? "))

    constant2 = 0
    lineal2 = 0
    square2 = 0

    for i in range(num_terms):
        coef = obcoefficient(i + 1)
        x = termtype()
        if x == 0:
            constant2 += coef
        elif x == 1:
            lineal2 += coef
        elif x == 2:
            square2 += coef

    print(f"{square2}x² + {lineal2}x + {constant2}")

    equation = f"{square}x² + {lineal}x + {constant} {ineq_type} {square2}x² + {lineal2}x + {constant2}"
    print("\nThe inequality is:", equation)

    a = square + (square2 * -1)
    b = lineal + (lineal2 * -1)
    c = constant + (constant2 * -1)
    print(f"{a}x² + {b}x + {c}")

    try:
        discriminant = pow(b, 2) - (4 * a * c)
        if discriminant < 0:
            raise ValueError
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)

        if x1 > x2:
            x1, x2 = x2, x1

        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

        if ineq_type == ">=":
            print("(-∞, " + str(x1) + "] U [" + str(x2) + ", ∞)")
        elif ineq_type == "<=":
            print("[ " + str(x1) + " , " + str(x2) + " ]")
        elif ineq_type == ">":
            print("(-∞, " + str(x1) + ") U (" + str(x2) + ", ∞)")
        elif ineq_type == "<":
            print("( " + str(x1) + " , " + str(x2) + " )")

    except ValueError:
        print("There is not a valid solution.")

solvequadraticinequality()
