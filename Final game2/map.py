import pygame as pg
import numpy as np
from pygame import Surface

from settings import *

Tiles = [
    # T0 = {'Nome': '', 'Is_wall': False, 'Color': [0, 0, 0, 0], 'action': False, 'Wall_higth': 1, 'render': False}
    ['', False, [255, 255, 255], None, 1, False, None],
    ['', True, 'darkgray', None, 1, True, 'quartz_bricks.png'],
    ['', True, 'red', None, 1, True, None],
    ['', True, 'Purple', None, 1, True, None],
    ['', False, 'green', 'Next map', 1, False, None],
    ['', False, '#c92a2a', 'Lose', 1, False, None],
]


def update_tiles():
    for tile in Tiles:
        if type(tile[6]) == str:
            tile[6] = pg.image.load(f'assets/walls/{tile[6]}').convert_alpha()


world_map = np.array([
    [  # Mapa 0
        [0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 2, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 4, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    ],
    [  # Mapa 1
        [0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    ],
    [  # Mapa 2
        [0, 0, 1, 0, 0, 0, 0, 2, 0, 3, 3, 3, 1, 2, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]
])


class Map:
    def __init__(self, game, mapa=0):
        self.game = game
        self.world_map = world_map[mapa]
        self.mapa_atual = mapa
        update_tiles()

    def get_tile(self, x, y):
        x = int(x // Tile_size)
        y = int(y // Tile_size)
        if 0 <= y <= len(self.world_map) - 1 and 0 <= x <= len(self.world_map[y]) - 1:
            return self.world_map[y][x]
        else:
            return 0

    def is_wall(self, x, y) -> bool:
        return Tiles[self.get_tile(x, y)][1]

    def tile_color(self, x, y):
        id = self.get_tile(x, y)
        if id:
            return Tiles[self.get_tile(x, y)][2]
        return [0, 0, 0]

    def tile_action(self, x, y):
        return Tiles[self.get_tile(x, y)][3]

    def wall_high(self, x, y):
        return Tiles[self.get_tile(x, y)][4]

    def is_render(self, x, y) -> bool:
        return Tiles[self.get_tile(x, y)][5]

    def tile_texture(self, x, y) -> Surface | None:
        return Tiles[self.get_tile(x, y)][6]

    def draw(self, screen):
        tamanho = (Mine_Map_zoom * len(self.world_map[0]), Mine_Map_zoom * len(self.world_map))
        pg.draw.rect(self.game.screen, [220, 220, 220], (Mini_Map_position, tamanho))
        for y, linha in enumerate(self.world_map):
            yr = int((y * Mine_Map_zoom) + Mini_Map_position[1])
            for x, tile in enumerate(linha):
                xr = int((x * Mine_Map_zoom) + Mini_Map_position[0])

                pg.draw.rect(screen, Tiles[self.world_map[y][x]][2], (xr, yr, Mine_Map_zoom, Mine_Map_zoom), 20)
