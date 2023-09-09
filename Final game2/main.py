import sys
from player import *
from ray_caster import *
from actions import *


class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()
        self.font_Blackout = pg.font.Font('fonts/Blackout.otf', 250)
        # pg.mouse.set_visible(False)
        # self.sky = pg.image.load('assets/sky/sky.png').convert()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.ray_tracer = Ray_tracer(self)
        self.action = Actions(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'Jogo de célula   FPS: {self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill([0, 0, 0])  # preto
        # self.screen.blit(self.sky, (0, 0))
        self.ray_tracer.draw(self.screen)
        if self.player.open_map: self.draw_2D(self.screen)

    def draw_2D(self, screen):
        self.map.draw(screen)
        #self.ray_tracer.draw_rays(screen)
        self.player.draw(screen)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # or (event.type == pg.KEYDOWN and event.key == pg.k_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.player.movimento()
            self.action.actions()


if __name__ == '__main__':
    game = Game()
    game.run()
