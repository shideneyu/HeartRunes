import pygame
import random
from player import Player
from ground import Ground

class Game:
    def __init__(self):
        self.terrains = {}
        self.players = {}
        self.continueGame = True
        self.playerList = {0:'ump',1:'fn', 2:'ps', 3:'communistes'}
        self.tour = 0

    #Combat de deux cartes entre elles
    def  attackCard(self, card0, card1):

        print(card.name + "lance une attaque sur " +card1.name)
        if(card1.power > card2.defense):
            difference = card1.power - card2.defense
            difference = difference/10
            print(card.name + " inflige" +difference +" de dégats")
            winCard = card1
            loseCard = card2
            winner = player1
        else:
            winCard = card2
            loseCard = card1
            winner = player2
        #
        loseCard.popularity = winCard.power - loseCard.defense
        winner.popularity += 2

    # Create the new players
    def setPlayers(self,i,player):

        if i==0:
            player1 = player
            if player1 in self.playerList:
                self.players[i] = Player(self.playerList[player1])
                print("\n ----> Joueur 1, vous avez choisi : " +self.players[i].name + "\n")
            else:
                print("Il faut choisir parmis les personnages existants" + player1)
        #

        if i==1:
            player2= player
            if player2  in self.playerList:
                self.players[i] = Player(self.playerList[player2])
                print("\n ----> Joueur 2, vous avez choisi:" + self.players[i].name + "\n")
            else:
                print("Il faut choisir parmis les personnages existants")
        #
    #
    def showPlayersAvaible(self):
        for x in range(len (self.playerList)):
            current = self.playerList[x]
            print (str(x)+" -- " +str(current))

    #Show scores
    def showScores(self,fenetre):
        x=1
        label ={}
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        yellow = (255, 255, 0)
        for x in range(len(self.players)):
            currentPlayer = self.players[x]
            label[x] = myfont.render(currentPlayer.name + ":" +str(currentPlayer.popularity) +"%", 1, yellow)
        #
        fenetre.blit(label[0], (350,10))
        fenetre.blit(label[1], (350,510))
        pygame.display.update(0, 0, 800, 600)

    #
    def startGame(self):
        # Tour par tour
        while(self.continueGame == True):
            currentPlayer = self.tour % 2
            player = self.players[currentPlayer]

            #Quand les deux ont joues on invoque un nouveau terrain
            if( ( self.tour % 2 ) == 0):
                ground = Ground()
                ground.groundAction(self.players)

            #
            print("\n\n- Tour " + str(self.tour) + " -----------------\n")
            print("Votre popularite actuelle : " + str(player.popularity) +"%")
            print("Hey "+player.name+ ", a ton tour, voici ta main -------\n")
            player.hand.pickCard(player.deck.getCard())
            player.hand.getHand()

            card = int( input("Quel carte compte tu jouer ? ") )
            if ( card >= 0 ):
                cardName =  player.hand.getCard(card)
                print("Vous avez jouer " + cardName.name )
                player.playCard( card )
            else:
                print("Vous n'avez jouer aucune carte ")

            #ICI LES ATTAQUESSSSSSS
            if( self.tour > 1):
                print("\n\n\n###### ATTAQUE : Voici vos cartes et celles de votre adversaire actuellement en jeu.")
                print("\n### Vous ")
                player.getCardsOnGame();
                tmp = ((self.tour+1) % 2 )
                playerO = self.players[tmp]
                print("\n### Adversaire")
                playerO.getCardsOnGame();
                card0 = input("Avec quelle carte souhaite tu attaquer ? ")
                print("\n\n\n")
                playerO.getCardsOnGame();
                card1 = input("Quelle carte souhaite tu attaquer ? ")

                self.attackCard(player.hand.getCard(card0), player.hand.getCard(card1))

                if (player.popularity >= 100 or player.popularity <= 0):
                    self.continueGame = False
            #Next
            self.tour += 1
