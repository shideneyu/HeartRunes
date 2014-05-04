from servant import Servant
from player import Player

player_one = Player("sidney")
player_two = Player("yassine")

dieudonne = Servant("Dieudonne", "42", "80", "100")

print("First Servant:", dieudonne.name, dieudonne.health_point, dieudonne.attack_point, dieudonne.mana_cost)
print("Player One:", player_one.name)
print("Player Two:", player_two.name)
