import numpy as np
import pygame as pg
from numba import njit, jit, prange
from time import sleep
from settings import *
from functions import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game

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
        self.game: Game = game
        self.screen = game.screen
        self.to_draw = []

    def update(self):
        # self.screen.fill([0, 0, 0])  # preto
        # print(self.to_draw[0])
        self.to_draw.sort(reverse=True, key=draw_order)
        if self.game.player.debug:
            for func_id, item in self.to_draw:
                Draw_functions[func_id](item, self.screen, self.game)
                pg.display.flip()
                sleep(0.007)
        else:
            for func_id, item in self.to_draw:
                Draw_functions[func_id](item, self.screen, self.game)

        self.to_draw.clear()


@njit(fastmath=FastMath)
def render_line(
        ray_dist, ray_id, ray_point, look, walls_height,
        tile_texture, scale, screen
):
    # line_high = Tile_size * RES[0] / ray_dist
    line_high = walls_height[ray_id]
    line_offset = (RES[1] - line_high) // 2

    if tile_texture is not None:
        if look == 0:  # Norte
            offset = int(Texture_Res * (Tile_size - (ray_point[0] % Tile_size)) / Tile_size)
        elif look == 1:  # Sul
            offset = int(Texture_Res * (ray_point[0] % Tile_size) / Tile_size)
        elif look == 2:  # Lest
            offset = int(Texture_Res * (Tile_size - (ray_point[1] % Tile_size)) / Tile_size)
        else:  # Oeste
            offset = int(Texture_Res * (ray_point[1] % Tile_size) / Tile_size)

        if line_high <= RES[1]:
            for id_y in range(int(line_high)):
                for id_x in range(scale):
                    screen[ray_id * SCALE + id_x][int(line_offset + id_y)] = \
                        tile_texture[offset][int(id_y / line_high * Texture_Res)]

        else:
            for id_y in range(RES[1]):
                for id_x in range(scale):
                    screen[ray_id * SCALE + id_x][id_y] = \
                        tile_texture[offset][int((id_y - line_offset) / line_high * Texture_Res)]


@add_draw
def ray_cast(item, screen, game):
    ray_dist, ray_id, ray_point, angle_ray, look = item
    if game.map.tile_texture(ray_point[0], ray_point[1]):
        tile_texture = pg.surfarray.pixels3d(game.map.tile_texture(ray_point[0], ray_point[1]).texture(look))
    else:
        tile_texture = None

    render_line(
        ray_dist,
        ray_id,
        ray_point,
        look,
        game.ray_caster.walls_height,
        tile_texture,
        SCALE if not game.player.xray else SCALE // 2,
        pg.surfarray.pixels3d(screen)
    )


@add_draw_overwrite
def player(self, screen, game):
    x = (Mine_Map_zoom * self.x / Tile_size) + Mini_Map_position[0]
    y = (Mine_Map_zoom * self.y / Tile_size) + Mini_Map_position[1]
    pg.draw.circle(screen, 'Green', (x, y), Mine_Map_zoom / 4)
    pg.draw.line(screen, 'Pink', (x, y), self.calc_linha(x, y, Mine_Map_zoom / 5), 2)


@add_draw_overwrite
def mine_map(self, screen, game):
    tamanho = (Mine_Map_zoom * len(self.world_wall[0]), Mine_Map_zoom * len(self.world_wall))
    pg.draw.rect(self.game.screen, [220, 220, 220], (Mini_Map_position, tamanho))
    for y, linha in enumerate(self.world_wall):
        yr = int((y * Mine_Map_zoom) + Mini_Map_position[1])
        for x, tile in enumerate(linha):
            xr = int((x * Mine_Map_zoom) + Mini_Map_position[0])

            pg.draw.rect(screen, self.tile_set[self.world_wall[y][x]].color, (xr, yr, Mine_Map_zoom, Mine_Map_zoom), 20)


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
    buffer_img, buffer_aph = item
    img = pg.surfarray.make_surface(buffer_img)
    img = pg.transform.scale_by(img, SCALE)
    screen.blit(img, (0, 0))
