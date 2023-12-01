import sys
from types import ModuleType
from player import *
from ray_caster import *
from actions import *
from sprites import *
from drawer import *
from dialogue import *
from textures import *
from parallax import *
from in_game import *
from map import *
from importlib import import_module


def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:  # or (event.type == pg.KEYDOWN and event.key == pg.k_ESCAPE):
            pg.quit()
            sys.exit()


class Game:
    level: ModuleType

    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode(RES, pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.time = pg.time.get_ticks()
        self.lest_time = pg.time.get_ticks()
        self.delta_time = 0
        self.new_game("base")
        # pg.mouse.set_visible

    def new_game(self, level: str):
        self.level = import_module(f".{level}", "levels")
        self.level.init(self)

    def update(self):
        pg.display.flip()
        self.screen.fill([0, 0, 0])  # preto
        self.clock.tick(FPS)
        self.lest_time = self.time
        self.time = pg.time.get_ticks()
        self.delta_time = (self.time - self.lest_time) / 1000.0
        pg.display.set_caption(f'Cellular Odyssey   FPS: {self.clock.get_fps() :.1f}')

    def run(self):
        while True:
            check_events()
            self.update()
            self.level.loop(self)


if __name__ == '__main__':
    game = Game()
    game.run()
