from deck import Deck

class Player:
  def __init__(self, name, health = 100, mana = 100):
    self.name = name
    self.health = health
    self.mana = mana
    self.deck = Deck() #Full Deck
    self.hand = Hand() #Empty list of Card
    for x in range(5):
      self.hand.addCard(self.deck.draw())

    #Add nb health and return player health
    def addHealth(self, nb = 1):
      self.health += nb
      return self.health

    #Remove nb health and return player health
    def removeHealth(self, nb = 1):
      self.health -= nb
      return self.health

    def drawFromDeck(self):
      return self.deck.draw()

    def drawFromHand(self):
      return self.hand.draw
