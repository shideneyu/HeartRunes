import pygame
from pygame.locals import *
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

    def getHandGraphic(self,Fenetre):
        i = 0
        tabcard=[]
        card = pygame.image.load("images/placecard.png").convert()
        myfont = pygame.font.SysFont("Arial", 18)
        yellow = (0, 0, 0)
        label=[]
        for current in self.cardsHand:

            #if(current.type == "1"):
            label.append(myfont.render(current.name, 1, yellow))
            tabcard.append(card)
            Fenetre.blit(label[i], ((i*200)+50,500))
            Fenetre.blit(tabcard[i], ((i*200)+10,550))

            #else:
            label.append(myfont.render(current.name, 1, yellow))
            tabcard.append(card)
            Fenetre.blit(label[i], ((i*200)+50,500))
            Fenetre.blit(tabcard[i], ((i*200)+10,550))

            #
            i +=1