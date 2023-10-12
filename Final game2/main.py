import sys
from types import ModuleType

from player import *
from ray_caster import *
from actions import *
from sprites import *
from drawer import *
from dialogue import *
from parallax import *


def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:  # or (event.type == pg.KEYDOWN and event.key == pg.k_ESCAPE):
            pg.quit()
            sys.exit()


class InGame:
    parallax: Parallax
    dialogue_handler: DialogueHandler
    sprite_handler: SpriteHandler
    drawer: Drawer
    action: Actions
    ray_caster: RayCaster
    player: Player
    map: Map
    level: ModuleType

    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode(RES, pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.time = pg.time.get_ticks()
        self.leas_time = pg.time.get_ticks()
        self.delta_time = 0
        self.new_game("alpha")
        # pg.mouse.set_visible

    def new_game(self, level: str):
        self.level = __import__(level)
        self.level.init(self)

    def update(self):
        pg.display.flip()
        self.screen.fill([0, 0, 0])  # preto
        self.clock.tick(FPS)
        self.leas_time = self.time
        self.time = pg.time.get_ticks()
        self.delta_time = (self.time - self.leas_time) / 1000.0
        pg.display.set_caption(f'Cellular Odyssey   FPS: {self.clock.get_fps() :.1f}')

    def run(self):
        while True:
            check_events()
            self.update()
            self.level.loop(self)


if __name__ == '__main__':
    game = InGame()
    game.run()
