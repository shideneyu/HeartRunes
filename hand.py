class Hand:
    def __init__( self, deck ):
        self.cardsHand = []
        self.deck = deck
        #new Hand
        for x in range(5):
            self.cardsHand.insert( 0, deck.getCard() )
    #
    def count(self):
        return len( self.cardsHand )

    #
    def pickCard( self, card ):
        self.cardsHand.append(self.deck.getCard())
        return self.cardsHand

    #
    def playCard( self, card ):
        tmp = self.cardsHand[card]
        self.cardsHand.pop(card)
        return tmp

    #
    def draw(self):
        return self.cardsHand.pop()

    #
    def getHand( self ):
        print ("ID | CS | NOM \t\t| ATTAQUE \t| PUISSANCE \t| DEFENSE")
        for x in range( len ( self.cardsHand ) ):
            current = self.cardsHand[ x ]
            if(current.type == "1"):
                print ( str(x)+"  | x | "+current.name+" \t| " +current.attack + " \t| " + current.power+ " \t| " +current.defense )
            else:
                print ( str(x) + "  |    | " +current.name +" \t| " +current.attack + " \t| " + current.power+ " \t| " +current.defense )
