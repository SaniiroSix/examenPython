import math
from operator import is_not 
class Rectangle():
    def rectangle_area(b,h):
        a = b*h
        print(f"The area forthe recangle, result of multiply his base {b} by his height {h} is: {a}")
        
while(True):
    print('Press "s" to stop.')
    x = float(input('Type the base of the rectangle: '))
    y = float(input('Type the height of the rectangle: '))
    area    = Rectangle.rectangle_area(x,y)

