from map import *
from time import sleep
from sys import exit

ACTIONS = {}


def add_action(func):
    ACTIONS[func.__name__] = func


class Actions:

    def __init__(self, game):
        self.game = game

    def do_action(self, action):
        ACTIONS[action](self.game)

    def update(self):
        playerX = self.game.player.x
        playerY = self.game.player.y
        action = self.game.map.tile_action(playerX, playerY)
        if action:
            # print(self.action)
            ACTIONS[action](self.game)


@add_action
def Next_map(game):
    mapa = game.map.mapa_atual + 1
    game.map = Map(game, mapa)
    game.player.x = 50
    game.player.y = 50
    game.player.ang = 0


@add_action
def Lose(game):
    # self.game.font_Blackout.render(text, antialias, color, background=None)
    text = game.font_Blackout.render('Você perdeu!', 1, 'red')
    game.screen.blit(text, (0, 0))
    # sleep(5)
    # pg.quit()
    # exit()
