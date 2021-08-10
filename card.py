# Card object is used for both creating and editing cards.
# Also, you can hook events like attacks, flips etc.
# Argument 'handler' should be function that will be called on specific event such as flip.

class Card(object):
    def __init__(self, cid, name, description, card_type, attack, defense, level, effect, attribute):
        self.cid = cid
        self.name = name
        self.description = description
        self.card_type = card_type
        self.attack = attack
        self.defense = defense
        self.level = level
        self.effect = effect
        self.attribute = attribute
        self.current_position = None
        self.owner = None
    def event_attack(self, handler):
        self.on_attack = handler
    def event_flip(self, handler):
        self.on_flip = handler
    def event_summoned(self, handler):
        self.on_summoned = handler
    def event_drawn(self, handler):
        self.on_draw = handler
    def event_attacked(self, handler):
        self.on_attacked = handler
    def event_destroyed(self, handler):
        self.on_destroyed = handler
    def event_graveyard(self, handler):
        self.on_graveyard = handler
    def event_effect(self, handler):
        self.on_effect = handler
