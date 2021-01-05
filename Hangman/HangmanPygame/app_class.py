import pygame
import sys

pygame.init()

LIGHT_BLUE = (113,197,207)
FPS = 60
WIDTH = 500
HEIGHT = 500

class App:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # put in screen dimensions as parameter
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.bird = pygame.image.load(r'C:\Users\user\Pictures\geek.jpg') 

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_game()
            elif self.state == 'playing':
                self.play_game()
            self.draw_screen()
            self.clock.tick(60) # put in frames per seconf (FPS) in parameter
        pygame.quit()
        sys.exit()

    def start_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.state = 'playing'

    def play_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw_screen(self):
        if self.state == 'start':
            self.screen.fill(LIGHT_BLUE)
            self.draw_text("Welcome to Flappy Bird!", self.screen, [250, 220], 30, (255,255,255), "arial black")
            self.draw_text("(Press enter to start playing)", self.screen, [250, 270], 15, (255,255,255), "arial black")
        elif self.state == 'playing':
            self.screen.fill((255,255,255))
        pygame.display.update()

    def draw_text(self, words, screen, pos, size, color, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0] // 2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)