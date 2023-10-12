import math

from pplay.gameimage import GameImage
from pplay.window import *
from pplay.sprite import *
import pygame as pg

width, height = 1280, 720
janela = Window(width, height)
teclado = janela.keyboard

default_speed_boll = 450
default_speed_bar = 200

fundo = GameImage("fundo.png")

# bola -=-=-=-=-=-=-=-=-=-=-=-
ball = Sprite("Riri.png")
ball.image = pg.transform.scale_by(ball.image, 0.06)
ball.width = ball.image.get_width()
ball.height = ball.image.get_height()

# Barra 1 -=-=-=-=-=-=-=-=-=-=-=-
barra1 = Sprite("barra.png")
barra1.image = pg.transform.scale_by(barra1.image, 0.3)
barra1.width = barra1.image.get_width()
barra1.height = barra1.image.get_height()
barra1.x = 10
# Barra 2 -=-=-=-=-=-=-=-=-=-=-=-
barra2 = Sprite("barra.png")
barra2.image = pg.transform.scale_by(barra1.image, 0.3)
barra2.image = pg.transform.flip(barra1.image, True, False)
barra2.width = barra1.image.get_width()
barra2.height = barra1.image.get_height()
barra2.x = width - barra2.width - 10
# -=-=-=-=-=-=-=-=-=-=-=-


janela.set_title("Nathan")
ball.set_position((width - ball.width) / 2, (height - ball.height) / 2)

ball_speed = [default_speed_boll, default_speed_boll]
barra_speed_P = default_speed_bar
barra_speed_Ai = default_speed_bar


class LifeHandler:
    def __init__(self):
        self.janela = pg.display.get_surface()

        vida1 = pg.image.load("vida1.png").convert_alpha()
        vida1 = pg.transform.scale_by(vida1, 0.15)
        self.vida1 = vida1

        vida2 = pg.image.load("vida2.png").convert_alpha()
        vida2 = pg.transform.scale_by(vida2, 0.15)
        self.vida2 = vida2

        self.pont = [0, 0]

    def update(self):
        global barra_speed_P
        global barra_speed_Ai
        if self.pont[0] > 7 or self.pont[1] > 7:
            self.pont = [0, 0]
            barra_speed_P = default_speed_bar
            barra_speed_Ai = default_speed_bar
        for id in range(self.pont[0]):
            self.janela.blit(
                self.vida1,
                (30 + self.vida1.get_width() * id, 30)
            )
        for id in range(self.pont[1]):
            self.janela.blit(
                self.vida2,
                (width - 30 - (self.vida2.get_width() * (id + 1)), 30)
            )


life_handler = LifeHandler()


def update_ball(ball):
    global barra_speed_P
    global barra_speed_Ai

    ball.move_x(ball_speed[0] * janela.delta_time())
    ball.move_y(ball_speed[1] * janela.delta_time())

    if ball.x + ball.width > width:
        ball_speed[0] = -math.fabs(ball_speed[0])
        life_handler.pont[0] += 1
        barra_speed_Ai += 30
        barra_speed_P -= 30
        ball.set_position((width - ball.width) / 2, (height - ball.height) / 2)
    elif ball.x < 0:
        ball_speed[0] = math.fabs(ball_speed[0])
        life_handler.pont[1] += 1
        barra_speed_P += 30
        barra_speed_Ai -= 30
        ball.set_position((width - ball.width) / 2, (height - ball.height) / 2)

    if ball.y + ball.height > height:
        ball_speed[1] = -math.fabs(ball_speed[1])
    elif ball.y < 0:
        ball_speed[1] = math.fabs(ball_speed[1])


def update_barra(barra: Sprite, up, down):
    if teclado.key_pressed(up) and barra.y > 0:
        barra.move_y(-barra_speed_P * janela.delta_time())
    if teclado.key_pressed(down) and barra.y + barra.height < height:
        barra.move_y(barra_speed_P * janela.delta_time())


def colide(bar1: Sprite, bar2: Sprite, boll: Sprite):
    if boll.collided(bar1):
        ball_speed[0] = math.fabs(ball_speed[0])
    elif boll.collided(bar2):
        ball_speed[0] = -math.fabs(ball_speed[0])


def bar_ai(bar: Sprite):
    bar_CY = bar.y + (bar.height / 2)
    ball_CY = ball.y + (ball.height / 2)

    if ball_CY < bar_CY:
        bar.move_y(-barra_speed_Ai * janela.delta_time())
    else:
        bar.move_y(barra_speed_Ai * janela.delta_time())


while True:
    fundo.draw()
    life_handler.update()

    update_ball(ball)
    colide(barra1, barra2, ball)

    ball.draw()

    update_barra(barra1, "w", "s")
    # update_barra(barra2, "up", "down")
    bar_ai(barra2)
    barra1.draw()
    barra2.draw()

    janela.update()
