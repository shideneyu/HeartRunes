from deck import Deck
from hand import Hand
from card import Card

class Player:
  def __init__(self, name, popularity = 50 ):
    self.name = name
    self.popularity = popularity
    self.deck = Deck( self )
    self.hand = Hand ( self.deck )
    self.cardsInGame = []

  #Add nb health and return player health
  def addHealth(self, nb = 1):
    self.health += nb
    return self.health
  #
  def drawFromDeck(self):
    return self.deck.draw()
  #
  def drawFromHand(self):
    return self.hand.draw
  #
  def getCard(self):
    self.listHand.apppend(self.deck.getCard())
  #
  def playCard(self, card):
    self.cardsInGame.append(self.hand.playCard( card ))

  #
  def getCardsOnGame(self):
    print ("ID | NOM \t\t| ATTAQUE \t| PUISSANCE \t| DEFENSE")
    i = 0
    for current in self.cardsInGame:
      print ( str(i) + "  | " +current.name +" \t| " +current.attack + " \t| " +current.defense )
      i +=1

  #
  def getHand(self):
    return self.getCard()
