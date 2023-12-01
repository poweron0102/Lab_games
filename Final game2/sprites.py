import pygame as pg
import math

from settings import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Sprite:
    def __init__(self, game, name, x, y, scale=0.5, shift=0.07, action=None):
        self.game: InGame = game
        self.player = game.player

        self.x = x
        self.y = y

        self.image = pg.image.load(f'assets/sprites/{name}.png').convert_alpha()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        # self.image_ratio = self.width / self.height

        self.dist = 1
        self.delta_ang = 1
        self.screen_x = 1

        self.scale = scale
        self.height_shift = shift
        self.action = action

    def update(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y

        sprite_ang = math.atan2(dy, dx)
        self.delta_ang = sprite_ang - self.player.ang
        if (dx > 0 and self.player.ang > math.pi) or (dx < 0 and dy < 0):
            self.delta_ang += math.tau  # tau == 2PI

        delta_rays = self.delta_ang / math.radians(FOV / (RES[0] / SCALE))
        self.screen_x = ((RES[0] / SCALE) / 2 + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        view_dist = self.dist * math.cos(self.delta_ang)
        # dist = self.dist * math.cos(delta_ang)
        if -self.width / 2 < self.screen_x < RES[0] + (self.width / 2) and view_dist > 1:
            item = view_dist, self.scale, self.image, self.height, self.screen_x, self.height_shift
            self.game.drawer.to_draw.append((3, item))

        if self.action:
            self.game.action.do_action(self.action, self)


class SpriteHandler:
    def __init__(self, game):
        self.game: Game = game
        self.sprites: list[Sprite] = []

    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def add(self, sprite: Sprite):
        self.sprites.append(sprite)
