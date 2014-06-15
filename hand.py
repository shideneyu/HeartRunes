class Hand:
    def __init__(self, listHand = []):
        self.listHand = listHand
        
    def pickCard(self, name):
        for card in self.listHand:
            if card.name == name:
                servant = card
                self.listHand.remove(card)
                return servant

    def count(self):
        return len(self.listHand)

    def addCard(self, card)
        self.listHand.apppend(card)
        return self.listHand
    
    def draw(self):
        return self.listHand.pop()
