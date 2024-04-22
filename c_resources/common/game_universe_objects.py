import pandas
from c_resources.common.game_types
class GameUniverses:
    def __init__\
                    (self,
                     game_universes_game_types,
                     game_universes_players):

        self.game_types =\
            game_universes_game_types

        self.players =\
            game_universes_players

        self.current_game_session =\
            GameUniverseGames

class GameUniverseGames:

    def __init__(self, game_universes_game_types):


        if game_universes_game_types = GameTypes.PORT_ROYAL:
            self.current_game_session = \
                PortRoyalGames(players=self.players)

class PortRoyalGames:

    def __init__\
                    (self,
                     port_royal_players):

        self.port_royal_players = (
            port_royal_players)

        self.port_royal_scores = pandas.DataFrame


