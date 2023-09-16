import sys
from player import *
from ray_caster import *
from actions import *
from sprites import *
from drawer import *
from dialogue import *


def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:  # or (event.type == pg.KEYDOWN and event.key == pg.k_ESCAPE):
            pg.quit()
            sys.exit()


class InGame:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode(RES, pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.time = pg.time.get_ticks()
        self.leas_time = pg.time.get_ticks()
        self.delta_time = 0
        self.new_game()
        self.font_Blackout = pg.font.Font('fonts/Blackout.otf', 250)
        # pg.mouse.set_visible(False)

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.ray_caster = RayCaster(self)
        self.action = Actions(self)
        self.drawer = Drawer(self)

        self.plaqueta = Sprite(self, 'platelet', 545, 610, action='construction')
        self.dialogue_handler = DialogueHandler(self)
        #self.dig = Dialogue(5, "Com licença, me desculpe, mas nos estamos fazendo uma construção.", "platelet")

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        self.leas_time = self.time
        self.time = pg.time.get_ticks()
        self.delta_time = (self.time - self.leas_time) / 1000.0
        pg.display.set_caption(f'Cellular Odyssey   FPS: {self.clock.get_fps() :.1f}')

    def run(self):
        while True:
            check_events()
            self.update()
            self.player.update()
            self.action.update()
            self.ray_caster.update()

            self.plaqueta.update()
            self.dialogue_handler.update()

            self.drawer.update()


if __name__ == '__main__':
    game = InGame()
    game.run()
