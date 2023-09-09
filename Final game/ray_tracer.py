from map import *
from functions import *
import math


class Ray_tracer:
    def __init__(self, game):
        self.rays = [ ]
        self.game = game

    def ray_size(self):
        playerX = self.game.player.x
        playerY = self.game.player.y
        player_ang = self.game.player.ang
        offsetX = offsetY = 0
        self.rays = []
        angle_ray = angle_to_fist(player_ang - math.radians(FOV) / 2)

        for contador in range(0, int(FOV * Rays_per_angle)):
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

            self.rays.append((ponto, tamanho * math.cos(self.game.player.ang - angle_ray)))

            angle_ray += math.radians(1 / Rays_per_angle)
            angle_ray = angle_to_fist(angle_ray)

    def draw_rays(self, screen):
        self.ray_size()
        # print(self.rays)
        for ray in self.rays:
            pg.draw.line(screen, 'blue', (self.game.player.x, self.game.player.y), ray[0])
            # print(ray)
        del self.rays

    def draw(self, screen):
        self.ray_size()
        const_screan = RES[0] // (FOV * Rays_per_angle)
        for ray_atual, ray in enumerate(self.rays):
            line_higth = (Tile_size * Screen_distance / (ray[1] + 0.000001)) * self.game.map.wall_high(ray[0][0],
                                                                                                       ray[0][1])
            # if line_higth > RES[1]: line_higth = RES[1] # Limitar o tamanho da parede

            # Dezenhar o chão
            # pg.draw.rect(screen,
            #             'darkblue',
            # s             (ray_atual * RES[0] / (FOV * Rays_per_angle), (RES[1]/2) - line_higth, RES[0] / (FOV * Rays_per_angle), 9990))
            # parede
            pg.draw.rect(screen,  # Tela
                         self.game.map.tile_color(ray[0][0], ray[0][1]),  # color
                         (ray_atual * const_screan, ((RES[1] / 2) - line_higth) / 2, const_screan,
                          line_higth))  # posição
