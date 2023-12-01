from numba import njit, typeof, jit

# from map import *
from settings import *
from functions import *
import numpy as np
import functools

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game
    from in_game import InGame


@njit(fastmath=FastMath)
def cast_walls(player_x, player_y, player_ang, world_map, is_render, walls_height):
    rays = []
    angle_ray = angle_to_fist(player_ang - np.deg2rad(FOV) / 2)

    for contador in range(RES[0] // SCALE):
        # Calculo horizontal -=-=-=-=-=-=-=--=-=-=-=-
        rendist = 0
        a_tan = -1 / (np.tan(angle_ray) + 0.00001)
        if angle_ray > np.pi:  # looking up
            ray_y = (player_y // Tile_size) * Tile_size - 0.0001
            ray_x = player_x + ((player_y - ray_y) * a_tan)
            offset_y = -Tile_size
            offset_x = -offset_y * a_tan
            look_ns = 1
        else:  # looking down
            ray_y = (player_y // Tile_size) * Tile_size + Tile_size
            ray_x = player_x + ((player_y - ray_y) * a_tan)
            offset_y = Tile_size
            offset_x = -offset_y * a_tan
            look_ns = 0

        while rendist < Render_dist:
            y = int(ray_y // Tile_size)
            if 0 <= y < len(world_map):
                x = int(ray_x // Tile_size)
                if 0 <= x < len(world_map[y]):
                    if world_map[y][x] in is_render:
                        break
            # else:
            ray_x += offset_x
            ray_y += offset_y
            rendist += 1

        ray_posi_h = (ray_x, ray_y)

        # Calculo vertical -=-=-=-=-=-=-=-=-=-=
        rendist = 0
        a_tan = -np.tan(angle_ray)
        if angle_ray < np.pi / 2 or angle_ray > np.pi * 3 / 2:  # looking right
            ray_x = (player_x // Tile_size) * Tile_size + Tile_size
            ray_y = player_y + ((player_x - ray_x) * a_tan)
            offset_x = Tile_size
            offset_y = -offset_x * a_tan
            look_ew = 3
        else:  # looking left
            ray_x = (player_x // Tile_size) * Tile_size - 0.0001
            ray_y = player_y + ((player_x - ray_x) * a_tan)
            offset_x = -Tile_size
            offset_y = -offset_x * a_tan
            look_ew = 2

        while rendist < Render_dist:
            y = int(ray_y // Tile_size)
            if 0 <= y < len(world_map):
                x = int(ray_x // Tile_size)
                if 0 <= x < len(world_map[y]):
                    if world_map[y][x] in is_render:
                        break
            # else:
            ray_x += offset_x
            ray_y += offset_y
            rendist += 1

        ray_posi_v = (ray_x, ray_y)

        dist_h = distancia((player_x, player_y), ray_posi_h)
        dist_v = distancia((player_x, player_y), ray_posi_v)

        if dist_h < dist_v:
            ponto = ray_posi_h
            tamanho = dist_h
            look = look_ns
        else:
            ponto = ray_posi_v
            tamanho = dist_v
            look = look_ew

        # rays[contador] = (0, (tamanho * math.cos(player_ang - angle_ray), contador, ponto, look))
        ray_dist = tamanho * math.cos(player_ang - angle_ray)
        rays.append((0, (ray_dist, contador, ponto, angle_ray, look)))
        walls_height[contador] = Tile_size * RES[0] / ray_dist

        angle_ray += math.radians(FOV) / (RES[0] // SCALE)
        angle_ray = angle_to_fist(angle_ray)

    return rays


@njit(fastmath=FastMath)
def cast_floor(
        player_x, player_y, player_ang,
        walls_height,
        world_floor, world_ceiling,
        floor_textures, floor_textures_alpha,
        buffer_img
):
    for id_x in range(RenderWidth):
        ray_angle = player_ang + np.deg2rad(id_x / (RenderWidth / FOV) - HalfFOV)
        sin, cos = np.sin(ray_angle), np.cos(ray_angle)
        fish = np.cos(np.deg2rad(id_x / (RenderWidth / FOV) - HalfFOV))

        c_height = HalfRenderHeight - walls_height[id_x//2]//2
        #if c_height > HalfRenderHeight:
        #    c_height = HalfRenderHeight
        for id_y in range(c_height):
            n = Tile_size * (HalfRenderWidth / (HalfRenderHeight - id_y)) / fish

            ray_x = (player_x + (n * cos))
            ray_y = (player_y + (n * sin))

            y = int(ray_y // Tile_size)
            if 0 <= y < len(world_floor):
                x = int(ray_x // Tile_size)
                if 0 <= x < len(world_floor[y]):
                    tex_x_rel = int(((ray_x % Tile_size) / Tile_size) * Texture_Res)
                    tex_y_rel = int(((ray_y % Tile_size) / Tile_size) * Texture_Res)

                    floor_id = world_floor[y][x]
                    if floor_id != 0 and floor_textures_alpha[floor_id - 1][tex_x_rel][tex_y_rel] == 255:
                        buffer_img[id_x][RenderHeight - id_y - 1] = floor_textures[floor_id - 1][tex_x_rel][tex_y_rel]

                    ceiling_id = world_ceiling[y][x]
                    if ceiling_id != 0 and floor_textures_alpha[ceiling_id - 1][tex_x_rel][tex_y_rel] == 255:
                        buffer_img[id_x][id_y] = floor_textures[ceiling_id - 1][tex_x_rel][tex_y_rel]


class RayCaster:
    def __init__(self, game):
        self.game: InGame = game
        self.walls_height = np.zeros(RES[0] // SCALE, dtype=np.uint16)

    """
    def ray_size_rust(self):
        self.game.drawer.to_draw.extend(fast_ray_cast.cast(
            NumThreads,
            self.game.player.x,
            self.game.player.y,
            self.game.player.ang,
            math.radians(FOV),
            RES[0],
            Tile_size,
            SCALE,
            Render_dist,
            [1, 2, 3],
            self.game.map.world_wall
        ))
        # print(self.rays)
    """

    def ray_size_python(self):
        self.game.drawer.to_draw.extend(cast_walls(
            self.game.player.x,
            self.game.player.y,
            self.game.player.ang,
            self.game.map.world_wall,
            self.game.map.tiles_to_render,
            self.walls_height
        ))

        cast_floor(
            self.game.player.x,
            self.game.player.y,
            self.game.player.ang,
            self.walls_height,
            self.game.map.world_floor,
            self.game.map.world_ceiling,
            self.game.map.texture_floor,
            self.game.map.texture_floor_alpha,
            pg.surfarray.pixels3d(self.game.screen)
        )

    def update(self):
        self.ray_size_python()
