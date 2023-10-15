from player import *
from arrow import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class InGame:
    player: Player
    arrow_handle: ArrowHandle


def init(game: 'Game | InGame'):
    game.background = pg.image.load("assets/background2.png").convert()

    game.player = Player()
    game.arrow_handle = ArrowHandle(game.player)


def loop(game: 'Game | InGame'):
    game.player.update()
    game.arrow_handle.update()
