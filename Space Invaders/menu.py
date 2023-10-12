import pygame as pg
from buttons import *
from settings import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Menu:
    background: pg.Surface

    button_play: Button
    button_difficulty: Button
    button_exit: Button


def init(game: 'Game | Menu'):
    game.background = pg.image.load("assets/background.png").convert()

    game.button_play = Button(
        (Width // 2) - 100, 100,
        "Play",
        function=lambda g: g.new_level("place_holder"), arg=game
    )
    game.button_difficulty = Button(
        (Width // 2) - 100, 250,
        "Difficulty",
        function=lambda g: g.new_level("difficulty"), arg=game
    )
    game.button_exit = Button(
        (Width // 2) - 100, 400,
        "Exit",
        function=exit
    )


def loop(game: 'Game | Menu'):
    game.screen.blit(game.background, (0, 0))

    game.button_play.update()
    game.button_difficulty.update()
    game.button_exit.update()
