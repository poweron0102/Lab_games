import pygame
import math

# Configurações da janela
WIDTH, HEIGHT = 800, 600
HALF_WIDTH, HALF_HEIGHT = WIDTH // 2, HEIGHT // 2
FOV = math.pi / 3  # Campo de visão (60 graus)
DIST_PROJ_PLANE = (WIDTH / 2) / math.tan(FOV / 2)

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Criar uma Surface para o mapa do jogo
map_surface = pygame.image.load('wall_test.png').convert_alpha()


# Função para desenhar o chão e o teto
def draw_ceiling_and_floor():
    for x in range(WIDTH):
        # Ângulo do raio lançado
        ray_angle = (player_angle - FOV / 2) + (x / WIDTH) * FOV

        for y in range(HALF_HEIGHT, HEIGHT-20):
            # Altura da linha em relação ao plano de projeção
            line_height = HEIGHT / (y - HALF_HEIGHT + 0.0000001)

            # Posição no mapa correspondente ao raio
            map_x = int(player_x + line_height * math.cos(player_angle - ray_angle))
            map_y = int(player_y + line_height * math.sin(player_angle - ray_angle))

            # Cor do chão e do teto (obtenha a cor do mapa do jogo)
            if 0 <= map_x < map_surface.get_width() and 0 <= map_y < map_surface.get_height():
                color = map_surface.get_at((map_x, map_y))
            else:
                color = (255, 255, 255)  # Cor padrão para fora do mapa

            # Desenhe a linha no chão e no teto
            screen.set_at((x, y), color)


# Variáveis do jogador
player_x, player_y = 49, 4
player_angle = 3*math.pi/2

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpe a tela
    #player_x += 0.3
    player_y += 1

    pygame.display.set_caption(f'Cellular Odyssey   FPS: {clock.get_fps() :.1f}')

    screen.fill((0, 0, 0))

    # Desenhe o chão e o teto
    draw_ceiling_and_floor()

    # Atualize a tela
    pygame.display.flip()

    # Controle de FPS
    clock.tick(60)

pygame.quit()
