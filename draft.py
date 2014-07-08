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
