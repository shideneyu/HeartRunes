class Hand:
    def __init__( self, deck ):
        self.cardsHand = {}
        #new Hand
        for x in range(5):
            self.cardsHand[ x ] = deck.getCard()

    #
    def pickCard(self, name):
        for card in self.cardsHand:
            if card.name == name:
                servant = card
                self.cardsHand.remove(card)
                return servant
    #
    def count(self):
        return len( self.cardsHand )

    #
    def addCard( self, card ):
        self.cardsHand.apppend( card )
        return self.cardsHand
    #
    def draw(self):
        return self.cardsHand.pop()
    #
    def getHand( self ):
        for x in range( len ( self.cardsHand ) ):
          current = self.cardsHand[ x ]
          if( current.type == "1"):
              print (  "CS  - nom : " +current.name +" - Attack : " +current.attack + " - Puissance " + current.power+ " - Defense" +current.defense )
          else:
              print ( current.name +" - Attack : " +current.attack + " - Puissance " + current.power+ " - Defense" +current.defense )
