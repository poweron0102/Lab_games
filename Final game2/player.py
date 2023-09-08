#from settings import *
#import pygame as pg
from map import *
import math
from functions import sig

class Player:
    def __init__(self, game):
        self.x = Posicao_inicial[0]
        self.y = Posicao_inicial[1]

        self.speed = Player_speed

        self.open_map = False

        self.ang = math.radians(Default_angulo)

        self.game = game

    def movimento(self):
        # Movimento WASD  -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        keys = pg.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pg.K_w]:
            dx += self.speed * math.cos(self.ang)
            dy += self.speed * math.sin(self.ang)
        if keys[pg.K_d]:
            dx += self.speed * math.cos(self.ang + (math.pi / 2))
            dy += self.speed * math.sin(self.ang + (math.pi / 2))
        if keys[pg.K_a]:
            dx += (self.speed * math.sin(self.ang + math.pi)) * -1
            dy += self.speed * math.cos(self.ang + math.pi)
        if keys[pg.K_s]:
            dx += self.speed * math.sin(self.ang + (3 * math.pi / 2))
            dy += (self.speed * math.cos(self.ang + (3 * math.pi / 2))) * -1
        # Movimento WASD  -=-=-=-=-=-=-=-=-=-=-=-=-=-=

        # Outros -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        if keys[pg.K_l]:
            self.game.action.Lose()

        if keys[pg.K_m]:
            if self.open_map:
                self.open_map = False
            else:
                self.open_map = True
        # Outros -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        # Movimento Mouse -=-=-=-=-=-=-=-=-=-=-=-=-=-=
        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] < 10:
            pg.mouse.set_pos(RES[0] - 30, mouse_pos[1])

        if mouse_pos[0] > RES[0] - 10:
            pg.mouse.set_pos(30, mouse_pos[1])

        # if mouse_pos[1] < 10:
        #    pg.mouse.set_pos(mouse_pos[0], RES[1]-30)

        # if mouse_pos[1] > RES[1] - 10:
        #    pg.mouse.set_pos(mouse_pos[0], 30)

        mouse_move = pg.mouse.get_rel()
        self.ang += mouse_move[0] * Mouse_sens
        if self.ang > 2 * math.pi:
            self.ang -= 2 * math.pi
        if self.ang < 0:
            self.ang += 2 * math.pi
        # Movimento Mouse -=-=-=-=-=-=-=-=-=-=-=-=-=-=

        if not self.game.map.is_wall(self.x + dx + Player_size * sig(dx), self.y):
            self.x += dx

        if not self.game.map.is_wall(self.x, self.y + dy + Player_size * sig(dy)):
            self.y += dy

    def calc_linha(self, x, y, tamanho):
        return ((x + (tamanho * math.cos(self.ang)), y + (tamanho * math.sin(self.ang))))


    def calc_linha_centro(self, tamanho):
        return ((RES[0]/2 + (tamanho * math.cos(self.ang)), RES[1]/2 + (tamanho * math.sin(self.ang))))


    def draw(self, screen):
        x = (Mine_Map_zoom * self.x / Tile_size) + Mini_Map_position[0]
        y = (Mine_Map_zoom * self.y / Tile_size) + Mini_Map_position[1]
        pg.draw.circle(screen, 'Green', (x, y), Mine_Map_zoom / 4)
        pg.draw.line(screen, 'Pink', (x, y), self.calc_linha(x, y, Mine_Map_zoom / 5), 2)


    def draw_centro(self):
        pg.draw.circle(self.game.screen, 'Green', (RES[0]/2, RES[1]/2), 15)
        pg.draw.line(self.game.screen, 'Pink', (RES[0]/2, RES[1]/2), self.calc_linha_centro(50), 3)
