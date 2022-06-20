class rectangle:
  def __init__(self, _height, _base):
    self.height = _height
    self.base = _base
   
  def calculate_area(self):
    area = self.height * self.base
    print(f'The area for the rectangle, result of multiply his base {self.height} by his height {self.base} is: {area}')

loop = True
while loop == True:
    height = input("Input rectangle height: ")
    base = input("Input rectangle base: ")
    if height.isnumeric() and base.isnumeric():
        r1 = rectangle(int(height),int(base))
        r1.calculate_area()
        cont = input("Type E if you want to exit, else type any other letter: ")
        if cont == "E" or cont == "e":
            loop = False
    else:
        print("Enter numbers")