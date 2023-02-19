#import modules
from random import shuffle
from string import ascii_uppercase

#import user modules
from options.MainOptions import RL_X, RL_Y

#class to handle letters
class Letters():
    def __init__(self):
        self.letters = list(ascii_uppercase)
        self.guess_letters = []
        self.shuffle_letters = True
        self.current_letter = ''
        self.current_index = 0
        self.letter_positions = []
        self.letter_size = [False for i in range(3)]
        self.initial_shuffle()
        self.set_current_letter()
        self.set_letter_positions()

    def get_guess_letters(self):
        if self.shuffle_letters:
            self.guess_letters = [x.upper() for x in self.letters if x.lower() != self.current_letter.lower()]
            shuffle(self.guess_letters)
            self.guess_letters = self.guess_letters[:2]
            self.guess_letters.append(self.current_letter.upper())
            shuffle(self.guess_letters)
            self.shuffle_letters = False
        return self.guess_letters
    
    def initial_shuffle(self):
        shuffle(self.letters)
    
    def set_current_letter(self):
        self.current_letter = self.letters[self.current_index]

    def get_current_letter(self):
        return self.current_letter
    
    def update_index(self):
        if self.current_index == 25:
            self.current_index = 0
            self.letters = ascii_uppercase
            shuffle(self.letters)
        else:
            self.current_index += 1

    def set_letter_positions(self):
        shift = 0
        for i in range(3):
            self.letter_positions.append(((RL_X, RL_X+30), (RL_Y+shift, RL_Y+shift+40)))
            shift += 100

    def get_enlarge(self, i:int):
        return self.letter_size[i]
    
    def check_click(self, pos:tuple):
        for x, position in enumerate(self.letter_positions):
            self.letter_size[x] = False
            if position[0][0] <= pos[0] <= position[0][1]:
                if position[1][0] <= pos[1] <= position[1][1]:
                    self.letter_size[x] = True

    def check_correct(self, pos:tuple):
        correct = False
        for x, position in enumerate(self.letter_positions):
            if position[0][0] <= pos[0] <= position[0][1]:
                if position[1][0] <= pos[1] <= position[1][1]:
                    if self.guess_letters[x] == self.current_letter:
                        correct = True
        return correct
    
    def check_incorrect(self, pos:tuple):
        incorrect = False
        for x, position in enumerate(self.letter_positions):
            if position[0][0] <= pos[0] <= position[0][1]:
                if position[1][0] <= pos[1] <= position[1][1]:
                    if self.guess_letters[x] != self.current_letter:
                        incorrect = True
        return incorrect

    def reset_size(self):
        for i in range(3):
            self.letter_size[i] = False

    def set_shuffle(self, value:bool):
        self.shuffle_letters = value