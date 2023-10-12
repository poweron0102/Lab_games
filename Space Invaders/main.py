import sys
import pygame as pg

from settings import *


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((Width, Height))
        self.level = __import__("menu")

        self.level.init(self)

    def new_level(self, nome):
        self.level = __import__(nome)

        self.level.init(self)

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # or (event.type == pg.KEYDOWN and event.key == pg.k_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.new_level("menu")

    def run(self):
        while True:
            self.update()
            self.level.loop(self)
            pg.display.flip()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()
