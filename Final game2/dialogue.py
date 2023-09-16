import pygame as pg
from settings import *


class Dialogue:
    def __init__(self, time, dialogue: str, speaker: str, audio=None, font='fonts/Roboto-Thin.ttf', size=25,
                 name_size=18):
        self.frame_x = 0
        self.frame_y = 490

        self.font = pg.font.Font(font, size)
        self.name_font = pg.font.Font(font, name_size)
        name_img = self.name_font.render(speaker, False, [0, 0, 0], None)

        self.image = pg.image.load("assets/dialogue/frame.png").convert_alpha()
        speaker = pg.image.load(f"assets/dialogue/{speaker}.png").convert_alpha()
        self.image.blits(((speaker, (45, 51)), (name_img, (46, 11))))

        self.passed_time = 0
        self.max_time = time * 1000

        self.dialogue = dialogue.split()
        self.is_line2 = False
        self.falado_line1 = ''
        self.falado_line2 = ''

        self.final_img = None

        self.audio = audio

    def update(self, game):
        if self.passed_time == 0:
            if self.audio:
                pg.mixer.music.load(f"assets/dialogue/sound/{self.audio}.mp3")
                pg.mixer.music.play()

        if self.passed_time < self.max_time:
            # print(round(len(self.dialogue) * (self.passed_time / self.max_time) + 0.5))
            if current_dialogue := self.dialogue[
                int(len(self.dialogue) * (self.passed_time / self.max_time))
            ]:
                if self.is_line2:
                    self.falado_line2 += current_dialogue + ' '
                else:
                    self.falado_line1 += current_dialogue + ' '

                self.dialogue[int(len(self.dialogue) * (self.passed_time / self.max_time))] = None

                if self.font.size(self.falado_line1)[0] > 890:
                    self.is_line2 = True

                img_text1 = self.font.render(self.falado_line1, False, [0, 0, 0], None)
                img_text2 = self.font.render(self.falado_line2, False, [0, 0, 0], None)
                self.final_img = self.image.copy()
                self.final_img.blits(((img_text1, (158, 46)), (img_text2, (158, 118))))

            game.drawer.to_draw.append((4, (self.final_img, self.frame_x, self.frame_y)))

        else:
            if game.player.interact:
                game.dialogue_handler.pop()
            game.drawer.to_draw.append((4, (self.final_img, self.frame_x, self.frame_y)))

        self.passed_time += game.delta_time * 1000


class DialogueHandler:
    def __init__(self, game):
        self.game = game
        self.queue: list[Dialogue | None] = []

    def update(self):
        if len(self.queue) > 0:
            self.queue[0].update(self.game)

    def add(self, dig: Dialogue):
        self.queue.append(dig)

    def pop(self):
        self.queue.pop(0)
