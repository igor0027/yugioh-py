# Board is virtual board between two players.
# Board don't have any informations of players or game.
# Board only knows how many cards are there on field and what cards are on field.
# Board field are:
# 1 - monster cards
# 2 - magic cards
# 3 - cards placed on graveyard
# 4 - cards removed from play

class Board(object):
    def __init__(self): # By default, max number of field's cards is five but there is option anyway
        self.monsters = []
        self.magics = []
        self.graveyard = []
        self.removed = []
    def remove_card(self, card):
        for i in (self.monsters, self.magics, self.graveyard, self.removed):
            if card in i:
                i.remove(card)
                return True
        return False
    def add_monster(self, card):
        self.monsters.append(card)
    def add_magic(self, card):
        self.magics.append(card)
    def add_to_graveyard(self, card):
        self.graveyard.append(card)
    def add_to_removed(self, card):
        self.removed.append(card)
    def get_monsters(self):
        return self.monsters
    def get_magics(self):
        return self.magics
    def get_graveyard(self):
        return self.graveyard
    def get_removed(self):
        return self.removed
