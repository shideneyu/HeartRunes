# -*- coding: utf-8 -*-
import sys, select, os
# If using windows, else using linux/mac
if os.name == 'nt':
  import msvcrt, time
else:
  from select import select
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

# Stop the game if incorrect answer
def game_loss():
  print("Incorrect! " + current_player.name + " lost this game!")
  sys.exit()

# Timeout for windows only
def windowsTimeout( caption, default, timeout = 5):
  start_time = time.time()
  sys.stdout.write('%s(%s):'%(caption, default));
  input = ''
  while True:
      if msvcrt.kbhit():
          chr = msvcrt.getche()
          if ord(chr) == 13: # enter_key
              break
          elif ord(chr) >= 32: #space_char
              input += chr
      if len(input) == 0 and (time.time() - start_time) > timeout:
          break

  print ''  # needed to move to next line
  if len(input) > 0:
      return input
  else:
      return default


def process_choice(record, servants):
  # Set those variable as global, or it won't work.
  global turn_count
  global history
  # If inputed answer is in the player's hand 
  if (record in list(map(lambda x: x.name, servants))):
    servants = [servant for servant in servants if servant.name != record]
    turn_count+=1
    os.system('cls' if os.name == 'nt' else 'clear')
    history = history + current_opponent.name + " chose " + record + "\n"
    print(history)
  else:
    # Stop the game if no answer. Turn's player lost the game
    game_loss()

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
  

  # Timer for linux/mac
  if os.name != "nt":
    timeout = 10
    print("What is your choice?\n")
    record, _, _ = select([sys.stdin], [], [], timeout)
    if record:
      process_choice(sys.stdin.readline().rstrip(), servants)
    else:
      game_loss()
  # Timer for windows
  else:
    record = windowsTimeout("What is your choice?\n", 10 )
    if record:
      process_choice(sys.stdin.readline().rstrip(), servants)
    else:
      game_loss()

print(current_player.name +" has lost this game !")
