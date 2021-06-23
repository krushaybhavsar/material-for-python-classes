import pygame
from app_class import *

class Pipe:
    def __init__(self, app, posY):
        self.app = app
        self.posX = 800
        self.posY = posY
        self.pipe_img = pygame.transform.scale(pygame.image.load(r'./images/pipe.png'), (71, 409))

    def draw_pipe(self):
        self.app.screen.blit(self.pipe_img, (self.posX, self.posY))

    def move_pipe(self):
        self.posX -= self.app.game_speed