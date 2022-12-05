import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    self.area = self.width * self.height
    return self.area
  def get_perimeter(self):
    self.perimeter = (2 * self.height) + (2 * self.width)
    return self.perimeter
  def get_diagonal(self):
    self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return self.diagonal
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*" * self.width + "\n"
    return picture
    # looping through height with the stars from the width
  def get_amount_inside(self, shape):
    total = shape.get_area()
    area = self.get_area()
    num = area / total
    num = math.floor(num)
    # floor rounding down tool imported from math library
    return num
    # creating various methods
      
  def __str__(self):
    statement = "Rectangle(width={}, height={})".format(self.width, self.height)
    return statement
    # method defining what is printed when object is in a print statement
  
class Square(Rectangle):
  def __init__(self, side):
    self.side = side
    self.width = self.side
    self.height = self.side
  def set_side(self, side):
    self.side = side
    self.set_width(side)
    self.set_height(side)
  def set_width(self, width):
    self.width = width
    self.height = self.width
    self.side = self.width
    # variables declared rather than using other method as recursion loop created otherwise
  def set_height(self, height):
    self.height = height
    self.width = self.height
    self.side = self.height
  # creating various methods
  def __str__(self):
    statement = "Square(side={})".format(self.side)
    return statement
  # method defining what is printed when object is in a print statement