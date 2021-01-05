import pygame
from app_class import *

class Floor:
    def __init__(self, app):
        self.floor = pygame.transform.scale(pygame.image.load(r'C:\Users\krush\OneDrive\Desktop\Side Projects\PythonProjects\FlappyBirdPygame\images\floor.png'), (320, 112))
        self.app = app
        self.floorX1 = 0
        self.floorX2 = 320
        self.floorX3 = 640
        self.floorX4 = 960
        self.y = 410

    def move_floor(self):
        self.floorX1 -= self.app.game_speed
        self.floorX2 -= self.app.game_speed
        self.floorX3 -= self.app.game_speed
        self.floorX4 -= self.app.game_speed

        if self.floorX1 + 320 < 0:
            self.floorX1 = self.floorX4 + 320
        if self.floorX2 + 320 < 0:
            self.floorX2 = self.floorX1 + 320
        if self.floorX3 + 320 < 0:
            self.floorX3 = self.floorX2 + 320
        if self.floorX4 + 320 < 0:
            self.floorX4 = self.floorX3 + 320

    def draw_start_floor(self):
        for x in range(0, 3):
                self.app.screen.blit(self.floor, ((x*320),self.y))

    def draw_playing_floor(self):
        self.app.screen.blit(self.floor, (self.floorX1, self.y))
        self.app.screen.blit(self.floor, (self.floorX2, self.y))
        self.app.screen.blit(self.floor, (self.floorX3, self.y))
        self.app.screen.blit(self.floor, (self.floorX4, self.y))