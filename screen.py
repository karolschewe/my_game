import pygame
class Screen:
    def __init__(self, width=600, height=600, background_color=(0, 0, 0)):
        pygame.init()
        self.background_color = background_color
        self.width = width
        self.height = height
        player_x = width / 2
        player_y = height / 2
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.update()

    #change resolution
    def change_resolution(self, width,height):
        self.width = width
        self.height = height
        player_x = width / 2
        player_y = height / 2
        self.screen = pygame.display.set_mode((width, height))
        self.carImg = pygame.image.load('beniz.png')
        self.screen.blit(self.carImg, (player_x, player_y))
