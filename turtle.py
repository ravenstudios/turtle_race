from constants import *
import pygame

class Turtle(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, y, color):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.x = 100
        self.y = y
        self.color = color
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(self.color)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (self.x, self.y)
        self.speed = 5


    def update(self):
        self.rect.left += self.speed
