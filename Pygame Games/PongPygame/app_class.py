import pygame, sys, random

pygame.init()

# Game settings
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 495
FPS = 60
PADDLE_SPEED = 5
BALL_SPEED = 4
AUTO_PADDLE_DIFFICULTY = 1

# Start screen UI
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 40
MULT_BUTTON_POS = [SCREEN_WIDTH/2 + 40, SCREEN_HEIGHT/2, BUTTON_WIDTH, BUTTON_HEIGHT]
SING_BUTTON_POS = [SCREEN_WIDTH/2 - 180, SCREEN_HEIGHT/2, BUTTON_WIDTH, BUTTON_HEIGHT]
BUTTON_FONT_SIZE = 18
BALL_SIZE = 8

# Game UI
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 80
PADDLE_X_OFFSET = 2
PADDLE_GAP_OFFSET = 10
SCORE_FONT_SIZE = 130
BG_COLOR = pygame.Color("#FFFFFF")

class App:

    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.mouse = pygame.mouse.get_pos()
        self.running = True
        self.state = "start"
        self.lPaddle_Y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
        self.rPaddle_Y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
        self.ballX = SCREEN_WIDTH // 2
        self.ballY = SCREEN_HEIGHT // 2
        self.ball_speed = BALL_SPEED
        self.ball_velX = random.choice([BALL_SPEED, -BALL_SPEED])
        self.ball_velY = random.choice([-BALL_SPEED, BALL_SPEED])
        self.l_score = 0
        self.r_score = 0

    def run(self):
        while self.running:
            if self.state == "start":
                self.start_game()
                self.l_score = 0
                self.r_score = 0  
            elif self.state == "mult" or self.state == "sing":
                self.play_game()
                self.move_paddles()
                self.move_ball()
            self.mouse = pygame.mouse.get_pos()
            self.draw_screen()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    def start_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MULT_BUTTON_POS[0] <= self.mouse[0] <= MULT_BUTTON_POS[0]+BUTTON_WIDTH and MULT_BUTTON_POS[1] <= self.mouse[1] <= MULT_BUTTON_POS[1]+BUTTON_HEIGHT:
                    self.state = "mult"
                elif SING_BUTTON_POS[0] <= self.mouse[0] <= SING_BUTTON_POS[0]+BUTTON_WIDTH and SING_BUTTON_POS[1] <= self.mouse[1] <= SING_BUTTON_POS[1]+BUTTON_HEIGHT:
                    self.state = "sing"

    def play_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = "start"

    def draw_screen(self):
        if self.state == "start":
            self.screen.fill((0, 0, 0))
            self.draw_text("PING PONG", self.screen, [(SCREEN_WIDTH/2), (SCREEN_HEIGHT/2) - 70], 30, (255,255,255), "arial black")
            pygame.draw.rect(self.screen, (255, 255, 255), MULT_BUTTON_POS, border_radius=20, width=3)
            self.draw_text("MULTIPLAYER", self.screen, [(SCREEN_WIDTH/2) + (MULT_BUTTON_POS[2]/2) + (MULT_BUTTON_POS[0]-SCREEN_WIDTH/2), (SCREEN_HEIGHT/2) + (MULT_BUTTON_POS[3]/2) + (MULT_BUTTON_POS[1]-SCREEN_HEIGHT/2)], BUTTON_FONT_SIZE, (255,255,255), "arial")
            pygame.draw.rect(self.screen, (255, 255, 255), SING_BUTTON_POS, border_radius=20, width=3)
            self.draw_text("SINGLE PLAYER", self.screen, [(SCREEN_WIDTH/2) + (SING_BUTTON_POS[2]/2) + (SING_BUTTON_POS[0]-SCREEN_WIDTH/2), (SCREEN_HEIGHT/2) + (SING_BUTTON_POS[3]/2) + (SING_BUTTON_POS[1]-SCREEN_HEIGHT/2)], BUTTON_FONT_SIZE, (255,255,255), "arial")
        elif self.state == "mult" or self.state == "sing":
            self.screen.fill((0, 0, 0))
            self.draw_dashed_line(self.screen, BG_COLOR, 10, 1, 20, 25, SCREEN_WIDTH // 2, 0)
            self.draw_text(str(self.l_score), self.screen, [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2], SCORE_FONT_SIZE, BG_COLOR, "arial")
            self.draw_text(str(self.r_score), self.screen, [(SCREEN_WIDTH * 3) // 4, SCREEN_HEIGHT // 2], SCORE_FONT_SIZE, BG_COLOR, "arial")
            pygame.draw.rect(self.screen, (255, 255, 255), [PADDLE_X_OFFSET, self.lPaddle_Y, PADDLE_WIDTH, PADDLE_HEIGHT])
            pygame.draw.rect(self.screen, (255, 255, 255), [SCREEN_WIDTH-PADDLE_X_OFFSET-PADDLE_WIDTH, self.rPaddle_Y, PADDLE_WIDTH, PADDLE_HEIGHT])
            pygame.draw.circle(self.screen, (255, 255, 255), [self.ballX, self.ballY], BALL_SIZE)
        pygame.display.update()

    def move_paddles(self):
        keys = pygame.key.get_pressed()
        if self.state == "mult":
            if keys[pygame.K_UP] and self.rPaddle_Y > PADDLE_GAP_OFFSET:
                self.rPaddle_Y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and self.rPaddle_Y < SCREEN_HEIGHT - PADDLE_HEIGHT - PADDLE_GAP_OFFSET:
                self.rPaddle_Y += PADDLE_SPEED
            if keys[ord('w')] and self.lPaddle_Y > PADDLE_GAP_OFFSET:
                self.lPaddle_Y -= PADDLE_SPEED
            if keys[ord('s')]  and self.lPaddle_Y < SCREEN_HEIGHT - PADDLE_HEIGHT - PADDLE_GAP_OFFSET:
                self.lPaddle_Y += PADDLE_SPEED
        elif self.state == "sing":
            if keys[pygame.K_UP] and self.lPaddle_Y > PADDLE_GAP_OFFSET:
                self.lPaddle_Y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and self.lPaddle_Y < SCREEN_HEIGHT - PADDLE_HEIGHT - PADDLE_GAP_OFFSET:
                self.lPaddle_Y += PADDLE_SPEED
            if self.ballY + (PADDLE_HEIGHT // 2) < SCREEN_HEIGHT - PADDLE_GAP_OFFSET and self.ballY > (PADDLE_HEIGHT // 2) + PADDLE_GAP_OFFSET:
                if self.ballX > SCREEN_WIDTH // 3:
                    if self.ballY - BALL_SIZE < self.rPaddle_Y:
                        self.rPaddle_Y -= random.randint(AUTO_PADDLE_DIFFICULTY, PADDLE_SPEED + 1)
                    elif self.ballY + BALL_SIZE > self.rPaddle_Y + PADDLE_HEIGHT:
                        self.rPaddle_Y += random.randint(AUTO_PADDLE_DIFFICULTY, PADDLE_SPEED + 1)
                    
    def move_ball(self):
        self.ballX += self.ball_velX
        self.ballY += self.ball_velY
        if (self.ballY + BALL_SIZE) >= SCREEN_HEIGHT or (self.ballY - BALL_SIZE) <= 0:
            self.ball_velY *= -1
        if (self.ballX - BALL_SIZE) <= 0:
            self.r_score += 1
            self.ballX = SCREEN_WIDTH // 2
            self.ballY = SCREEN_HEIGHT // 2
            self.ball_velX = self.ball_speed
            self.ball_velY = random.choice([i for i in range(-self.ball_speed - 1, self.ball_speed + 1) if i not in [0]])
        if (self.ballX + BALL_SIZE) >= SCREEN_WIDTH:
            self.l_score += 1
            self.ballX = SCREEN_WIDTH // 2
            self.ballY = SCREEN_HEIGHT // 2
            self.ball_velX = -self.ball_speed
            self.ball_velY = random.choice([i for i in range(-self.ball_speed - 1, self.ball_speed + 1) if i not in [0]])
        if ((self.ballX - BALL_SIZE - BALL_SPEED) < (PADDLE_X_OFFSET + PADDLE_WIDTH)) and ((self.lPaddle_Y + PADDLE_HEIGHT + BALL_SPEED) > (self.ballY + BALL_SIZE) > (self.lPaddle_Y - BALL_SPEED)):
            self.ball_velX = abs(self.ball_velX)
        if ((self.ballX + BALL_SIZE + BALL_SPEED) > (SCREEN_WIDTH - PADDLE_X_OFFSET - PADDLE_WIDTH)) and ((self.rPaddle_Y + PADDLE_HEIGHT + BALL_SPEED) > (self.ballY + BALL_SIZE) > (self.rPaddle_Y - BALL_SPEED)):
            self.ball_velX = -abs(self.ball_velX)

    def draw_text(self, words, screen, pos, size, color, font_name):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0] // 2
        pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def draw_dashed_line(self, screen, color, dash_length, width, gap, dash_num, x, y):
        start = [x,y]
        end = [x, start[1] + dash_length]
        for i in range(dash_num):
           pygame.draw.line(screen, color, start, end, width)
           start[1] += gap
           end[1] += gap

