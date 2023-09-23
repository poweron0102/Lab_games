from map import *
from functions import *
#from numba import njit
import fast_ray_cast
import math


class RayCaster:
    def __init__(self, game):
        self.game = game

    #@njit()
    def ray_size(self):
        player_x = self.game.player.x
        player_y = self.game.player.y
        player_ang = self.game.player.ang
        offset_x = offset_y = 0
        angle_ray = angle_to_fist(player_ang - math.radians(FOV) / 2)

        for contador in range(RES[0] // SCALE):
            # Calculo horizontal -=-=-=-=-=-=-=--=-=-=-=-
            rendist = 0
            a_tan = -1 / (math.tan(angle_ray) + 0.00001)
            if angle_ray > math.pi:  # looking up
                ray_y = (player_y // Tile_size) * Tile_size - 0.0001
                ray_x = player_x + ((player_y - ray_y) * a_tan)
                offset_y = -Tile_size
                offset_x = -offset_y * a_tan
                look_ns = 1
            elif angle_ray < math.pi:  # looking down
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
                if Tile_size < ray_x < RES[0] + Tile_size and -Tile_size < ray_y < RES[1] + Tile_size:
                    if self.game.map.is_render(ray_x, ray_y):
                        break
                # else:
                ray_x += offset_x
                ray_y += offset_y
                rendist += 1

            ray_posi_h = (ray_x, ray_y)

            # Calculo vertical -=-=-=-=-=-=-=-=-=-=
            rendist = 0
            a_tan = -math.tan(angle_ray)
            if angle_ray < math.pi / 2 or angle_ray > math.pi * 3 / 2:  # looking right
                ray_x = (player_x // Tile_size) * Tile_size + Tile_size
                ray_y = player_y + ((player_x - ray_x) * a_tan)
                offset_x = Tile_size
                offset_y = -offset_x * a_tan
                look_ew = 3
            elif math.pi / 2 < angle_ray < math.pi * 3 / 2:  # looking left
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
                if Tile_size < ray_x < RES[0] + Tile_size and -Tile_size < ray_y < RES[1] + Tile_size:
                    if self.game.map.is_render(ray_x, ray_y):
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

            self.game.drawer.to_draw.append((0, (tamanho * math.cos(self.game.player.ang - angle_ray), contador, ponto, look)))

            angle_ray += math.radians(FOV) / (RES[0] // SCALE)
            angle_ray = angle_to_fist(angle_ray)

    def ray_size_fast(self):
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

    def update(self):
        if RUST:
            self.ray_size_fast()
        else:
            self.ray_size()

    #def draw_rays(self, screen):
    #    self.ray_size()
    #    # self.ray_size_fast()
    #
    #    # print(self.rays)
    #    for ray in self.rays:
    #        pg.draw.line(screen, 'blue', (self.game.player.x, self.game.player.y), ray[1])
    #        # print(ray)
    #    self.rays.clear()


