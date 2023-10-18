from pplay.sprite import *
import pygame as pg
from settings import *
from player import *


class ArrowHandle:
    def __init__(self, player: Player):
        self.arrows = []
        self.player = player

    def update(self):
        for arrow in self.arrows:
            arrow.update()
            if arrow.should_be_deleted:
                self.arrows.remove(arrow)

        if self.player.key_click(pg.K_SPACE) and len(self.arrows) < MaxArrows:
            self.arrows.append(Arrow(self.player))


class Arrow(Sprite):
    def __init__(self, player: Player, image_file='base'):
        super().__init__(f"assets/arrow/{image_file}.png")

        self.speed = ArrowSpeed
        self.x = player.center()[0] - (self.width // 2)
        self.y = Height - 105
        self.should_be_deleted = False

    def collide(self, mapa: list['Shirogane']) -> bool:
        """TODO"""
        return False

    def draw(self):
        if not self.drawable:
            return

        # Clips the frame (rect on the image)
        clip_rect = pygame.Rect(
            self.curr_frame * self.width, 0, self.width, self.height
        )

        # Updates the pygame rect based on new positions values
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Blits the image with the rect and clip_rect clipped
        pg.display.get_surface().blit(self.image, self.rect, area=clip_rect)

    def update(self):
        self.move_y(self.speed)
        self.draw()

        if self.y + self.height < 0 or self.collide([1, 2, 3]):
            self.should_be_deleted = True
