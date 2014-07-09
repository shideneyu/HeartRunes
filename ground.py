import csv, random

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
		randomInt = random.randint(5, 10)
		theme = self.themes[str(randomIntTheme)]
		type = int(theme['type'])
		print('Theme:' + theme['name'])
		print('Description:' + theme['description'])
		
		if randomInt == 1 :
			player1 = players[0]
			player2 = players[1]
		else :
			player1 = players[1]
			player2 = players[0]
			
		
			
		
			
		
					
