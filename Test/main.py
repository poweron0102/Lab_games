import sys

from settings import *
from Test.in_game.in_game import *
import pygame as pg


def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


class GameRunner:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SCREEN_RESOLUTION)
        self.clock = pg.time.Clock()

        self.game_mode = InGame(self)

    def run(self):
        while True:
            check_events()

            pg.display.flip()
            self.clock.tick(FPS)
            pg.display.set_caption(f'Cells at work   FPS: {self.clock.get_fps() :.1f}')

            self.game_mode.update()

            self.screen.fill([0, 0, 0])  # preto
            self.game_mode.draw()


if __name__ == '__main__':
    game = GameRunner()
    game.run()
