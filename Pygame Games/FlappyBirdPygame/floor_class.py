import pygame
from app_class import *

class Floor:
    def __init__(self, app):
        self.floor = pygame.transform.scale(pygame.image.load(r'./images/floor.png'), (320, 112))
        self.floorX_pos = [0, 320, 640, 955]
        self.app = app
        self.y = 410
           
    def draw_floor(self, state):
        self.app.screen.blit(self.floor, (self.floorX_pos[0], 410))
        self.app.screen.blit(self.floor, (self.floorX_pos[1], 410))
        self.app.screen.blit(self.floor, (self.floorX_pos[2], 410))
        self.app.screen.blit(self.floor, (self.floorX_pos[3], 410))
        if state == "playing":
            for i in range(len(self.floorX_pos)):
                self.floorX_pos[i] -= self.app.game_speed
            if self.floorX_pos[0] + 320 < 0:
                self.floorX_pos[0] = self.floorX_pos[3] + 320
            if self.floorX_pos[1] + 320 < 0:
                self.floorX_pos[1] = self.floorX_pos[0] + 320
            if self.floorX_pos[2] + 320 < 0:
                self.floorX_pos[2] = self.floorX_pos[1] + 320 
            if self.floorX_pos[3] + 320 < 0:
                self.floorX_pos[3] = self.floorX_pos[2] + 320