from map import *
from time import sleep
from sys import exit

class Actions:

    def __init__(self, game):
        self.game = game


    def actions(self):
        playerX = self.game.player.x
        playerY = self.game.player.y
        self.action = self.game.map.tile_action(playerX, playerY)
        if self.action:
            #print(self.action)

            if self.action == 'Lose':
                self.Lose()

            elif self.action == 'Next map':
                self.Next_map()


    def Next_map(self):
        mapa = self.game.map.mapa_atual + 1
        self.game.map = Map(self.game, mapa)
        self.game.player.x = 50
        self.game.player.y = 50
        self.game.player.ang = 0


    def Lose(self):
        #self.game.font_Blackout.render(text, antialias, color, background=None)
        text = self.game.font_Blackout.render('Você perdeu!', 1, 'red')
        self.game.screen.blit(text, (0, 0))
        #sleep(5)
        #pg.quit()
        #exit()


