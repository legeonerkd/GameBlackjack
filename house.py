 Дом

#TODO: Блок
class Brick:
  # attributes (properties) - the state of objects
  # methods - functions, objects' behavior 

  def build(self):
    return '#'
  
  # __init__ is a constructor (special function to create objects)
  
# PEP 8

# TODO Крыша
class Roof:
  def __init__(self, height):
    self.height = height
    
  def build(self):
    print(' ' * (self.height - 1)  + Brick().build())
    after = 1
    for before in range(self.height - 2, -1, -1):
      print(' ' * before + Brick().build() + (' ' * after) + Brick().build())
      after += 2
      
    # print(self.height)
  
  
#TODO: Стена
class Wall:
  def __init__(self, height, distance):
    self.height = height
    self.distance = distance
    
  def build(self):
    for _ in range(self.height):
      print(Brick().build() + ' ' * self.distance + Brick().build())


class House:
  def __init__(self, roof_height, wall_height):
    self.roof_height = roof_height
    self.wall_height = wall_height

  def build(self):
    roof = Roof(self.roof_height)
    wall = Wall(self.wall_height, 1 + 2 * (self.roof_height - 2))

    roof.build()
    wall.build()


    


# brick = Brick()

# syntax, call - вызов
# call the build function to build a brick

# omitted - опущенный
# object.action(object, arguments)
# brick.build()

# Brick().build()
# Roof(10).build()

house = House(wall_height=10, roof_height=20)


house.build()