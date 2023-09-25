import numpy as np
import pygame as pg
from numba import njit, jit
from settings import *
from map import Tiles

Draw_functions = []
Overwrites = []
Underwrites = []


def add_draw_overwrite(func):
    Overwrites.append(len(Draw_functions))
    Draw_functions.append(func)


def add_draw_underwrite(func):
    Underwrites.append(len(Draw_functions))
    Draw_functions.append(func)


def add_draw(func):
    Draw_functions.append(func)


def draw_order(to_draw):
    func_id, item = to_draw
    if func_id in Overwrites:
        return 0
    if func_id in Underwrites:
        return 9999999999999
    return item[0]


class Drawer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.to_draw = []

    def update(self):
        self.screen.fill([0, 0, 0])  # preto
        # print(self.to_draw[0])
        self.to_draw.sort(reverse=True, key=draw_order)
        for func_id, item in self.to_draw:
            Draw_functions[func_id](item, self.screen, self.game)
        self.to_draw.clear()


def render_line(ray_dist, ray_id, ray_point, look, tile_texture, screen):
    line_high = Tile_size * RES[0] / ray_dist
    # if line_high > 4000: line_high = 4000  # <-- A gambiarra
    line_offset = (RES[1] - line_high) / 2

    if tile_texture:
        if look == 0:  # Norte
            offset = Tile_size - (ray_point[0] % Tile_size)
        elif look == 1:  # Sul
            offset = ray_point[0] % Tile_size
        elif look == 2:  # Lest
            offset = Tile_size - (ray_point[1] % Tile_size)
        else:  # Oeste
            offset = ray_point[1] % Tile_size

        for id_y in range():
            pass

        coluna = tile_texture.subsurface(
            Texture_Res * offset / Tile_size,
            0,
            1,
            Texture_Res
        )
        coluna = pg.transform.scale(coluna, (SCALE, line_high))

        screen.blit(coluna, (ray_id * SCALE, line_offset))


@add_draw
def ray_cast(item, screen, game):
    ray_dist, ray_id, ray_point, look = item
    line_high = Tile_size * RES[0] / ray_dist
    if line_high > 4000: line_high = 4000  # <-- A gambiarra
    line_offset = (RES[1] - line_high) / 2

    if game.map.tile_texture(ray_point[0], ray_point[1]):
        if look == 0:  # Norte
            offset = Tile_size - (ray_point[0] % Tile_size)
        elif look == 1:  # Sul
            offset = ray_point[0] % Tile_size
        elif look == 2:  # Lest
            offset = Tile_size - (ray_point[1] % Tile_size)
        else:  # Oeste
            offset = ray_point[1] % Tile_size

        coluna = game.map.tile_texture(ray_point[0], ray_point[1])[look].subsurface(
            Texture_Res * offset / Tile_size,
            0,
            1,
            Texture_Res
        )
        coluna = pg.transform.scale(coluna, (SCALE, line_high))

        screen.blit(coluna, (ray_id * SCALE, line_offset))
        return

    pg.draw.rect(screen,  # Tela
                 game.map.tile_color(ray_point[0], ray_point[1]),  # color
                 (
                     ray_id * SCALE,
                     line_offset,
                     SCALE,
                     line_high
                 )
                 )


@add_draw_overwrite
def player(self, screen, game):
    x = (Mine_Map_zoom * self.x / Tile_size) + Mini_Map_position[0]
    y = (Mine_Map_zoom * self.y / Tile_size) + Mini_Map_position[1]
    pg.draw.circle(screen, 'Green', (x, y), Mine_Map_zoom / 4)
    pg.draw.line(screen, 'Pink', (x, y), self.calc_linha(x, y, Mine_Map_zoom / 5), 2)


@add_draw_overwrite
def mine_map(self, screen, game):
    tamanho = (Mine_Map_zoom * len(self.world_map[0]), Mine_Map_zoom * len(self.world_map))
    pg.draw.rect(self.game.screen, [220, 220, 220], (Mini_Map_position, tamanho))
    for y, linha in enumerate(self.world_map):
        yr = int((y * Mine_Map_zoom) + Mini_Map_position[1])
        for x, tile in enumerate(linha):
            xr = int((x * Mine_Map_zoom) + Mini_Map_position[0])

            pg.draw.rect(screen, Tiles[self.world_map[y][x]][2], (xr, yr, Mine_Map_zoom, Mine_Map_zoom), 20)


@add_draw
def sprite(item, screen, game):
    dist, scale, image, height, screen_x, height_shift = item
    # pg.draw.circle(screen,
    #               'red',
    #               ((Mine_Map_zoom * self.x / Tile_size) + Mini_Map_position[0],
    #                (Mine_Map_zoom * self.y / Tile_size) + Mini_Map_position[1]),
    #               4
    #               )

    high = scale * (Tile_size * RES[0]) / dist

    image = pg.transform.scale_by(image, high / height)

    screen.blit(image, (
        screen_x,
        ((RES[1] - high * height_shift) / 2)
    ))


@add_draw_overwrite
def dialogue(item, screen, game):
    img, x, y = item

    screen.blit(img, (x, y))


@add_draw_underwrite
def floor(item, screen, game):
    img = pg.surfarray.make_surface(item)
    img = pg.transform.scale_by(img, SCALE)
    screen.blit(img, (0, 0))
