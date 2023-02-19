#import modules
import pygame as pg
from os import getcwd
from string import ascii_uppercase
from random import shuffle

#import user modules
import options.MainOptions as mo
from modules.ImageHandler import Images
from modules.LetterHandler import Letters

class LetterStart():
    def __init__(self):
        self.game = pg.init()
        self.run_game = True
        self.display = pg.display.set_mode((mo.S_WIDTH, mo.S_HEIGHT))
        self.font = pg.font.SysFont(mo.F_STYLE, mo.F_SIZE)
        self.large_font = pg.font.SysFont(mo.F_STYLE, mo.F_LARGE)
        self.letters = Letters()
        self.images = Images(getcwd() + mo.I_DIR)
        self.correct_guess = False
        self.incorrect_guess = False
        self.answer_string = ''

    def run(self):
        while self.run_game:
            self.display.fill(mo.GRAY)
            self.draw_objects()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run_game = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.run_game = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    if not self.correct_guess:
                        self.letters.check_click(mouse_pos)
                        self.correct_guess = self.letters.check_correct(mouse_pos)
                        self.incorrect_guess = self.letters.check_incorrect(mouse_pos)
                    else:
                        self.check_reset(mouse_pos)
            self.update_answer()
            pg.display.flip()

    def draw_objects(self):
        image = self.images.get_image(self.letters.get_current_letter())
        if self.correct_guess:
            image_name = self.images.get_image_name(self.letters.get_current_letter())
        else:
            image_name = self.images.get_hidden_image_name(self.letters.get_current_letter())
        self.display.blit(image, (mo.I_X, mo.I_Y))
        self.display.blit(self.font.render(image_name, True, mo.BLUE), (mo.F_X, mo.F_Y))
        shift = 0
        for x, g_letter in enumerate(self.letters.get_guess_letters()):
            if self.letters.get_enlarge(x):
                self.display.blit(self.large_font.render(g_letter, True, mo.BLUE), (mo.RL_X, mo.RL_Y + shift))
            else:
                self.display.blit(self.font.render(g_letter, True, mo.BLUE), (mo.RL_X, mo.RL_Y + shift))
            shift += 100
        self.display.blit(self.font.render(self.answer_string, True, mo.GREEN), (mo.A_X, mo.A_Y))
        if self.correct_guess:
            pg.draw.rect(self.display, mo.BLUE, (mo.RL_X, mo.A_Y, mo.R_WIDTH, mo.R_HEIGHT))
            text = pg.font.SysFont(None, mo.R_FONT_SIZE, bold=True)
            reset_text = text.render('NEXT', True, mo.BLACK)
            self.display.blit(reset_text, (mo.RL_X, mo.A_Y))

    def update_answer(self):
        if self.correct_guess:
            self.answer_string = mo.A_TRUE_STRING
        if self.incorrect_guess:
            self.answer_string = mo.A_FALSE_STRING

    def check_reset(self, pos:tuple):
        if mo.RL_X <= pos[0] <= mo.RL_X + mo.R_WIDTH:
            if mo.A_Y <= pos[1] <= mo.A_Y + mo.R_HEIGHT:
                self.next_letter()

    def next_letter(self):
        self.correct_guess = False
        self.incorrect_guess = False
        self.letters.update_index()
        self.letters.set_current_letter()
        self.letters.set_shuffle(True)
        self.letters.reset_size()
        self.answer_string = ''

if __name__ == '__main__':
    LetterStart().run()