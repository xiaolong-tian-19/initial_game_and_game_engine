import pygame, sys

"""
CPSC 4160 Initial Game & Game Engine

Name:   George Tian
Email:  xt@g.clemson.edu
"""

class Controller():
    def handle_events(self, paddle1, paddle2, pong, surface, score, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up(dt, surface)
        elif keys[pygame.K_s]:
            paddle1.move_down(dt, surface)

        if keys[pygame.K_UP]:
            paddle2.move_up(dt, surface)
        elif keys[pygame.K_DOWN]:
            paddle2.move_down(dt, surface)

        pong.move(paddle1, paddle2, surface, score, dt)
