# -*- coding: utf-8 -*-
import sys, select, os
from servant import Servant
from player import Player

# Create the new players
player_one = Player("sidney")
player_two = Player("yassine")

# Create the servants
dieudonne = Servant("Dieudonne", "42", "80", "100")
taubira = Servant("Taubira", "30", "70", "80")

# Set the servants inside an array
servants = [dieudonne, taubira]

# Initialize variables
current_player = player_two
current_opponent = player_one
turn_count = 0
timer = 10
history = ""

#print("First Servant:", dieudonne.name, dieudonne.health_point, dieudonne.attack_point, dieudonne.mana_cost)
#print("Second Servant:", taubira.name, taubira.health_point, taubira.attack_point, taubira.mana_cost)

while(current_player.health_point != 0):
  if (current_player == player_one):
    current_player = player_two
    current_opponent = player_one
  else:
    current_player = player_one
    current_opponent = player_two
  print("----------------- TURN " + str(turn_count) + " -----------------\n\n")
  print(str(current_player.name) +"'s turn. You have " + str(timer) + " seconds! Choose a card between:")
  # Print every servant card in player's hand
  for servant in servants:
    print("------->" + str(servant.name))
  print('\n')
  print("What is your choice?")

  i, o, e = select.select( [sys.stdin], [], [], timer )

  # If inputed answer is in the player's hand 
  if (i):
    turn_count+=1
    os.system('cls' if os.name == 'nt' else 'clear')
    history = history + str(current_opponent.name) + " chose " + sys.stdin.readline().strip() + "\n"
    print history
  else:
    # Stop the game if no answer. Turn's player lost the game
    print "You said nothing! " + str(current_player.name) + " lost this game!"
    sys.exit()
print(str(current_player.name) +" has lost this game !")