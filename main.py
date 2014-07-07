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
players = {1: 'yassine', 2: 'sidney'}

playerOne = Player( players[1] )
playerTwo = Player( players[2] )
# Set the servants inside an array

# Initialize variables
current_player = playerOne
current_opponent = playerTwo
turn_count = 0
timer = 15
history = ""

# Stop the game if incorrect answer
def game_loss():
  print("Incorrect! " + current_player.name + " lost this game!")
  sys.exit()

# Timeout for windows only
def windowsTimeout( caption, default, timeout = 15):
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

  if len(input) > 0:
      return input
  else:
      return default


def process_choice(record, servants):
  # Set those variable as global, or it won't work.
  global turn_count
  global history
  if (record in list(map(lambda x: x.name, servants))):
    servants = [servant for servant in servants if servant.name != record]
    turn_count+=1
    os.system('cls' if os.name == 'nt' else 'clear')
    history = history + current_opponent.name + " chose " + record + "\n"
    print(history)
  else:
    # Stop the game if no answer. Turn's player lost the game
    game_loss()

# Points de vies
while(current_player.health != 0 or current_player.health >= 100 ):
  if (current_player == playerOne):
    current_player = playerTwo
    current_opponent = playerOne
  else:
    current_player = playerOne
    current_opponent = playerTwo
  print("----------------- TURN " + str( turn_count ) + " -----------------\n")
  print("Hey " + current_player.name+ ", a ton tour  -------\n")
  print("Voici ta main \n")
  current_player.hand.getHand ()
  print("Hey " + current_player.name+ ", a ton tour  -------\n")

  print("Terrain \n")
  # Print every servant card in player's hand

  # Timer for linux/mac
  if os.name != "nt":
    timeout = 10
    print("What is your choice?\n")
    record, _, _ = select([ sys.stdin], [], [], timeout)
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
