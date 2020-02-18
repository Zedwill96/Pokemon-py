from typing import List

from game import typechart
from game.pokemon import Pokemon


class Player:
    team: List[Pokemon] = []

    def __init__(self):
        if (len(self.team) < 1):
            self.team.append(self.get_random_pokemon())

    @staticmethod
    def get_random_pokemon() -> Pokemon:
        # TODO: actually random pokemon
        random_pokemon = Pokemon("Eevee", 133, typechart.NORMAL)
        return random_pokemon


PLAYER = Player()