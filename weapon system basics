# -*- coding: utf-8 -*-



from abc import ABC , abstractmethod

class weapon(ABC):
  @abstractmethod
  def attack (self):
          pass
class swoard(weapon):
  def attack(self):
    print("swosh..swosh")
class gun (weapon):
  def attack(self):
    print("trrrrrrrr")
class bow(weapon):
  def attack(self):
    print("thiwp")
class magicwand(weapon):
  def attack(self):
    print("expecto patronum")

class player():
  def __init__(self,weapon):
    self.weapon = weapon
  def use_weapon(self):
    self.weapon.attack()

# Objects b
s = swoard()
g = gun()
b = bow()
m = magicwand()


p1 = player(s)
p1.use_weapon() # Output


p1.weapon = g
p1.use_weapon() #
