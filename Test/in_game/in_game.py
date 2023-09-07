from Test.in_game.map import Map
from Test.in_game.player import Player
import pygame as pg

#from Test.main import GameRunner


class InGame:
    def __init__(self, game_runner):
        self.player = Player(self)
        self.word_map = Map(self)

        self.game_runner = game_runner

    def update(self):
        self.player.movimento()

    def draw(self):
        #pg.draw.circle(
        #    self.game_runner.screen,
        #    [0, 250, 5],
        #    (self.player.x, self.player.y),
        #    10
        #)
        self.word_map.draw()
        self.player.draw()

