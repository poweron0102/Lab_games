import pygame as pg


class Button:
    def __init__(
            self,
            x, y,
            text: str,
            font_size=25,
            color=(216, 53, 64),
            font="BIG_JOHN.otf",
            img_base="button_base",
            img_hover="button_hover",
            function=None, arg=None
    ):
        self.img = None
        self.pressed = True

        self.img_base = pg.image.load(f"assets/gui/{img_base}.png").convert_alpha()
        self.img_hover = pg.image.load(f"assets/gui/{img_hover}.png").convert_alpha()

        self.x, self.y = x, y

        self.width = self.img_base.get_width()
        self.height = self.img_base.get_height()

        font = pg.font.Font(f"assets/fonts/{font}", font_size)
        self.text_img = font.render(text, False, color)
        self.font_x = self.x + (self.width // 2 - self.text_img.get_width() // 2)
        self.font_y = self.y + (self.height // 2 - self.text_img.get_height() // 2)

        self.func = function
        self.arg = arg

    def update(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            self.img = self.img_hover
            pressed = pg.mouse.get_pressed()[0]
            if pressed and not self.pressed:
                if self.func:
                    if self.arg:
                        self.func(self.arg)
                    else:
                        self.func()
            self.pressed = pressed
        else:
            self.img = self.img_base

        if self.img:
            pg.display.get_surface().blit(
                self.img,
                (self.x, self.y)
            )
            pg.display.get_surface().blit(
                self.text_img,
                (self.font_x, self.font_y)
            )
