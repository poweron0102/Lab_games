import pygame as pg
import numpy as np
from pygame import Surface
from settings import *
from textures import *
from numba.experimental.jitclass import jitclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import InGame


class Tile:
    def __init__(self, is_wall, render, color, action, texture: int | None):
        self.is_wall = is_wall
        self.render = render
        self.color = color
        self.action = action
        self.texture = texture


class Map:
    def __init__(self, game, world_map, tile_set, texture_set, texture_floor):
        self.game: InGame = game

        self.tile_set: list[Tile] = tile_set
        self.texture_set: list[Texture] = texture_set

        self.world_wall: list[list[int]] = world_map[0]
        self.world_floor: list[list[int]] = world_map[1]
        self.world_ceiling: list[list[int]] = world_map[2]

        self.texture_floor = np.empty([len(texture_floor), Texture_Res, Texture_Res, 3], dtype=np.int8)
        for tex_id, tex_name in enumerate(texture_floor):
            self.texture_floor[tex_id] = pg.surfarray.array3d(pg.image.load(f"assets/floor/{tex_name}.png"))

    def get_tile(self, x, y):
        x = int(x // Tile_size)
        y = int(y // Tile_size)
        if 0 <= y <= len(self.world_wall) - 1 and 0 <= x <= len(self.world_wall[y]) - 1:
            return self.world_wall[y][x]
        else:
            return 0

    def is_wall(self, x, y) -> bool:
        return self.tile_set[self.get_tile(x, y)].is_wall

    def tile_color(self, x, y):
        id = self.get_tile(x, y)
        if id:
            return self.tile_set[self.get_tile(x, y)].color
        return [0, 0, 0]

    def tile_action(self, x, y):
        return self.tile_set[self.get_tile(x, y)].action

    def is_render(self, x, y) -> bool:
        return self.tile_set[self.get_tile(x, y)].render

    def tile_texture(self, x, y) -> Texture | None:
        if self.tile_set[self.get_tile(x, y)].texture:
            return self.texture_set[self.tile_set[self.get_tile(x, y)].texture]
