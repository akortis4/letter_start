#import modules
import pygame as pg
from os import getcwd
from string import ascii_uppercase
from random import shuffle

#import user modules
import options.MainOptions as mo
from modules.ImageHandler import Images

class LetterStart():
    def __init__(self):
        self.game = pg.init()
        self.run_game = True
        self.display = pg.display.set_mode((mo.S_WIDTH, mo.S_HEIGHT))
        self.font = pg.font.SysFont(mo.F_STYLE, mo.F_SIZE)
        self.alphabet = list(ascii_uppercase)
        self.images = Images(getcwd() + mo.I_DIR)

    def run(self):
        while self.run_game:
            self.display.fill(mo.GRAY)
            self.draw_objects()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run_game = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.run_game = False
            pg.display.flip()

    def draw_objects(self):
        image = self.images.get_image(self.alphabet[8])
        image_name = self.images.get_hidden_image_name(self.alphabet[8])
        self.display.blit(image, (mo.I_X, mo.I_Y))
        self.display.blit(self.font.render(image_name, True, mo.BLUE), (mo.F_X, mo.F_Y))

if __name__ == '__main__':
    LetterStart().run()