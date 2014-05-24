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
  print(current_player.name +"'s turn. You have " + str(timer) + " seconds! Choose a card between:")
  # Print every servant card in player's hand
  for servant_name in list(map(lambda x: x.name, servants)):
    print("------->" + servant_name)
  print('\n')
  record = input("What is your choice?\n")

  # If inputed answer is in the player's hand 
  if (record in list(map(lambda x: x.name, servants))):
    servants = [servant for servant in servants if servant.name != record]
    turn_count+=1
    os.system('cls' if os.name == 'nt' else 'clear')
    history = history + current_opponent.name + " chose " + record + "\n"
    print(history)
  else:
    # Stop the game if no answer. Turn's player lost the game
    print("You said nothing! " + current_player.name + " lost this game!")
    sys.exit()
print(current_player.name +" has lost this game !")
