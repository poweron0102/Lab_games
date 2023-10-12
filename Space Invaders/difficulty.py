import pygame as pg
from buttons import *
from settings import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Difficulty:
    background: pg.Surface

    button_easy: Button
    button_normal: Button
    button_hard: Button


def init(game: 'Game | Difficulty'):
    game.background = pg.image.load("assets/background.png").convert()

    def set_difficulty(item):
        g, difficulty = item
        g.Difficulty = difficulty
        print("Dificuldade setada para", g.Difficulty)

    game.button_easy = Button(
        (Width // 2) - 100, 100,
        "Easy",
        function=set_difficulty, arg=(game, 1)
    )
    game.button_normal = Button(
        (Width // 2) - 100, 250,
        "Normal",
        function=set_difficulty, arg=(game, 2)
    )
    game.button_hard = Button(
        (Width // 2) - 100, 400,
        "Hard",
        function=set_difficulty, arg=(game, 3)
    )


def loop(game: 'Game | Difficulty'):
    game.screen.blit(game.background, (0, 0))

    game.button_easy.update()
    game.button_normal.update()
    game.button_hard.update()
