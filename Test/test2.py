import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Define textures and other variables
texWidth = 64
texHeight = 64
# Load the image as a texture
texture_image = pygame.image.load('wall_test.png')

# Convert the loaded image into a NumPy array
texture = pygame.surfarray.array3d(texture_image)
#texture = np.random.randint(0, 16777215, (7, texWidth * texHeight), dtype=np.uint32)  # Placeholder for textures
posX = 22.0
posY = 11.5
dirX = -1.0
dirY = 0.0
planeX = 0.0
planeY = 0.66

# Create a buffer to store the pixels
buffer = np.zeros((screenWidth, screenHeight, 3), dtype=np.uint8)

for y in range(screenHeight//2, screenHeight):
    rayDirX0 = dirX - planeX
    rayDirY0 = dirY - planeY
    rayDirX1 = dirX + planeX
    rayDirY1 = dirY + planeY

    p = y - screenHeight / 2
    posZ = 0.5 * screenHeight
    rowDistance = posZ / (p + 0.000001)

    floorStepX = rowDistance * (rayDirX1 - rayDirX0) / screenWidth
    floorStepY = rowDistance * (rayDirY1 - rayDirY0) / screenWidth

    floorX = posX + rowDistance * rayDirX0
    floorY = posY + rowDistance * rayDirY0

    for x in range(screenWidth):
        cellX = int(floorX)
        cellY = int(floorY)

        tx = int(texWidth * (floorX - cellX)) & (texWidth - 1)
        ty = int(texHeight * (floorY - cellY)) & (texHeight - 1)

        floorX += floorStepX
        floorY += floorStepY

        floorTexture = 3
        ceilingTexture = 6

        # Choose texture and draw the pixel
        try:
            color = texture[texWidth * ty + tx][floorTexture]  # [floorTexture][texWidth * ty + tx]
        except IndexError:
            color = texture[0][0]

        buffer[x][y] = color

        # Ceiling (symmetrical, at screenHeight - y - 1 instead of y)
        try:
            color = texture[texWidth * ty + tx][ceilingTexture]  # [ceilingTexture][texWidth * ty + tx]
        except IndexError:
            color = texture[0][0]

        buffer[x][screenHeight - y - 1] = color

# Convert the buffer to a Pygame surface
image = pygame.surfarray.make_surface(buffer)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
