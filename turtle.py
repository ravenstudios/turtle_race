from constants import *
import pygame, random, datetime

class Turtle(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, name, y, color):
        super().__init__()
        self.name = name
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
        self.rdm_min = 0
        self.rdm_max = 3

        self.can_start = False

        self.ended_race = False
        self.start_time = 0
        self.end_time = 0
        self.top_speed = 0



    def update(self):

        if self.can_start:

            speed = self.speed * random.randint(self.rdm_min, self.rdm_max)

            if speed > self.top_speed:
                self.top_speed = speed

            self.rect.left += speed

        if self.rect.right > FINISH_LINE:
            self.ended_race = True
            self.rect.left = FINISH_LINE
            self.end_time = datetime.datetime.now()
            self.can_start = False



    def start(self):
        self.start_time = datetime.datetime.now()
        self.can_start = True

    def get_results(self):
        results = {
            "name": self.name,
            "start": self.start_time,
            "end": self.end_time,
            "top_speed": self.top_speed
        }
        return results
