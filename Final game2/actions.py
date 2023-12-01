from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import *

ACTIONS = {}


def add_action(func):
    ACTIONS[func.__name__] = func


class Actions:

    def __init__(self, game):
        self.game: InGame = game

    def do_action(self, action, *args):
        ACTIONS[action](self.game, args)

    def update(self):
        playerX = self.game.player.x
        playerY = self.game.player.y
        action = self.game.map.tile_action(playerX, playerY)
        if action:
            # print(self.action)
            ACTIONS[action](self.game)


@add_action
def Next_map(game, *args):
    mapa = game.map.mapa_atual + 1
    game.map = Map(game, mapa)
    game.player.x = 50
    game.player.y = 50
    game.player.ang = 0


@add_action
def Lose(game, *args):
    # self.game.font_Blackout.render(text, antialias, color, background=None)
    text = game.font_Blackout.render('Você perdeu!', 1, 'red')
    game.screen.blit(text, (0, 0))
    # sleep(5)
    # pg.quit()
    # exit()


@add_action
def construction(game, *args):
    # print(args[0][0])
    if args[0][0].dist < 128 and game.player.interact:
        game.dialogue_handler.add(
            Dialogue(
                7,
                "Oh, i'm really sorry. but we are doing some construction.",
                "platelet",
                audio='construcao'
            )
        )
        game.dialogue_handler.add(
            Dialogue(
                2,
                "No way we can snappy by?",
                "ae3803pla",
                audio='jeitodepassar'
            )
        )
        game.dialogue_handler.add(
            Dialogue(
                10,
                "No way at all. You see, what happened was there as a bit of trouble so construction get delayed.\
                 I gest the delivery people had made a big mistake.",
                "platelet",
                audio='dellead'
            )
        )
        game.dialogue_handler.add(
            Dialogue(
                10,
                "No way at all. You see, what happened was there as a bit of trouble so construction get delayed. I "
                "gest the delivery people had made a big mistake. Esta é uma mensagem de teste, ela serve para "
                "textar o tamanho maxim dos textos que a caixa de dialogo consegue agent de uma única vez, "
                "por isso eu estou escrevendo um monte de coisa nada haver de uma única vez. pipi´pipopopo"
                "por isso eu estou escrevendo um monte de coisa nada haver de uma única vez. pipi´pipopopo",
                "platelet"
            )
        )
        args[0][0].action = None
