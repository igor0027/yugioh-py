Card(cid, name, description, card_type, attack, defense, level, effect, attribute="No", current_position=0)
# card_type could be 1 - Monsters, 2 - Spell Cards, 3 - Trap cards
# current_position could be 0 - in deck, 1 - in hand, 2 - face up, 3 - face up defense, 4 - face down
# effect could be False - no effect or True - effect

from model.py import Card

card = Card(1523, "Summoned Skull", "Opis", 1, 2500, 1200, 6, 0)
card.connect_
card2 = Card(1532, "Aqua Madoor", "Opis", 1, 1200, 2000, 4, 0)
