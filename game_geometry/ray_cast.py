from map import *
from functions import *
import math
from sympy import Ray, Point, Ray2D, Point2D, Segment, Segment2D


class Ray_tracer:
    def __init__(self, game):
        self.game = game
        self.rays = []

    def ray_size(self):
        playerX = self.game.player.x
        playerY = self.game.player.y
        player_ang = self.game.player.ang
        offsetX = offsetY = 0
        self.rays.clear()
        angle_ray = angle_to_fist(player_ang - math.radians(FOV) / 2)

        for contador in range(RES[0] // SCALE):
            ray = Ray(Point(playerX, playerY), angle=angle_ray)
            for obj in self.game.map.world_wall:
                print(ray.intersection(obj.entity))


            angle_ray += math.radians(FOV) / (RES[0] // SCALE)
            angle_ray = angle_to_fist(angle_ray)

    def draw_rays(self, screen):
        pass

    def draw(self, screen):
        self.ray_size()
        pass
