class Hand:
    def __init__( self, deck ):
        self.cardsHand = []
        self.deck = deck
        #new Hand
        for x in range(3):
            self.cardsHand.append(deck.getCard())

    #
    def count(self):
        return len( self.cardsHand )

    #
    def pickCard( self, card ):
        self.cardsHand.append(self.deck.getCard())
        return self.cardsHand

    #
    def getCard( self, card ):
        return self.cardsHand[card]

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
        print ("ID | CS | NOM \t\t| ATTAQUE \t| DEFENSE")
        i = 0
        for current in self.cardsHand:
            if(current.type == "1"):
                print ( str(i)+"  | x | "+current.name+" \t| " +str(current.power)  + " \t| " +str(current.defense) )
            else:
                print ( str(i) + "  |    | " +current.name +" \t| " +str(current.power ) + " \t| " +str(current.defense) )
            #
            i +=1
