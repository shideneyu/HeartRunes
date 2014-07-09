import csv, random
from player import Player

class Ground:
	def __init__(self):
		self.themes = {}
		with open('datas/themes.csv', 'r') as f:
			reader = csv.DictReader(f, delimiter=',')
			for line in reader:
				self.themes[line["id"]] = {'type':line["type"],'name':line["name"],'description':line["description"],'bonus':line["bonus"],'malus':line["malus"]}

	def groundAction(self, players):
		randomIntTheme = random.randint(1, 5) #Five themes
		randomBits = random.getrandbits(1)
		randomInt = random.randint(1, 5)
		theme = self.themes[str(randomIntTheme)]
		type = int(theme['type'])
		bonus = int(theme["bonus"])
		malus = int(theme["malus"])
		print('Theme:' + theme['name'])
		print('Description:' + theme['description'])

		if randomInt == 1 :
			players[0].popularity += bonus
			players[1].popularity += malus
		else :
			players[1].popularity += bonus
			players[0].popularity += malus
		







