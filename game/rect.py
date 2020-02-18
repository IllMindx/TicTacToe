import pygame


class Rect(pygame.Rect):

    def __init__(self, x, y, width, height):
        super(Rect, self).__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.draw = ''
    
    def setDraw(self, draw):
        self.draw = draw
