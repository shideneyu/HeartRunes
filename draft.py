class Stack
  private cards
end

class Turn
  current_player.
end

class BattePlace
  private servants
end

class Servant
  private status
end

class Player
  private popularity_point
  private health_point
  private cards

  def constructor(popularity_point, health_point, cards)
  end
end




      if os.name != "nt":
            timeout = 10
            print("What is your choice?\n")
            record, _, _ = select([ sys.stdin], [], [], timeout)
            if record:
                process_choice(sys.stdin.readline().rstrip(), servants)
            else:
                game_loss()
            #
        else:
            record = windowsTimeout("What is your choice?\n", 10 )
            if record:
                process_choice(sys.stdin.readline().rstrip(), servants)
            else:
                game_loss()

                print(currentPlayer.name +" has lost this game !")


# Timeout for windows only
def windowsTimeout( caption, default, timeout = 15):
    start_time = time.time()
    sys.stdout.write('%s(%s):'%(caption, default));
    input = ''
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getche()
            if ord(chr) == 13:
                break
            elif ord(chr) >= 32:
                input += chr
                if len(input) == 0 and (time.time() - start_time) > timeout:
                    break

                    if len(input) > 0:
                        return input
                    else:
                        return default

# Set those variable as global, or it won't work.
def process_choice(record, servants):
    global turn_count
    global history
    if (record in list(map(lambda x: x.name, servants))):
        servants = [servant for servant in servants if servant.name != record]
        turn_count+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        history = history + current_opponent.name + " chose " + record + "\n"
        print(history)
    else:
        game_loss()
