class Card:
    def __init__( self, data):
        self.id = id
        self.name = data["name"]
        self.popularity = int(data["popularity"])
        self.attack = data["attack"]
        self.power = int(data["power"])
        self.defense = int(data["defense"])
        self.type = data["type"]
