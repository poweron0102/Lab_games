import pygame.time

from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *

from inimigo import *


def menu_ranking():
    # CRIANDO A TELA
    janela = Window(1200, 600)
    janela.set_title('MENU RANKING')

    # CRIANDO TECLADO
    teclado = janela.get_keyboard()

    while True:

        if teclado.key_pressed("ESC"):
            menu_principal()

        janela.update()


def menu_niveis():
    # CRIANDO A TELA
    janela = Window(1200, 600)
    janela.set_title('MENU NIVEIS')

    # CRIANDO O MOUSE
    mouse = janela.get_mouse()

    # CRIANDO TECLADO
    teclado = janela.get_keyboard()

    # IMPORTANDO AS IMAGENS ESTÁTICAS
    fundo_esquerdo = Sprite("imagens_menu_niveis/tela_fundo.png")
    fundo_direito = Sprite("imagens_menu_niveis/tela_fundo.png")
    titulo = Sprite("imagens_menu_niveis/titulo_niveis.png")
    botao_facil_estatico = Sprite("imagens_menu_niveis/botao_facil_estatico.png")
    botao_medio_estatico = Sprite("imagens_menu_niveis/botao_medio_estatico.png")
    botao_dificil_estatico = Sprite("imagens_menu_niveis/botao_dificil_estatico.png")

    # IMPORTANDO BOTÕES HOOVER 
    botao_facil_hoover = Sprite("imagens_menu_niveis/botao_facil_hoover.png")
    botao_medio_hoover = Sprite("imagens_menu_niveis/botao_medio_hoover.png")
    botao_dificil_hoover = Sprite("imagens_menu_niveis/botao_dificil_hoover.png")

    # IMPORTANDO BOTÕES CLICK
    botao_facil_click = Sprite("imagens_menu_niveis/botao_facil_click.png")
    botao_medio_click = Sprite("imagens_menu_niveis/botao_medio_click.png")
    botao_dificil_click = Sprite("imagens_menu_niveis/botao_dificil_click.png")

    # POSICIONANDO AS IMAGENS ESTÁTICAS
    fundo_direito.set_position(0, 0)
    fundo_esquerdo.set_position(janela.width / 2, 0)
    titulo.set_position((janela.width - titulo.width) / 2, 40)
    botao_facil_estatico.set_position((janela.width - botao_facil_estatico.width) / 2 + 10, 200)
    botao_medio_estatico.set_position((janela.width - botao_medio_estatico.width) / 2 + 10, 300)
    botao_dificil_estatico.set_position((janela.width - botao_dificil_estatico.width) / 2 + 10, 400)

    while True:

        # DESENHANDO AS IMAGENS ESTÁTICAS NA TELA
        fundo_direito.draw()
        fundo_esquerdo.draw()
        titulo.draw()
        botao_facil_estatico.draw()
        botao_medio_estatico.draw()
        botao_dificil_estatico.draw()

        # MUDANDO BOTÕES SE HOUVER HOOVER
        if mouse.is_over_object(botao_facil_estatico):
            botao_facil_hoover.set_position((janela.width - botao_facil_estatico.width) / 2 + 10, 200)
            botao_facil_hoover.draw()

        if mouse.is_over_object(botao_medio_estatico):
            botao_medio_hoover.set_position((janela.width - botao_medio_estatico.width) / 2 + 10, 300)
            botao_medio_hoover.draw()

        if mouse.is_over_object(botao_dificil_estatico):
            botao_dificil_hoover.set_position((janela.width - botao_dificil_estatico.width) / 2 + 10, 400)
            botao_dificil_hoover.draw()

        # MUDANDO BOTÕES SE HOUVER CLICK
        if mouse.is_button_pressed(True) and mouse.is_over_object(botao_facil_hoover):
            botao_facil_click.set_position((janela.width - botao_facil_hoover.width) / 2 + 10, 200)
            botao_facil_click.draw()

        if mouse.is_button_pressed(True) and mouse.is_over_object(botao_medio_hoover):
            botao_medio_click.set_position((janela.width - botao_medio_hoover.width) / 2 + 10, 300)
            botao_medio_click.draw()

        if mouse.is_button_pressed(True) and mouse.is_over_object(botao_dificil_hoover):
            botao_dificil_click.set_position((janela.width - botao_dificil_hoover.width) / 2 + 12, 400)
            botao_dificil_click.draw()

        if teclado.key_pressed("ESC"):
            menu_principal()

        janela.update()


