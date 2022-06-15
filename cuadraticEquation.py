from cmath import sqrt
import math
def cuadratic_equation(a,b,c):
    xp = (-b + sqrt((b**2) - (4*a*c)))/ (2*a)
    xm = (-b - sqrt((b**2) - (4*a*c)))/ (2*a)
    print(f'The result of the cuadratic equation {a}x^2 + {b}x +{c} is: {xp} , {xm}')

while (True):
    print('Script for the solution of a cuadratic equation. Press "s" to stop.')
    a = float(input('Enter the first coeficient of the equation (a): '))
    b = float(input('Enter the second coeficient of the equation (b): '))
    c = float(input('Enter the third coeficient of the equation (c): '))
    if a and b and c == True:
        result = cuadratic_equation(a,b,c)
    elif a or b or c == 's':
        break
    else:
        print('Enter a valid number.')