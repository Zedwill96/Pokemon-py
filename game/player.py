from typing import List

import asyncio

from api import pokeapi
from config.config import TEXT
from game.pokemon import Pokemon


class Player:
    """Holds current information about the player"""

    team: List[Pokemon] = []

    def __init__(self):
        """Fills the player's team with a random Pokemon from the PokeAPI"""
        if len(self.team) < 1:
            self.team.extend(asyncio.run(pokeapi.get_random_pokemon_from_api(1)))

    def add_to_team(self, pokemon: Pokemon):
        """Add a pokemon to the user's team and inform the user"""
        self.team.append(pokemon)
        print(f"{pokemon.name} {TEXT['POKEMON']['ADD']}")

    def print_team(self):
        """Prints a formatted table of the player's team"""
        header = "{:4} {:^11} {:6} {:^9}{:^9}".format(
            "No.", "Name", "Health", "Type", "Type 2"
        )
        print(header)
        print(*[str(pokemon) for pokemon in self.team], sep="\n", end="\n" * 2)


"""Global Player instance"""
PLAYER = Player()
