import csv, random

class Ground:
	def __init__(self):
		self.themes = {}
		self.previousTheme = - 1
		with open('datas/themes.csv', 'r') as f:
			reader = csv.DictReader(f, delimiter=',')
			for line in reader:
				self.themes[line["id"]] = {'type':line["type"],'name':line["name"],'description':line["description"],'bonus':line["bonus"],'malus':line["malus"]}
	
	def groundAction(self, players):
		
		if self.previousTheme != -1:
			if self.previousTheme['type'] != 1:
				self.attackBonusOnAllCards(players, self.previousTheme['type'], int(self.previousTheme["bonus"]) * -1) #Reverse the effect
		
		randomIntTheme = random.randint(1, len(self.themes))
		randomBits = random.getrandbits(1)
		theme = self.themes[str(randomIntTheme)]
		self.previousTheme = theme
		typeOf = theme['type']
		bonus = int(theme["bonus"])
		malus = int(theme["malus"])
		print('Theme:' + theme['name'])
		print('Description:' + theme['description'])
		
		if typeOf == '1': #Event
			if randomBits == 1 :
				players[0].popularity += bonus
				players[1].popularity += malus
			else :
				players[1].popularity += bonus
				players[0].popularity += malus
		else : #Theme
			self.attackBonusOnAllCards(players, typeOf, bonus)
	
	#Ajoute un bonus aux cartes de la main et du plateau selon le theme
	def attackBonusOnAllCards(self, players, typeOf, bonus):
		for player in players:
			for card in player.hand:
				if card.favorite == typeOf:
					card.attack += bonus
			for card in player.cardsInGame:
				if card.favorite == typeOf:
					card.attack += bonus
				
				
				
				
				