import pygame as pg
import math
from settings import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class Parallax:
    def __init__(self, floor, ceiling, in_game: 'Game'):
        self.game = in_game

        self.x_size = (360/FOV)*RES[0]

        if floor:
            self.floor: pg.Surface | None = pg.transform.scale(
                pg.image.load(f'assets/parallax/{floor}.png').convert(),
                (self.x_size, RES[1]//2)
            )
        else:
            self.floor = None
        if ceiling:
            self.ceiling: pg.Surface | None = pg.transform.scale(
                pg.image.load(f'assets/parallax/{ceiling}.png').convert(),
                (self.x_size, RES[1]//2)
            )
        else:
            self.ceiling = None

    def update(self):
        if self.floor:
            self.game.screen.blit(
                self.floor,
                (-self.x_size*self.game.player.ang/math.tau, RES[1]//2)
            )
            self.game.screen.blit(
                self.floor,
                ((-self.x_size * self.game.player.ang / math.tau) + self.x_size, 0)
            )
        if self.ceiling:
            self.game.screen.blit(
                self.ceiling,
                (-self.x_size*self.game.player.ang/math.tau, 0)
            )
            self.game.screen.blit(
                self.ceiling,
                ((-self.x_size * self.game.player.ang / math.tau) + self.x_size, 0)
            )
