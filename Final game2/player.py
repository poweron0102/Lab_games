# from settings import *
# import pygame as pg
# from map import *
from settings import *
import math
from functions import sig

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class Player:
    def __init__(self, game):
        self.game: Game = game

        self.x = Posicao_inicial[0]
        self.y = Posicao_inicial[1]

        self.speed = Player_speed

        self.xray = False
        self.open_map = False
        self.interact = False
        self.debug = False

        self.ang = math.radians(Default_angulo)

        self.keys = pg.key.get_pressed()

    def update(self):
        # Movimento WASD  -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        keys = pg.key.get_pressed()
        dx = 0
        dy = 0
        speed = self.speed * self.game.delta_time

        if keys[pg.K_w]:
            dx += speed * math.cos(self.ang)
            dy += speed * math.sin(self.ang)
        if keys[pg.K_d]:
            dx += speed * math.cos(self.ang + (math.pi / 2))
            dy += speed * math.sin(self.ang + (math.pi / 2))
        if keys[pg.K_a]:
            dx += (speed * math.sin(self.ang + math.pi)) * -1
            dy += speed * math.cos(self.ang + math.pi)
        if keys[pg.K_s]:
            dx += speed * math.sin(self.ang + (3 * math.pi / 2))
            dy += (speed * math.cos(self.ang + (3 * math.pi / 2))) * -1
        # Movimento WASD  -=-=-=-=-=-=-=-=-=-=-=-=-=-=

        # Outros -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        if keys[pg.K_e] and not self.keys[pg.K_e]:
            self.interact = True
        else:
            self.interact = False

        if keys[pg.K_0] and not self.keys[pg.K_0]:
            self.debug = True
        else:
            self.debug = False

        if keys[pg.K_m] and not self.keys[pg.K_m]:
            self.open_map = not self.open_map

        if keys[pg.K_x] and not self.keys[pg.K_x]:
            self.xray = not self.xray

        # Outros -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        self.keys = keys

        # Movimento Mouse -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] < 10:
            pg.mouse.set_pos(RES[0] - 30, mouse_pos[1])

        if mouse_pos[0] > RES[0] - 10:
            pg.mouse.set_pos(30, mouse_pos[1])

        mouse_move = pg.mouse.get_rel()
        self.ang += mouse_move[0] * Mouse_sens
        if self.ang > 2 * math.pi:
            self.ang -= 2 * math.pi
        if self.ang < 0:
            self.ang += 2 * math.pi
        # Movimento Mouse -=-=-=-=-=-=-=-=-=-=-=-=-=-=

        if not self.game.map.is_wall(self.x + dx * Player_size, self.y):
            self.x += dx

        if not self.game.map.is_wall(self.x, self.y + dy * Player_size):
            self.y += dy

        if self.open_map:
            self.game.drawer.to_draw.extend([
                (2, self.game.map),
                (1, self)
            ])

    def calc_linha(self, x, y, tamanho):
        return x + (tamanho * math.cos(self.ang)), y + (tamanho * math.sin(self.ang))

    def calc_linha_centro(self, tamanho):
        return RES[0] / 2 + (tamanho * math.cos(self.ang)), RES[1] / 2 + (tamanho * math.sin(self.ang))
