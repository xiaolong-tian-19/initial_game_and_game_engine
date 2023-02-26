import pygame, sys
from view import View
from models import Ball, Paddle, Score, Surface
from controller import Controller

"""
CPSC 4160 Initial Game & Game Engine

Name:   George Tian
Email:  xt@g.clemson.edu
"""


pygame.init()

view = View(caption="Pong Game", SCREEN_HEIGHT=400, SCREEN_WIDTH=800, screen_color = (200, 200, 200), font_size=36)

surface = Surface(view)
pong = Ball(radius=5, center=[400, 50], direction=[-1, 1], magnitude=0.4)
paddle1 = Paddle(SCREEN_HEIGHT=view.SCREEN_HEIGHT, SCREEN_WIDTH=view.SCREEN_WIDTH, paddleSpeed=1, paddlePos=Paddle.LEFT)
paddle2 = Paddle(SCREEN_HEIGHT=view.SCREEN_HEIGHT, SCREEN_WIDTH=view.SCREEN_WIDTH, paddleSpeed=1, paddlePos=Paddle.RIGHT)
score = Score(player1_score=0, player2_score=0, end_score=11)

controller = Controller()

fps = 60
clock = pygame.time.Clock()
clock.tick(fps)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick()

    controller.handle_events(paddle1, paddle2, pong, surface, score, dt)

    view.display(pong, paddle1, paddle2, pong_color=[255, 0, 0], paddle_color=(255, 0, 0), score=score)

    if score.check_win() == True:
        break

view.end_screen(score)


