
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




class GameUniverseGamePlayers:

    def __init__(self, player_names):
            self.players = [Player(name) for name in player_names]
class GameUniverseGamePlayAreas:
    def __init__(self):
        self.play_area = []

    def add_item(self, item):
        self.play_area.append(item)

    def remove_item(self, item):
        self.play_area.remove(item)
class GameUniverseGamePlayerBoards:
    def __init__(self, player):
        self.player = player
        self.board = []

    def add_piece(self, piece):
        self.board.append(piece)

    def remove_piece(self, piece):
        self.board.remove(piece)
class GameUniverseGamePieces:
    def __init__(self, owner):
        self.owner = owner