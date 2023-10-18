import math
import pygame as pg

#from Test.in_game.in_game import Game
from Test.settings import *


class Player:
    def __init__(self, game):
        self.x = 70
        self.y = -110
        self.z = 20
        self.ang = 0
        self.look = 0

        self.speed = 1
        self.height = 10

        self.open_map = False

        self.game = game

    def movimento(self):
        # Movimento WASD  -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        keys = pg.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pg.K_w]:
            dx += self.speed * math.cos(self.ang)
            dy += self.speed * math.sin(self.ang)
            #dx += 1
        if keys[pg.K_d]:
            dx += self.speed * math.cos(self.ang + (math.pi / 2))
            dy += self.speed * math.sin(self.ang + (math.pi / 2))
            #dy -= 1
        if keys[pg.K_a]:
            dx += (self.speed * math.sin(self.ang + (math.pi))) * -1
            dy += self.speed * math.cos(self.ang + (math.pi))
            #dy += 1
        if keys[pg.K_s]:
            dx += self.speed * math.sin(self.ang + (3 * math.pi / 2))
            dy += (self.speed * math.cos(self.ang + (3 * math.pi / 2))) * -1
            #dx -= 1
        # Movimento WASD  -=-=-=-=-=-=-=-=-=-=-=-=-=-=

        # Outros -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        #if keys[pg.K_l]:
        #    self.game.action.Lose()

        if keys[pg.K_m]:
            if self.open_map:
                self.open_map = False
            else:
                self.open_map = True
        # Outros -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        # Movimento Mouse -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] < 10:
            pg.mouse.set_pos(SCREEN_RESOLUTION[0] - 30, mouse_pos[1])

        if mouse_pos[0] > SCREEN_RESOLUTION[0] - 10:
            pg.mouse.set_pos(30, mouse_pos[1])

        # if mouse_pos[1] < 10:
        #    pg.mouse.set_pos(mouse_pos[0], SCREEN_RESOLUTION[1]-30)

        # if mouse_pos[1] > SCREEN_RESOLUTION[1] - 10:
        #    pg.mouse.set_pos(mouse_pos[0], 30)

        mouse_move = pg.mouse.get_rel()
        self.ang += mouse_move[0] * Mouse_sens
        if self.ang > 2 * math.pi:
            self.ang -= 2 * math.pi
        if self.ang < 0:
            self.ang += 2 * math.pi
        # Movimento Mouse -=-=-=-=-=-=-=-=-=-=-=-=-=-=

        #if not self.game.map.is_wall(self.x + dx + Player_size * sig(dx), self.y):
        #    self.x += dx
        self.x += dx
        #if not self.game.map.is_wall(self.x, self.y + dy + Player_size * sig(dy)):
        #    self.y += dy
        self.y += dy

    def calc_linha(self, tamanho):
        return SW2 + (tamanho * math.cos(self.ang)), SH2 + (tamanho * math.sin(self.ang))

    def draw(self):
        x = SW2
        y = SH2
        pg.draw.circle(self.game.game_runner.screen, 'Green', (x, y),  6)
        pg.draw.line(self.game.game_runner.screen, 'Pink', (x, y), self.calc_linha(10), 2)

