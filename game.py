# -*- coding: utf8 -*-
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
        self.Winner = 0 #Si le dernier joueur a gagner ou non.
        self.Loser = 0 #Si le dernier joueur a gagner ou non.
        self.nameGameOver = False #le nom du dernier joueur

    #Combat de deux cartes entre elles
    def  attackCard(self, currentPlayer, card0, card1):

        player = self.players[currentPlayer]
        tmp = ((self.tour+1) % 2 )
        playerO = self.players[tmp]

        print(card0.name + "lance une attaque sur " +card1.name)
        difference = card0.power - card1.defense
        difference = difference/10
        if(card0.power > card1.defense):
            print(card0.name + " inflige" +str(difference)+" de dégats")
            winCard = card0
            loseCard = card1
            winner = player
            loser = playerO
        else:
            print(card0.name + " s'est attaque a plus fort que lui ! Il a perdu " +str(difference)+" de dégats")
            winCard = card1
            loseCard = card0
            winner = playerO
            loser = player
        #
        loser.deleteCardFromGame(loseCard)
        winner.popularity += difference/2
        loser.popularity -= int(difference)
        loseCard.popularity = int(card0.power) - int(card1.defense)

    # Create the new players
    def setPlayers(self,i,player):
        if i == 0:
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
        myfont = pygame.font.SysFont("Arial", 30)
        yellow = (0, 0, 0)
        for x in range(len(self.players)):
            currentPlayer = self.players[x]
            label[x] = myfont.render(currentPlayer.name + ":" +str(currentPlayer.popularity) +"%", 1, yellow)
        #
        fenetre.blit(label[0], (350,10))
        fenetre.blit(label[1], (350,510))
        pygame.display.update(0, 0, 900, 600)

    #Show scores
    def updateScore(self):
        print("\n\n ---------------- ESTIMATIONS IPSOS ---------------------------\n")
        for x in range(len(self.players)):
            currentPlayer = self.players[x]
            print(currentPlayer.name + ":" +str(currentPlayer.popularity) +"%")
        #
        print("\n ------------------------------------------------------------------\n\n")
        """myfont = pygame.font.SysFont("Arial", 30)
        yellow = (0, 0, 0)
        currentPlayer = self.players[player]
        label[player] = myfont.render(currentPlayer.name + ":" +str(currentPlayer.popularity) +"%", 1, yellow)
        #
        if(player == 0):
            fenetre.blit(label[player], (350,10))
        else:
            fenetre.blit(label[player], (350,510))
            #
            pygame.display.update(0, 0, 900, 600)"""

    #
    def startGame(self,fenetre):
        ground = Ground()
        # Tour par tour
        yellow = (0, 0, 0)
        while(self.continueGame == True):
            self.updateScore()
            currentPlayer = self.tour % 2
            player = self.players[currentPlayer]
            myfont = pygame.font.SysFont("Arial", 35)
            labelTour = myfont.render(" Tour :" +str(self.tour), 2, yellow)
            fenetre.blit(labelTour, (600,250))
            pygame.display.update(0, 0, 800, 600)

            #Quand les deux ont joues on invoque un nouveau terrain
            if( ( self.tour % 2 ) == 0):
                ground.groundAction(self.players)

            #
            print("\n\n- Tour " + str(self.tour) + " -----------------\n")
            print("Hey "+player.name+ ", a ton tour, voici ta main -------\n")
            player.hand.pickCard(player.deck.getCard())
            player.hand.getHand()

            card = int( input("Quel carte compte tu jouer ? ") )
            if ( card >= 0 ):
                cardName =  player.hand.getCard(card)
                print("Vous avez jouer " + cardName.name )
                player.playCard(card)
            else:
                print("Vous n'avez jouer aucune carte ")

            #ICI LES ATTAQUESSSSSSS
            if( self.tour >= 1):
                print("\n\n###### ATTAQUE : Voici vos cartes et celles de votre adversaire actuellement en jeu.")
                print("\n### Vous ")
                player.getCardsOnGame();
                tmp = ((self.tour+1) % 2 )
                playerO = self.players[tmp]

                #Aucun adversaire, le joueur perd 5 point direct
                if ( playerO.noCardOnGame() == True ):
                    playerO.popularity -= 5
                    player.popularity += 3
                    playerO.getCardsOnGame()
                    print("\n\n ---****************  MANQUE DES CARTES CHEZ LE VOISIN **************** \n\n")
                else:
                    card0 = input("Avec quelle carte souhaite tu attaquer ? ")
                    card0 = player.getCard(int(card0))
                    if(card0.type == 1):
                        print("il s'agit d'une carte special")
                    #
                    print("\n### Adversaire")
                    playerO.getCardsOnGame();
                    print("\n\n\n")
                    card1 = input("Quelle carte souhaite tu attaquer ? ")

                    self.attackCard(currentPlayer, card0, playerO.getCard(int(card1)))

                    if (player.popularity >= 100 ):
                        self.Winner = player
                        self.Loser =  playerO
                        self.continueGame = False
                #
                if (player.popularity <= 0):
                    self.Winner =  playerO
                    self.Loser =  player
                    self.continueGame = False

            #Next
            self.tour += 1
        #Winning game
        label = []
        myfont = pygame.font.SysFont("Arial", 60)
        rouge = (210,2,2)
        green = (0,128,0)
        label.append(myfont.render("Vainqueur :" +str(self.Winner.name), 2, green))
        label.append(myfont.render("Vainqueur :" +str(self.Loser.name), 2, red))
        fenetre.blit(label[0], (350,120))
        fenetre.blit(label[1], (350,300))
        pygame.display.update(0, 0, 800, 600)
