import pygame

width, height = 800, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 70, 12
BALL_RADIUS = 10

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("BRICK BREAKER")

class Paddle:
    VEL = 10

    def __init__(self, x, y, width, height, color):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.color = color 

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x -= self.VEL
    
    def move_right(self):
        self.x += self.VEL
    
class Ball:
    VEL = 15

    def __init__(self, x, y, radius, color):
        self.x = x 
        self.y = y 
        self.radius = radius 
        self.color = color 
        self.x_vel = 0
        self.y_vel = -self.VEL

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def draw(win, paddle, ball):
    win.fill(("white"))
    paddle.draw(win)
    ball.draw(win)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    center_x, center_y = width/2 - PADDLE_WIDTH/2, height - PADDLE_HEIGHT - 3
    paddle = Paddle(center_x, center_y, PADDLE_WIDTH, PADDLE_HEIGHT, "black")

    ball = Ball(center_x, center_y - BALL_RADIUS, BALL_RADIUS, "black")

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and paddle.x > 2:
            paddle.move_left()
        if keys[pygame.K_RIGHT] and paddle.x < (width - paddle.width + 2):
            paddle.move_right()

        ball.move()
        if ball.x < BALL_RADIUS or ball.x > (width - BALL_RADIUS):
            ball.set_vel(-ball.x_vel, ball.y_vel)
        if ball.y < BALL_RADIUS:
            ball.set_vel(ball.x_vel, -ball.y_vel)
        if ball.y > (height - BALL_RADIUS):
            ball.x, ball.y = center_x, center_y - BALL_RADIUS
            ball.set_vel(0, -ball.VEL)

        draw(win, paddle, ball)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()