def tela_do_jogo():
    # CRIANDO A TELA
    janela = Window(1200, 600)
    janela.set_title('SPACE INVADERS')

    # IMPORTANDO A NAVE, OS INIMIGOS, TIROS E FUNDO
    nave = Sprite("imagens_jogo_principal/nave.png")
    tiros: list[Sprite] = []  # Sprite("imagens_jogo_principal/tiro.png")
    # inimigos= Sprite("imagens_jogo_principal/inimigos.png")
    fundo_esquerdo = Sprite("imagens_menu_niveis/tela_fundo.png")
    fundo_direito = Sprite("imagens_menu_niveis/tela_fundo.png")

    # POSICIONANDO A NAVE E DOS TIROS
    fundo_direito.set_position(0, 0)
    fundo_esquerdo.set_position(janela.width / 2, 0)
    nave.set_position((janela.width - nave.width) / 2, janela.height - 90)

    # CRIANDO TECLADO
    teclado = janela.get_keyboard()

    # CRIANDO A VELOCIDADE DE MOVIMENTO DA NAVE
    velocidade_direita_nave = 300
    velocidade_esquerda_nave = -300

    # CRIANDO A VELOCIDADE DOS TIROS
    velocidade_tiros = -300

    tempo = pygame.time.Clock()
    frame_mod = 0

    inimigos = Inimigos(tiros)

    while True:
        tempo.tick(60 - inimigos.num_inimigos)
        janela.set_title(f'SPACE INVADERS    FPS: {int(tempo.get_fps())}')

        frame_mod += 1
        if frame_mod >= 30:
            frame_mod = 0

        fundo_direito.draw()
        fundo_esquerdo.draw()
        nave.draw()

        # MOVIMENTAÇÃO DA NAVE
        if teclado.key_pressed("RIGHT"):
            nave.move_x(velocidade_direita_nave * janela.delta_time())
        if teclado.key_pressed("LEFT"):
            nave.move_x(velocidade_esquerda_nave * janela.delta_time())

        if nave.x >= (janela.width - nave.width):
            nave.x = janela.width - nave.width
            velocidade_direita_nave = 0
            velocidade_esquerda_nave = -300

        if nave.x <= 0:
            nave.x = 0
            velocidade_esquerda_nave = 0
            velocidade_direita_nave = 300

        if 0 < nave.x < (janela.width - nave.width):
            velocidade_direita_nave = 300
            velocidade_esquerda_nave = -300

        # MOVIMENTAÇÃO DOS TIROS 
        if teclado.key_pressed("SPACE") and len(tiros) < 3 and (frame_mod == 0 or frame_mod == 10 or frame_mod == 20):
            tiro = Sprite("imagens_jogo_principal/tiro.png")
            tiro.x = nave.x + (nave.width//2)
            tiro.y = nave.y
            tiros.append(tiro)

        for tiro in tiros:
            if tiro.y > -20:
                tiro.move_y(velocidade_tiros * janela.delta_time())
            else:
                tiros.remove(tiro)
            tiro.draw()

        # SAÍDA DA TELA
        if teclado.key_pressed("ESC"):
            return

        inimigos.update()

        janela.update()


def menu_principal():
    # CRIANDO A JANELA
    janela = Window(1200, 600)
    janela.set_title('MENU PRINCIPAL')

    # CRIANDO O MOUSE
    mouse = janela.get_mouse()

    # CRIANDO TECLADO
    teclado = janela.get_keyboard()

    # IMPORTANDO AS IMAGENS ESTÁTICAS DO MENU
    fundo_esquerdo = Sprite("imagens_menu_principal/tela_fundo.png")
    fundo_direito = Sprite("imagens_menu_principal/tela_fundo.png")
    titulo = Sprite("imagens_menu_principal/title_space.png")
    subtitulo = Sprite("imagens_menu_principal/subtitle_invaders.png")
    botao_jogar_estatico = Sprite("imagens_menu_principal/botao_jogar_estatico.png")
    botao_nivel_estatico = Sprite("imagens_menu_principal/botao_nivel_estatico.png")
    botao_ranking_estatico = Sprite("imagens_menu_principal/botao_ranking_estatico.png")
    botao_sair_estatico = Sprite("imagens_menu_principal/botao_sair_estatico.png")

    # IMPORTANDO OS BOTÕES DE HOOVER
    botao_jogar_hoover = Sprite("imagens_menu_principal/botao_jogar_hoover.png")
    botao_nivel_hoover = Sprite("imagens_menu_principal/botao_nivel_hoover.png")
    botao_ranking_hoover = Sprite("imagens_menu_principal/botao_ranking_hoover.png")
    botao_sair_hoover = Sprite("imagens_menu_principal/botao_sair_hoover.png")

    # IMPORTANDO OS BOTÕES DE CLICK
    botao_jogar_click = Sprite("imagens_menu_principal/botao_jogar_click.png")
    botao_nivel_click = Sprite("imagens_menu_principal/botao_nivel_click.png")
    botao_ranking_click = Sprite("imagens_menu_principal/botao_ranking_click.png")
    botao_sair_click = Sprite("imagens_menu_principal/botao_sair_click.png")

    # POSICIONANDO AS IMAGENS ESTÁTICAS
    fundo_direito.set_position(0, 0)
    fundo_esquerdo.set_position(janela.width / 2, 0)
    titulo.set_position((janela.width - titulo.width) / 2, 25)
    subtitulo.set_position((janela.width - subtitulo.width) / 2 + 10, 140)
    botao_jogar_estatico.set_position((janela.width - botao_jogar_estatico.width) / 2 + 10, 250)
    botao_nivel_estatico.set_position((janela.width - botao_nivel_estatico.width) / 2 + 8, 330)
    botao_ranking_estatico.set_position((janela.width - botao_ranking_estatico.width) / 2 + 10, 410)
    botao_sair_estatico.set_position((janela.width - botao_sair_estatico.width) / 2 + 8, 490)

    while True:

        # DESENHANDO AS IMAGENS ESTÁTICAS NA TELA
        fundo_direito.draw()
        fundo_esquerdo.draw()
        titulo.draw()
        subtitulo.draw()
        botao_jogar_estatico.draw()
        botao_nivel_estatico.draw()
        botao_ranking_estatico.draw()
        botao_sair_estatico.draw()

        # MUDANDO OS BOTÕES SE HOVER HOOVER NA TELA MENU
        if mouse.is_over_object(botao_jogar_estatico):
            botao_jogar_hoover.set_position((janela.width - botao_jogar_estatico.width) / 2 + 10, 250)
            botao_jogar_hoover.draw()

        if mouse.is_over_object(botao_nivel_estatico):
            botao_nivel_hoover.set_position((janela.width - botao_nivel_estatico.width) / 2 + 8, 330)
            botao_nivel_hoover.draw()

        if mouse.is_over_object(botao_ranking_estatico):
            botao_ranking_hoover.set_position((janela.width - botao_ranking_estatico.width) / 2 + 10, 410)
            botao_ranking_hoover.draw()

        if mouse.is_over_object(botao_sair_estatico):
            botao_sair_hoover.set_position((janela.width - botao_sair_estatico.width) / 2 + 8, 490)
            botao_sair_hoover.draw()

        # MUDANDO OS BOTÕES SE HOUVER CLICK NA TELA DO MENU
        if mouse.is_button_pressed(True) and mouse.is_over_object(botao_jogar_hoover):
            botao_jogar_click.set_position((janela.width - botao_jogar_hoover.width) / 2 + 10, 250)
            botao_jogar_click.draw()
            tela_do_jogo()

        if mouse.is_button_pressed(True) and mouse.is_over_object(botao_nivel_hoover):
            botao_nivel_click.set_position((janela.width - botao_nivel_hoover.width) / 2 + 8, 330)
            botao_nivel_click.draw()
            menu_niveis()

        if mouse.is_button_pressed(True) and mouse.is_over_object(botao_ranking_hoover):
            botao_ranking_click.set_position((janela.width - botao_ranking_hoover.width) / 2 + 8, 410)
            botao_ranking_click.draw()
            menu_ranking()

        if mouse.is_button_pressed(True) and mouse.is_over_object(botao_sair_hoover):
            botao_sair_click.set_position((janela.width - botao_sair_hoover.width) / 2 + 8, 490)
            botao_sair_click.draw()
            quit()

        janela.update()


menu_principal()
