from cmath import sqrt
import math
def cuadratic_equation(a,b,c):
    
    x = (-b - sqrt((b**2) - (4*a*c)))/ (2*a)
    y = (-b + sqrt((b**2) - (4*a*c)))/ (2*a)
    print(f'Resultado de la ecuación {a}x^2 + {b}x +{c} is: {x} , {y}')

while (True):
    print('Script solucion de la ecuacion. Ingresa "A" para detener.')
    a = float(input('Ingresa el primer Coeficiente (a): '))
    b = float(input('Ingresa el segundo Coeficiente (b): '))
    c = float(input('Ingresa el tercer Coeficiente (c): '))
    if a and b and c == True:
        result = cuadratic_equation(a,b,c)
    elif a or b or c == 'A':
        break
    else:
        print('ingresa un valor valido.')