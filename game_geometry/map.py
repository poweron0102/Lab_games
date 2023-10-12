import pygame as pg
# import sympy as sp
from sympy import Ray, Point, Ray2D, Point2D, Segment, Segment2D
from sympy.geometry.entity import GeometryEntity

from settings import *


class Wall:
    entity: GeometryEntity
    color: tuple[int]

    def __init__(self, entity: GeometryEntity, color=(255, 255, 255)):
        self.entity = entity
        self.color = color


world_map = [
    [
        Wall(Segment(Point2D(1, 1), Point2D(1, 600))),
        #Wall(Segment(Point2D(1, 600), Point2D(600, 600))),
        #Wall(Segment(Point2D(600, 600), Point2D(600, 1))),
        #Wall(Segment(Point2D(600, 1), Point2D(1, 1))),
    ],
    [
        None
    ]
]


class Map:
    def __init__(self, game, mapa=0):
        self.game = game
        self.world_map = world_map[mapa]
        self.mapa_atual = mapa

    def draw(self, screen):
        for obj in self.world_map:
            # print(type(object) == Segment2D)
            if type(obj.entity) == Segment2D:
                x1, y1, x2, y2 = obj.entity.bounds
                pg.draw.line(
                    screen,
                    obj.color,
                    (x1, y1),
                    (x2, y2),
                    1
                )
