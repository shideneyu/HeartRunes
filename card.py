class Card:
    def __init__( self, data):
        self.name = data["name"]
        self.popularity = data["popularity"]
        self.attack = data["attack"]
        self.power = data["power"]
        self.defense = data["defense"]
        self.type = data["type"]
        self.favorite = data["favorite"]
