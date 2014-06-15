import random
from servant import Servant

class Deck:
  #Servant(self, name, health_point, attack_point, mana_cost)
  
  def __init__(self):
    self.listServant = [
      Servant("a", 2, 1, 1),
      Servant("b", 5, 2, 3),
      Servant("c", 7, 3, 2),
      Servant("d", 1, 2, 1),
      Servant("e", 10, 1, 2),
      Servant("f", 1, 2, 3),
      Servant("g", 4, 9, 2),
      Servant("h", 10, 1, 1),
      Servant("i", 4, 2, 2),
      Servant("j", 1, 1, 3)]
    random.shuffle(self.listServant)

  #Return the last card of the deck and remove it
  def draw(self):
    return self.listServant.pop()
  
  def count(self):
    return len(self.listServant)

  #def __repr__(self):
     #return "[LIST DECK]: " + str(self.count())

    
