import pygame, sys
from random import random

"""
CPSC 4160 Initial Game & Game Engine

Name:   George Tian
Email:  xt@g.clemson.edu
"""

class Ball():
    def __init__(self, radius, center, direction, magnitude):
        self.radius = radius
        self.center = center
        self.direction = direction
        self.magnitude = magnitude

        velocity = (self.direction[0]**2 + self.direction[1]**2)**1/2
        self.velocity = [0, 0]
        self.velocity[0] = self.direction[0] / velocity * self.magnitude
        self.velocity[1] = self.direction[1] / velocity * self.magnitude

    def collide_with_paddle_1(self, left, top, width, height, center_x, center_y, radius):
        if center_x - radius < left + width and center_y >= top and center_y <= top + height:
            if center_x > left:
                return True
        return False
    
    def collide_with_paddle_2(self, left, top, width, height, center_x, center_y, radius):
        if center_x + radius > left and center_y >= top and center_y <= top + height:
            if center_x < left + width:
                return True
        return False
    
    def move(self, paddle1, paddle2, surface, score, dt):
        self.center[0] += self.velocity[0] * dt
        self.center[1] += self.velocity[1] * dt

        if self.collide_with_paddle_1(paddle1.paddle.left, paddle1.paddle.top, paddle1.paddle.width, paddle1.paddle.height, self.center[0], self.center[1], self.radius):
            self.velocity[0] *= -1
        if self.collide_with_paddle_2(paddle2.paddle.left, paddle2.paddle.top, paddle2.paddle.width, paddle2.paddle.height, self.center[0], self.center[1], self.radius):
            self.velocity[0] *= -1

        if self.center[0] < -100 * self.radius:
            score.player2_score += 1
            self.center = [surface.SCREEN_WIDTH / 2, self.radius]
            self.velocity[0] = -1
            self.velocity[1] = random() * surface.SCREEN_HEIGHT / (surface.SCREEN_WIDTH / 2)
            velocity = (self.velocity[0]**2 + self.velocity[1]**2)**1/2
            self.velocity[0] = self.velocity[0] / velocity * self.magnitude
            self.velocity[1] = self.velocity[1] / velocity * self.magnitude
        if self.center[0] > surface.SCREEN_WIDTH + 100 * self.radius:
            score.player1_score += 1
            self.center = [surface.SCREEN_WIDTH / 2, self.radius]
            self.velocity[0] = 1
            self.velocity[1] = random() * surface.SCREEN_HEIGHT / (surface.SCREEN_WIDTH / 2)
            velocity = (self.velocity[0]**2 + self.velocity[1]**2)**1/2
            self.velocity[0] = self.velocity[0] / velocity * self.magnitude
            self.velocity[1] = self.velocity[1] / velocity * self.magnitude
        if self.center[1] < self.radius:
            self.velocity[1] *= -1
        if self.center[1] > surface.SCREEN_HEIGHT - self.radius:
            self.velocity[1] *= -1

        


class Surface():

    def __init__(self, view):
        self.surface = view.surface.get_rect()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.surface.width, self.surface.height


class Paddle():
    LEFT = 0
    RIGHT = 1

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, paddleSpeed, paddlePos):
        self.paddleWidth = SCREEN_WIDTH / 80
        self.paddleHeight = SCREEN_HEIGHT / 8
        self.paddleSpeed = paddleSpeed
        self.paddlePos = paddlePos

        if self.paddlePos == self.LEFT:
            self.paddleX, self.paddleY = 0, SCREEN_HEIGHT / 2 - self.paddleHeight / 2
        else:
            self.paddleX, self.paddleY = SCREEN_WIDTH - self.paddleWidth, SCREEN_HEIGHT / 2 - self.paddleHeight / 2

        self.paddle = pygame.Rect(self.paddleX, self.paddleY, self.paddleWidth, self.paddleHeight)

    def move_up(self, dt, surface):
        self.paddle.move_ip(0, -1 * self.paddleSpeed * dt)
        self.paddle.clamp_ip(surface.surface)

    def move_down(self, dt, surface):
        self.paddle.move_ip(0, self.paddleSpeed * dt)
        self.paddle.clamp_ip(surface.surface)


class Score():
    def __init__(self, player1_score, player2_score, end_score):
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.end_score = end_score

    def check_win(self):
        if self.player1_score >= self.end_score:
            self.winner = 1
            return True
        if self.player2_score >= self.end_score:
            self.winner = 2
            return True
        
        return False