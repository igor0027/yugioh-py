cards__list = []

EVENT_CONTINUE = 0
EVENT_STOP = 1
EVENT_HALFSTOP = 2

import random

class Game(object):
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player
        self.turn = first_player
    def attack(self, first_card, second_card):
