import os

# noinspection PyUnreachableCode
if False:
    from ..main import *
    from ..buttons import *
else:
    # noinspection PyUnresolvedReferences
    from main import *
    # noinspection PyUnresolvedReferences
    from buttons import *


class Menu:
    background: pg.Surface
    levels: list[Button]


MapaNames = [
    'Pneumococos',
    'Staphylococcus',
    'Streptococcus'
]


def init(in_menu: 'Game | Menu'):
    in_menu.background = pg.image.load('assets/gui/fundo_levels.png').convert()
    in_menu.levels = []

    button_cont = 0
    # for file_name in os.listdir('levels/'):
    for file_name in MapaNames:
        bnt = Button(
            80 + button_cont * (80 + 320),
            HalfRenderHeight - 140,
            file_name,
            img_base='button_base_ico',
            img_hover='button_hover_ico',
            func_click=in_menu.new_game, arg_click=file_name
        )
        bnt.img_base.blit(pg.image.load(f'assets/gui/{file_name}.png').convert_alpha(), (0, 4))
        bnt.img_hover.blit(pg.image.load(f'assets/gui/{file_name}.png').convert_alpha(), (0, 4))
        if file_name + ".py" not in os.listdir('levels/'):
            bnt.img_base.blit(pg.image.load(f'assets/gui/cadeado_a.png').convert_alpha(), (0, 0))
            bnt.img_hover.blit(pg.image.load(f'assets/gui/cadeado_a.png').convert_alpha(), (0, 0))
            bnt.func_click = None
            bnt.arg_click = None
        bnt.font_y = bnt.y + 320 - 35
        in_menu.levels.append(bnt)

        button_cont += 1
        if button_cont >= 3:
            break


def loop(in_menu: 'Game | menu'):
    pg.display.get_surface().blit(in_menu.background, (0, 0))

    for button in in_menu.levels:
        button.update()
