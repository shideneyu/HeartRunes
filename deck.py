import random
import csv
from card import Card

class Deck:
    def __init__( self, player ):
        self.player = player
        self.deckPlayer= {}

        with open('datas/'+self.player.name+'.csv', 'r') as f:
            reader = csv.DictReader( f, delimiter = ',' )
            for line in reader:
                self.deckPlayer[line["id_card"] ] = { 'type' : line["type"], 'name' : line["name"], 'attack' :  line["attack"], 'power' : line["power"], 'defense' : line["defense"], 'popularity' : line["popularity"]}

    def getCard( self ) :
        rd = random.choice( list ( self.deckPlayer.keys() ) )
        ca = Card ( self.deckPlayer[  rd ] )
        # on vire la carte du deck
        self.deckPlayer.pop(rd, None)
        return ca
