from numba import njit

from map import *
from functions import *
import numpy as np
# from numba import njit
import fast_ray_cast


# import math


@njit(fastmath=FastMath)
def cast_walls(player_x, player_y, player_ang, world_map, is_render=(1, 2, 3)):
    # (0, (tamanho * math.cos(player_ang - angle_ray), contador, ponto, look))
    # rays = np.empty(RES[0] // SCALE, dtype=np.dtype( [np.uint8, [float, np.uint16, [float, float], np.uint8]] ))
    # rays = [None] * (RES[0] // SCALE)
    rays = []
    offset_x = offset_y = 0
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
        elif angle_ray < np.pi:  # looking down
            ray_y = (player_y // Tile_size) * Tile_size + Tile_size
            ray_x = player_x + ((player_y - ray_y) * a_tan)
            offset_y = Tile_size
            offset_x = -offset_y * a_tan
            look_ns = 0
        else:  # if angle_ray == 0 or angle_ray == math.pi:
            ray_y = player_y
            ray_x = player_x
            rendist = Render_dist

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
        elif np.pi / 2 < angle_ray < np.pi * 3 / 2:  # looking left
            ray_x = (player_x // Tile_size) * Tile_size - 0.0001
            ray_y = player_y + ((player_x - ray_x) * a_tan)
            offset_x = -Tile_size
            offset_y = -offset_x * a_tan
            look_ew = 2
        else:
            ray_y = player_y
            ray_x = player_x
            rendist = Render_dist

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
        rays.append((0, (tamanho * math.cos(player_ang - angle_ray), contador, ponto, look)))

        angle_ray += math.radians(FOV) / (RES[0] // SCALE)
        angle_ray = angle_to_fist(angle_ray)

    return rays


@njit()
def cast_floor(player_x, player_y, player_ang, world_floor):
    buffer = np.zeros((RenderWidth, RenderHeight, 3), dtype=np.uint8)

    for id_x in range(RenderWidth):
        ray_angle = player_ang + np.deg2rad(id_x / (RenderWidth / FOV) - HalfFOV)
        sin, cos = np.sin(ray_angle), np.cos(ray_angle)
        fish = np.cos(np.deg2rad(id_x / (RenderWidth / FOV) - HalfFOV))

        for id_y in range(HalfRenderHeight):
            n = Tile_size * (HalfRenderHeight / (HalfRenderHeight - id_y + 1)) / fish

            ray_x = (player_x + (n * cos))
            ray_y = (player_y + (n * sin))

            y = int(ray_y // Tile_size)
            if 0 <= y < len(world_floor):
                x = int(ray_x // Tile_size)
                if 0 <= x < len(world_floor[y]):
                    if world_floor[y][x] == 1:
                        buffer[id_x][RenderHeight - id_y - 1] = [0, 255, 0]
                    else:
                        buffer[id_x][RenderHeight - id_y - 1] = [0, 0, 0]

    return buffer


class RayCaster:
    def __init__(self, game):
        self.game = game

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
            self.game.map.world_map
        ))
        # print(self.rays)

    def ray_size_python(self):
        self.game.drawer.to_draw.extend(cast_walls(
            self.game.player.x,
            self.game.player.y,
            self.game.player.ang,
            self.game.map.world_map,
        )
        )

        """
        self.game.drawer.to_draw.append(
            (5, cast_floor(
                self.game.player.x,
                self.game.player.y,
                self.game.player.ang,
                self.game.map.world_floor,
            )
             )
        )
        """


    def update(self):
        if RUST:
            self.ray_size_rust()
        else:
            self.ray_size_python()

    # def draw_rays(self, screen):
    #    self.ray_size()
    #    # self.ray_size_fast()
    #
    #    # print(self.rays)
    #    for ray in self.rays:
    #        pg.draw.line(screen, 'blue', (self.game.player.x, self.game.player.y), ray[1])
    #        # print(ray)
    #    self.rays.clear()
