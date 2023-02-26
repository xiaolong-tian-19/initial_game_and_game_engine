import pygame, sys

"""
CPSC 4160 Initial Game & Game Engine

Name:   George Tian
Email:  xt@g.clemson.edu
"""

class View():

    def __init__(self, caption, SCREEN_WIDTH, SCREEN_HEIGHT, screen_color, font_size):
        self.caption = caption
        pygame.display.set_caption(caption)
        
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
        self.SCREEN_SIZE = self.SCREEN_WIDTH, self.SCREEN_HEIGHT
        self.surface = pygame.display.set_mode(self.SCREEN_SIZE)

        self.screen_color = screen_color

        pygame.font.init()
        self.font_size = 36
        self.font = pygame.font.Font(None, self.font_size)

    def display(self, pong, paddle1, paddle2, pong_color, paddle_color, score):
        self.surface.fill(self.screen_color)
        pygame.draw.circle(self.surface, pong_color, pong.center, pong.radius)
        pygame.draw.rect(self.surface, paddle_color, paddle1.paddle)
        pygame.draw.rect(self.surface, paddle_color, paddle2.paddle)

        score_text = self.font.render(f'{score.player1_score} : {score.player2_score}', True, (255, 255, 255))
        self.surface.blit(score_text, (380, 10))

        pygame.display.update()

    def end_screen(self, score):
        self.surface.fill(self.screen_color)
        status_text = self.font.render(f'Player {score.winner} has won!!', True, (255, 255, 255))

        self.surface.blit(status_text, (self.SCREEN_WIDTH/2 - 100, self.SCREEN_HEIGHT/2))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
