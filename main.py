import math

def licz_sume_pol(shapes):
    sum = 0
    for shape in shapes:
        if len(shape) == 1:
            square = math.pi * shape[0]**2
        elif len(shape) == 2:
            square = shape[0] * shape[1]
        elif len(shape) == 3:
            a = shape[0]
            b = shape[1]
            c = shape[2]
            p = (a+b+c)/2
            square = math.sqrt(p*(p-a)*(p-b)*(p-c))
        else:
            return("„Błąd: można podać maksymalnie 3 liczby")
        sum += square
    return round(sum, 1)

n = int(input())
shapes = []

for i in range(n):
    str = input()
    tab = str.split()
    tab = [float(x) for x in tab]
    shapes.append(tab)

print(licz_sume_pol(shapes))

