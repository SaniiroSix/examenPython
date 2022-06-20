loop = True
while loop == True:
    NumberVal = input("Please enter a numeric value between 1 and 10: ")
    if NumberVal.isnumeric() == False or int(NumberVal) > 10:
        print("Wrong Value")
    else:
        NumberVal = int(NumberVal)
        if NumberVal == 9 or NumberVal == 10:
            print("A")
        elif NumberVal == 8:
            print("B") 
        elif NumberVal == 7:
            print("C")
        elif NumberVal == 6:
            print("D")
        else:
            print("F")
        cont = input("Type E if you want to exit, else type any other letter: ")
        if cont == "E" or cont == "e":
            loop = False
          

