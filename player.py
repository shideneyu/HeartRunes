from deck import Deck
from hand import Hand
#class player
class Player:

  def __init__(self, name, popularity = 50 ):
    self.name = name
    self.popularity = popularity
    self.deck = Deck( self )
    self.hand = Hand ( self.deck )
    self.cardsInGame = []

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
  def getCard(self, card):
    return self.cardsInGame[card]
  #
  def playCard(self, card):
    if (len(self.cardsInGame)<3):
      self.cardsInGame.append(self.hand.playCard( card ))
    else:
      print("ATTENTION : Pas plus de 3 cartes sur votre plateau, vous ne pouvez pas en rajouter")
  #
  def deleteCardFromGame(self, card):
    if card in  self.cardsInGame:  self.cardsInGame.remove(card)
  #
  def getCardsOnGame(self):
    print ("ID | NOM \t\t| ATTAQUE \t| DEFENSE")
    i = 0
    for current in self.cardsInGame:
      print ( str(i) + "  | " +current.name +" \t| " +str(current.power) + " \t| " +str(current.defense) )
      i +=1
  #
  def getHand(self):
    return self.getCard()
