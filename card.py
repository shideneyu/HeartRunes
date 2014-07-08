import random
from servant import Servant

class Card:
  def __init__( self, data):
    #self.player = player
    self.id = id
    self.name = data["name"]
    self.popularity = data["popularity"]
    self.attack = data["attack"]
    self.power = data["power"]
    self.defense = data["defense"]
    self.type = data["type"]
    #self.bestTheme = data.bestTheme
