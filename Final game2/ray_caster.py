from map import *
from functions import *
import fast_ray_cast
import math


class Ray_tracer:
    def __init__(self, game):
        self.rays = []
        self.game = game

    def ray_size(self):
        playerX = self.game.player.x
        playerY = self.game.player.y
        player_ang = self.game.player.ang
        offsetX = offsetY = 0
        self.rays.clear()
        angle_ray = angle_to_fist(player_ang - math.radians(FOV) / 2)

        for contador in range(RES[0] // SCALE):
            # Calculo horizontal -=-=-=-=-=-=-=--=-=-=-=-
            rendist = 0
            aTan = -1 / (math.tan(angle_ray) + 0.00001)
            if angle_ray > math.pi:  # looking up
                rayY = (playerY // Tile_size) * Tile_size - 0.0001
                rayX = playerX + ((playerY - rayY) * aTan)
                offsetY = -Tile_size
                offsetX = -offsetY * aTan
            elif angle_ray < math.pi:  # looking down
                rayY = (playerY // Tile_size) * Tile_size + Tile_size
                rayX = playerX + ((playerY - rayY) * aTan)
                offsetY = Tile_size
                offsetX = -offsetY * aTan
            else:  # if angle_ray == 0 or angle_ray == math.pi:
                rayY = playerY
                rayX = playerX
                rendist = Render_dist

            while rendist < Render_dist:
                if Tile_size < rayX < RES[0] + Tile_size and -Tile_size < rayY < RES[1] + Tile_size:
                    if self.game.map.is_render(rayX, rayY):
                        break
                # else:
                rayX += offsetX
                rayY += offsetY
                rendist += 1

            ray_posiH = (rayX, rayY)

            # Calculo vertical -=-=-=-=-=-=-=-=-=-=
            rendist = 0
            aTan = -math.tan(angle_ray)
            if angle_ray < math.pi / 2 or angle_ray > math.pi * 3 / 2:  # looking right
                rayX = (playerX // Tile_size) * Tile_size + Tile_size
                rayY = playerY + ((playerX - rayX) * aTan)
                offsetX = Tile_size
                offsetY = -offsetX * aTan
            elif angle_ray > math.pi / 2 and angle_ray < math.pi * 3 / 2:  # looking left
                rayX = (playerX // Tile_size) * Tile_size - 0.0001
                rayY = playerY + ((playerX - rayX) * aTan)
                offsetX = -Tile_size
                offsetY = -offsetX * aTan
            else:
                rayY = playerY
                rayX = playerX
                rendist = Render_dist

            while rendist < Render_dist:
                if Tile_size < rayX < RES[0] + Tile_size and -Tile_size < rayY < RES[1] + Tile_size:
                    if self.game.map.is_render(rayX, rayY):
                        break
                # else:
                rayX += offsetX
                rayY += offsetY
                rendist += 1

            ray_posiV = (rayX, rayY)

            distH = distancia((playerX, playerY), ray_posiH)
            distV = distancia((playerX, playerY), ray_posiV)

            if distH < distV:
                ponto = ray_posiH
                tamanho = distH
            else:
                ponto = ray_posiV
                tamanho = distV

            self.rays.append((contador, ponto, tamanho * math.cos(self.game.player.ang - angle_ray)))

            angle_ray += math.radians(FOV) / (RES[0] // SCALE)
            angle_ray = angle_to_fist(angle_ray)

    def ray_size_fast(self):
        self.rays = fast_ray_cast.cast(
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
        )
        # print(self.rays)

    def draw_rays(self, screen):
        # self.ray_size()
        # self.ray_size_fast()

        # print(self.rays)
        for ray in self.rays:
            pg.draw.line(screen, 'blue', (self.game.player.x, self.game.player.y), ray[1])
            # print(ray)
        self.rays.clear()

    def draw(self, screen):
        # self.ray_size()
        self.ray_size_fast()
        # for a in self.rays: print(a)
        # exit(0)

        for ray_id, ray_point, ray_dist in self.rays:
            line_high = (Tile_size * Screen_distance / (ray_dist + 0.000001)) * self.game.map.wall_higth(ray_point[0],
                                                                                                         ray_point[1])

            pg.draw.rect(screen,  # Tela
                         self.game.map.tile_color(ray_point[0], ray_point[1]),  # color
                         (
                             ray_id * SCALE,
                             ((RES[1] / 2) - line_high) / 2,
                             SCALE,
                             line_high
                         )
                         )
