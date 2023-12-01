import math
import pygame as pg

RUST = False
FastMath = True  # Gambiarra para ganhar speed


RES = (800, 600)  # 1280, 720   1366, 736   1260, 736  120, 100

FPS = 60

Player_speed = 200
Player_size = 4
Mouse_sens = 0.005

Posicao_inicial = (50, 50)
Default_angulo = 0

NumThreads = 2

Texture_Res = 128
Tile_size = 64
SCALE = 2
FOV = 60

Render_dist = 20
Sprite_Ren_dist = 2048

Mine_Map_zoom = 24
Mini_Map_position = (2 * Mine_Map_zoom, RES[1] - 13 * Mine_Map_zoom)


RenderWidth = RES[0]
HalfRenderWidth = RenderWidth // 2
RenderHeight = RES[1]
HalfRenderHeight = RenderHeight // 2
HalfFOV = FOV // 2

"""
RenderWidth = RES[0] // SCALE
HalfRenderWidth = RenderWidth // 2
RenderHeight = RES[1] // SCALE
HalfRenderHeight = RenderHeight // 2
HalfFOV = FOV // 2
"""
