# -*- coding: utf-8 -*-
import sys, select, os
# If using windows, else using linux/mac
if os.name == 'nt':
    import msvcrt, time
else:
    from select import select

#
from servant import Servant
from player import Player
from game import Game

# Initialize variables
turn_count = 0
timer = 15
history = ""

#Message d'accueil
print ("-----* Bienvenue *-----\n")
print ("Les regles de ce jeu sont simples, le premier atteignant 100%% de popularite Gagne ! ")
print ("Attention, si vous retombez a 0%% vous serez alors elimines\n")
print (" -----*                    *-----\n")

game = Game()
game.setPlayers()
game.showScores()
game.startGame()
 #current_player = playerOne
#current_opponent = playerTwo

# Stop the game if incorrect answer
def game_loss():
    print ("Incorrect! " + current_player.name + " lost this game!")
    sys.exit()


