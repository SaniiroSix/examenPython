import math

loop = True
while loop == True:
    a = input("Please enter variable a: ")
    b = input("Please enter variable b: ")
    c = input("Please enter variable c: ")

    if a.isnumeric() == False or b.isnumeric() == False or c.isnumeric() == False:
        print("Wrong Value")
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        x1 = (((-b)+(math.sqrt(b**2)-(4*a*c)))/(2*a))
        x2 = (((-b)-(math.sqrt(b**2)-(4*a*c)))/(2*a))
        print("x1: ",x1)
        print("x2: ",x2)
        cont = input("Type E if you want to exit, else type any other letter: ")
        if cont == "E" or cont == "e":
            loop = False