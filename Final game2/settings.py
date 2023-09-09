import math

RES = (1280, 720)  # 1280, 720   1366, 736   1260, 736
# RES = (1280, 720)
FPS = 60

Player_speed = 5
Player_size = 20
Mouse_sens = 0.005

Posicao_inicial = (50, 50)
Default_angulo = 0

NumThreads = 2

Tile_size = 64
SCALE = 2
FOV = 60
Render_dist = 20
Mine_Map_zoom = 24
Mini_Map_position = (2 * Mine_Map_zoom, RES[1] - 13 * Mine_Map_zoom)
Screen_distance = (RES[0] / 2) / math.tan(math.radians(FOV/2))
