#import modules
from os import listdir
from pygame import image as im, transform

#import user modules
from options.MainOptions import I_SCALE

#class to handle images
class Images():
    def __init__(self, directory):
        self.directory = directory
        self.image_list = []
        self.create_image_list()

    def create_image_list(self):
        self.image_list = list(listdir(self.directory))

    def get_image(self, letter:str):
        for image in self.image_list:
            if image[0].lower() == letter.lower():
                image_dir = self.directory + '\\' + image
                break
        letter_image = im.load(image_dir)
        letter_image = self.rescale_image(letter_image)
        return letter_image

    def rescale_image(self, letter_image:im):
        i_height = letter_image.get_height()
        i_width = letter_image.get_width()
        h_w_ratio = i_height / i_width
        if i_width > I_SCALE[0]:
            i_width = I_SCALE[0]
            i_height = i_width * h_w_ratio
        if i_height > I_SCALE[1]:
            i_height = I_SCALE[1]
            i_width = i_height / h_w_ratio
        return transform.scale(letter_image, (i_width, i_height))

    def get_hidden_image_name(self, letter:str):
        for image in self.image_list:
            if image[0].lower() == letter.lower():
                return '_' + image[1:-4].replace('_', ' ')
            
    def get_image_name(self, letter:str):
        for image in self.image_list:
            if image[0].lower() == letter.lower():
                return image[:-4].capitalize().replace('_', ' ')