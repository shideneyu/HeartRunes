class Hand:
    def __init__( self, deck ):
        self.cardsHand = {}
        #new Hand
        for x in range(5):
            self.cardsHand[ x ] = deck.getCard()
    #
    def count(self):
        return len( self.cardsHand )

    #
    def pickCard( self, card ):
        self.cardsHand.insert( 0, card )
        return self.cardsHand

    #
    def draw(self):
        return self.cardsHand.pop()

    #
    def getHand( self ):
        print ("ID | CS | NOM \t\t| ATTAQUE \t| PUISSANCE \t| DEFENSE")
        for x in range( len ( self.cardsHand ) ):
            current = self.cardsHand[ x ]
            if(current.type == "1"):
                print ( str(x)+"  | Oui | "+current.name+" \t| " +current.attack + " \t| " + current.power+ " \t| " +current.defense )
            else:
                print ( str(x) + "  |    | " +current.name +" \t| " +current.attack + " \t| " + current.power+ " \t| " +current.defense )
