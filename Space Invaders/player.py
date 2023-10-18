from pplay.sprite import *
import pygame as pg
from settings import *


class Player(Sprite):
    def __init__(self, image_file='base'):
        super().__init__(f"assets/player/{image_file}.png")

        self.x = HalfWidth - (self.width // 2)
        self.y = Height - self.height - 20

        self.keys = pg.key.get_pressed()
        self.keys_lest = self.keys
        self.speed = PlayerSpeed

    def move_key_x(self, speed):
        self.keys_lest = self.keys
        self.keys = pg.key.get_pressed()

        if self.keys[pg.K_a] and self.x > 20:
            self.set_position(self.x - speed, self.y)

        if self.keys[pg.K_d] and self.x + self.width < Width - 20:
            self.set_position(self.x + speed, self.y)

    def key_click(self, Key_Id) -> bool:
        return self.keys[Key_Id] and not self.keys_lest[Key_Id]

    def center(self) -> tuple[int, int]:
        return self.x + (self.width // 2), self.y - (self.height // 2)

    def set_texture(self, image_file):
        super().__init__(f"assets/player/{image_file}.png")

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
        self.move_key_x(self.speed)

        self.draw()
