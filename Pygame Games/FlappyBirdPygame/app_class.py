import pygame, sys, random
from floor_class import *
from pipe_class import *

pygame.init()

# Game settings
FPS = 60
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 495
BIRD_X = 70
GRAVITY = 0.25
JUMP_STRENGTH = 5
MIN_PIPE = 380
MAX_PIPE = 180
GAME_SPEED = 3
PIPE_DIST_TIME = 1300
PIPE_GAP = 130
PIPE_STEP = 20       # increase for steeper drops and climbs


# Creating SPAWN_PIPE event and triggering the event every second
SPAWN_PIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE, PIPE_DIST_TIME) # Time in milliseconds (1000 ms = 1 sec)

class App:

    def __init__(self):

        # System
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

        self.game_speed = GAME_SPEED

        # Images
        self.bird = pygame.transform.scale(pygame.image.load(r'./images/bird.png'), (47, 33)) 
        self.bg = pygame.transform.scale(pygame.image.load(r'./images/bg.png'), (750, 420)) 
        
        # Bird movement
        self.birdY = 225
        self.bird_movement = 0
        
        # Collision
        self.collided = False

        # Floor object
        self.base = Floor(self)

        # Pipe lists
        self.bottom_pipe_list = []
        self.top_pipe_list = []

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_game()
            elif self.state == 'playing':
                self.play_game()
                self.collision_detection()
                if self.collided or self.birdY > 375:
                    self.reset()
                    self.state = 'game_over'
            elif self.state == 'game_over':
                self.start_game()
            self.draw_screen()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def start_game(self):
        # events --> you typing a letter from your keyboard or you clicking something on the application
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "playing"
                self.collided = False

    def draw_screen(self):
        if self.state == 'start':
            self.screen.blit(self.bg, (0,0))
            self.draw_text("Welcome to Flappy Bird!", self.screen, [375, 130], 30, (255,255,255), "arial black")
            self.draw_text("(Press enter to start playing)", self.screen, [375, 180], 15, (255,255,255), "arial black")
        elif self.state == 'playing':
            self.screen.fill((255,255,255))
            self.screen.blit(self.bg, (0,0))
            self.draw_pipes()
            self.screen.blit(self.bird, (BIRD_X, self.birdY))
        elif self.state == 'game_over':
            self.screen.blit(self.bg, (0,0))
            self.draw_text("You Lost!", self.screen, [375, 130], 30, (255,255,255), "arial black")
            self.draw_text("(Press enter to play again)", self.screen, [375, 180], 15, (255,255,255), "arial black")
        self.base.draw_floor(self.state)
        pygame.display.update()

    def play_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.birdY > 33:
                    self.bird_movement = 0
                    self.bird_movement -= JUMP_STRENGTH
            self.create_pipe(event)
        self.move_bird()
    
    def move_bird(self):
        self.bird_movement += GRAVITY
        self.birdY += self.bird_movement

    def create_pipe(self, event):
        if event.type == SPAWN_PIPE:
            bottom_pipe = Pipe(self, int(random.randrange(MAX_PIPE, MIN_PIPE, PIPE_STEP))) # not using randint() because I want step
            top_pipe = Pipe(self, bottom_pipe.posY - (PIPE_GAP + 409))
            self.bottom_pipe_list.append(bottom_pipe)
            self.top_pipe_list.append(top_pipe)

    def draw_pipes(self):
        for bottom_pipe in self.bottom_pipe_list:
            self.screen.blit(bottom_pipe.pipe_img, (bottom_pipe.posX, bottom_pipe.posY))
            bottom_pipe.move_pipe()
            if bottom_pipe.posX < - 300:
                self.bottom_pipe_list.remove(bottom_pipe)
        for top_pipe in self.top_pipe_list:
            self.screen.blit(pygame.transform.flip((top_pipe.pipe_img), False, True), (top_pipe.posX, top_pipe.posY))
            top_pipe.move_pipe()
            if top_pipe.posX < - 300:
                self.top_pipe_list.remove(top_pipe)
    
    def collision_detection(self):
        for bottom_pipe in self.bottom_pipe_list:
            if (BIRD_X + 47) >= bottom_pipe.posX and BIRD_X <= (bottom_pipe.posX + 71):
                if (self.birdY + 33) >= bottom_pipe.posY or self.birdY <= bottom_pipe.posY - PIPE_GAP:
                    self.collided = True

    def draw_text(self, words, screen, pos, size, color, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0] // 2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def reset(self):
        self.bird_movement = 0
        self.birdY = 225
        self.bottom_pipe_list.clear()
        self.top_pipe_list.clear()