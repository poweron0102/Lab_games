import math
import pygame as pg

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
        x: [float]
        y: [float]
        z: [float]

        def __init__(self, x: [int], y: [int], z: [int]):
            """
            Passar uma lista de 4 valores para x, y, z.
            """
            self.x = []
            self.y = []
            self.z = []
            for a in x: self.x.append(a)
            for a in y: self.y.append(a)
            for a in z: self.z.append(a)

        def offset(self, x, y, z):
            for a in range(4): self.x[a] -= x
            for a in range(4): self.y[a] -= y
            for a in range(4): self.z[a] -= z

        def rotate(self, sin, cos):
            # tx, ty, tz = [None]*len(self.x), [None]*len(self.y), [None]*len(self.z)
            tx, ty = [None] * len(self.x), [None] * len(self.y)
            for a in range(len(self.x)): tx[a] = (self.x[a] * cos) - (self.y[a] * sin)
            for a in range(len(self.y)): ty[a] = (self.y[a] * cos) + (self.x[a] * sin)
            # for a in range(len(self.z)): self.z[a] -= z
            self.x, self.y = tx, ty

        def to_screen(self):
            num_wtf = 200
            for a in range(4): self.x[a] = (self.x[a] * num_wtf / self.y[a]) + SW2
            for a in range(4): self.y[a] = (self.z[a] * num_wtf / self.x[a]) + SH2

            for a in range(4):
                if not 0 <= self.x[a] <= SW or not 0 <= self.y[a] <= SH:
                    self = None
                    return

        def get_point(self, id: int):
            return self.x[id], self.y[id], self.z[id]

        def __copy__(self):
            return Map.Wall(self.x, self.y, self.z)

    def draw(self):
        player_x, player_y, player_z = self.game.player.x, self.game.player.y, self.game.player.z
        player_cos, player_sin = math.cos(self.game.player.ang), math.sin(self.game.player.ang)
        # print(player_cos, player_sin)

        for key, wall in self.walls.items():
            wall = wall.__copy__()
            wall.offset(player_x, player_y, player_z)
            wall.rotate(player_sin, player_cos)

            pg.draw.line(
                self.game.game_runner.screen,
                [0, 200, 64],
                (wall.get_point(0)[0], SCREEN_RESOLUTION[1] - wall.get_point(0)[1]),
                (wall.get_point(1)[0], SCREEN_RESOLUTION[1] - wall.get_point(1)[1]),
                2
            )

            wall.to_screen()

            if wall is None: continue

            for a in range(4):
                pg.draw.circle(
                    self.game.game_runner.screen,
                    [50 * a, 60, 64],
                    (wall.get_point(a)[0] * SCALING, SCREEN_RESOLUTION[1] - wall.get_point(a)[1] * SCALING),
                    3
                )
