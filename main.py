# -*- coding: utf-8 -*-

import sys, select, os
from game import Game
# Usefull for timer
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
