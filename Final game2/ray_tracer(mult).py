from map import *
from functions import *
import math
from multiprocessing import Pool


def ray_size(data):
    angle_ray, playerX, playerY, player_ang, map = data
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
        if map.is_render(rayX, rayY):
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
            if map.is_render(rayX, rayY):
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

    return (ponto, tamanho * math.cos(player_ang - angle_ray))


class Ray_tracer:
    def __init__(self, game):
        self.rays = []
        self.game = game

    def rays_size(self):
        ray_ang = self.game.player.ang
        player_x, player_y, player_ang = self.game.player.x, self.game.player.y, self.game.player.ang
        game_map = self.game.map
        #self.rays = []

        #data = [(self, angle_to_fist(angle)) for angle in range(ray_ang, ray_ang + math.radians(FOV), math.radians(FOV)/RES[0])]
        data = []
        for i in range(RES[0]):
            data.append((ray_ang, player_x, player_y, player_ang, game_map))
            ray_ang += math.radians(FOV) / RES[0]

        with Pool() as pool:
            result = pool.imap(ray_size, data)
            for point, tamanho in result:
                self.rays.append((point, tamanho))

        #angle_ray = angle_to_fist(ray_ang - math.radians(FOV) / 2)

        #for contador in range(0, RES[0]//SCALE):


            #angle_ray += math.radians(1 / Rays_per_angle)
            #angle_ray = angle_to_fist(angle_ray)


    def draw_rays(self, screen):
        self.rays_size()
        # print(self.rays)
        for ray in self.rays:
            pg.draw.line(screen, 'blue', (self.game.player.x, self.game.player.y), ray[0])
            # print(ray)
        del self.rays

    def draw(self, screen):
        self.rays_size()
        const_screan = RES[0] // (FOV * Rays_per_angle)
        for ray_atual, ray in enumerate(self.rays):
            line_higth = (Tile_size * Screen_distance / (ray[1] + 0.000001)) * self.game.map.wall_higth(ray[0][0],
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
