import pygame as pg
from settings import *
from collections import defaultdict
#from numba import jit

T0 = {'Nome': '', 'Is_wall': False, 'Color': '#FFFFFF' , 'action': False     ,'Wall_higth': 1, 'render': False}
T1 = {'Nome': '', 'Is_wall': True , 'Color': 'darkgray', 'action': False     ,'Wall_higth': 1, 'render': True }
T2 = {'Nome': '', 'Is_wall': True , 'Color': 'Red'     , 'action': False     ,'Wall_higth': 1, 'render': True }
T3 = {'Nome': '', 'Is_wall': True , 'Color': 'Purple'  , 'action': False     ,'Wall_higth': 1, 'render': True }
T4 = {'Nome': '', 'Is_wall': False, 'Color': 'green'   , 'action': 'Next map','Wall_higth': 1, 'render': False}
T5 = {'Nome': '', 'Is_wall': False, 'Color': '#c92a2a' , 'action': 'Lose'    ,'Wall_higth': 1, 'render': False}

mini_map = [
    [  # Mapa 0
        [T0, T0, T1, T0, T0, T0, T0, T2, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T0, T0, T2, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T0, T0, T2, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T0, T0, T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T2, T3, T3, T3, T2, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T2, T0, T0, T0, T2, T0, T1, T1, T1, T1, T1, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T1, T0, T4, T0, T1, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T1, T0, T0, T0, T1, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T1, T1, T0, T1, T1, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T1, T0, T0, T0, T1, T0, T0, T0, T2, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0],

    ],
    [  # Mapa 1
        [T0, T0, T1, T0, T0, T0, T0, T2, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T1, T1],
        [T0, T0, T1, T0, T0, T0, T0, T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T0, T0, T2, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T0, T0, T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T2, T0, T0, T0, T2, T0, T1, T1, T1, T1, T1, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T1, T0, T0, T0, T1, T1, T1, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T1, T0, T0, T0, T1, T0, T1, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T1, T1, T0, T1, T1, T0, T0, T0, T1, T0, T0, T0, T0, T0, T4],
        [T0, T0, T1, T0, T0, T1, T0, T0, T0, T1, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0, T0, T0, T5],
    ],
    [  # Mapa 2
        [T0, T0, T1, T0, T0, T0, T0, T2, T0, T3, T3, T3, T1, T2, T1, T0, T0, T0, T1, T1],
        [T0, T0, T1, T0, T0, T0, T0, T0, T0, T3, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T0, T0, T2, T0, T3, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T0, T3, T3, T3, T2, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T3, T0, T0, T0, T2, T0, T1, T1, T1, T1, T1, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T1, T1, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0, T1, T5, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T1, T1, T0, T1, T1, T0, T0, T0, T1, T0, T0, T0, T0, T0, T4],
        [T0, T0, T1, T0, T0, T1, T0, T0, T0, T1, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0],
        [T0, T0, T1, T0, T0, T0, T0, T0, T0, T1, T0, T0, T0, T0, T0, T0, T0, T0, T0, T5],
    ]
]


class Map:
    def __init__(self, game, mapa=0):
        self.game = game
        self.mini_map = mini_map[mapa]
        #self.world_map = defaultdict(lambda: T0)
        self.world_map = {}
        self.get_map()
        self.mapa_atual = mapa


    #@jit(nopython=True)
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def is_wall(self, x, y):
        if (x // Tile_size, y // Tile_size) in self.world_map:
            next_tile = self.world_map[(x // Tile_size, y // Tile_size)]
            return next_tile['Is_wall']
        else:
            return T0['Is_wall']


    def is_render(self, x, y):
        if (x // Tile_size, y // Tile_size) in self.world_map:
            next_tile = self.world_map[(x // Tile_size, y // Tile_size)]
            return next_tile['render']
        else:
            return T0['render']


    def wall_higth(self, x, y):
        if (x // Tile_size, y // Tile_size) in self.world_map:
            next_tile = self.world_map[(x // Tile_size, y // Tile_size)]
            return next_tile['Wall_higth']
        else:
            return T0['Wall_higth']


    def tile_color(self, x, y):
        if (x // Tile_size, y // Tile_size) in self.world_map:
            next_tile = self.world_map[(x // Tile_size, y // Tile_size)]
            return next_tile['Color']
        else:
            return T0['Color']


    def tile_action(self, x, y):
        if (x // Tile_size, y // Tile_size) in self.world_map:
            next_tile = self.world_map[(x // Tile_size, y // Tile_size)]
            return next_tile['action']
        else:
            return T0['action']


    def draw(self, screen):
        tamanho = (Mine_Map_zoom * len(self.mini_map[0]), Mine_Map_zoom * len(self.mini_map))
        pg.draw.rect(self.game.screen, '#FFFFFF', (Mini_Map_position, tamanho))
        for pos in self.world_map:
            x = (pos[0] * Mine_Map_zoom) + Mini_Map_position[0]
            y = (pos[1] * Mine_Map_zoom) + Mini_Map_position[1]
            pg.draw.rect(screen, self.world_map[pos]['Color'], (x, y, Mine_Map_zoom, Mine_Map_zoom), 5)


    def draw_centro(self):
        playerX = self.game.player.x
        playerY = self.game.player.y
        for pos in self.world_map:
            rect = (pos[0] * Tile_size - playerX, pos[1] * Tile_size - playerY, Tile_size, Tile_size)
            pg.draw.rect(self.game.screen, self.world_map[pos]['Color'], rect, 5, 2)
