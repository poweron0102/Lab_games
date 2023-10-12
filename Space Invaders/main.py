import sys
import pygame as pg

from settings import *

"""
    Este é o arquivo usado para o loop principal do jogo.
    É aqui que as coisas básicas são definidas.
    Se voce veio aqui pensando em modificar algo, 
    saiba que provavelmente você esta no lugar errado. 
"""


class Game:
    """
    Classe responsável por guardar todas as variables do jogo.
    Aqui é definido apenas o valor inicial delas, ou apenas ofato delas
    existirem.
    """
    def __init__(self):
        pg.init()
        pg.font.init()
        self.Difficulty = 1
        self.screen = pg.display.set_mode((Width, Height))
        self.level = __import__("menu")

        self.level.init(self)

    def new_level(self, nome):
        """
        Muda o fluxo de execução do programa para um definido no
        arquivo "nome".py.
        Executa a função init definida no arquivo, uma única vez
        e passa o loop para a função loop definida no mesmo arquivo.
        """
        self.level = __import__(nome)

        self.level.init(self)

    def update(self):
        """
        Retorna ao menu sempre que ESQ for pressionado
        E encerra o programa sempre que evento de QUIT ocorrer
        Como pressionar "Alt + F4", ou clicar no "X" da janela
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.new_level("menu")

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.update()
            self.level.loop(self)
            pg.display.flip()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()
