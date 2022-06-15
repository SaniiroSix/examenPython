def is_float(s):
    try:
        s = float(s)
        return True
    except:
        return False

while(True):
    x = input("Enter the calification from 1-10: ") 
    validNumber = is_float(x)
    if validNumber == True:
        c = float(x)
        if 9 <= c <= 10:
            print("The calification is 'A' ")
        if 8 <= c <= 8.9:
            print("The calification is 'B' ")
        if 7 <= c <= 7.9:
            print("The calification is 'C' ")
        if 6 <= c <= 6.9:
            print("The calification is 'D' ")
        if 6 > c:
            print("The calification is 'F' ")
        else:
            print('Enter a valid value from 1-10')
    else: 
        print("Enter a valid number between 1-10.")



