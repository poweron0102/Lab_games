import math
import pygame as pg

from Test.in_game.player import Player
from Test.settings import *


class Map:
    def __init__(self, game):
        self.game = game

        self.walls: dict[any, Map.Wall] = {}
        self._wall_cont = 10000

        self.create_map()

    def add_wall(self, x: [int], y: [int], z: [int]):
        """
        Passar uma lista de 4 valores para x, y, z.
        """
        self.walls[self._wall_cont] = Map.Wall(x, y, z)
        self._wall_cont += 1

    def create_map(self):
        self.add_wall([40, 40, 40, 40], [10, 290, 10, 290], [0, 0, 30, 30])

    class Wall:
        x: list[float]
        y: list[float]
        z: list[float]
        color: tuple[int, int, int]

        def __init__(self, x: list[float], y: list[float], z: list[float]):
            """
            Passar uma lista de 4 valores para x, y, z.
            """
            self.x = x
            self.y = y
            self.z = z
            self.color = (0, 255, 110)

        def __copy__(self):
            return Map.Wall(self.x, self.y, self.z)

        def draw(self, player: Player, screen):
            for i in range(len(self.x)):
                # Calculate the relative coordinates of the wall based on player position and angle
                rel_x = self.x[i] - player.x
                rel_y = self.y[i] - player.y

                # Apply rotation to the wall based on player's angle
                wall_x = rel_x * math.cos(player.ang) - rel_y * math.sin(player.ang)
                wall_y = rel_x * math.sin(player.ang) + rel_y * math.cos(player.ang)

                # Calculate the distance to the wall for depth perception
                distance = math.sqrt(wall_x ** 2 + wall_y ** 2)

                # Correct for player's field of view (optional)
                wall_x_corrected = wall_x * math.cos(player.look) - wall_y * math.sin(player.look)
                wall_y_corrected = wall_x * math.sin(player.look) + wall_y * math.cos(player.look)

                # Calculate the wall height based on its distance
                wall_height = self.z[i] * player.height / distance

                # Calculate the top and bottom y-coordinates of the wall slice to draw
                wall_top = int(SH2 - wall_height / 2)
                wall_bottom = int(SH2 + wall_height / 2)

                # Draw the wall slice
                pg.draw.rect(screen, self.color, (i * 10, wall_top, 10, wall_height))

    def draw(self):
        for key, wall in self.walls.items():
            wall.draw(self.game.player, self.game.game_runner.screen)

