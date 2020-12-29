import sys
import time
import pygame






class Player:
    def __init__(self,x,y,window_width,window_height):
        self.x = x
        self.y = y
        self.window_width = window_width
        self.window_height = window_height
    def up(self):
        if self.y > 0:
            self.y = self.y - 5
        else:
            self.y = 0
    def down(self):
        if self.y < self.window_height:
            self.y = self.y + 5
        else:
            self.y = self.window_height

    def left(self):
        if self.x > 0:
            self.x = self.x - 5
        else:
            self.x = 0
    def right(self):
        if self.x < self.window_width:
            self.x = self.x + 5
        else:
            self.x = self.window_width


width = 500
height = 500
player_x = width/2
player_y = height/2
background_color = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((width, height))
carImg = pygame.image.load('beniz.png')
screen.blit(carImg, (player_x, player_y))
pygame.display.update()
player_1 = Player(player_x,player_y,width,height)
while (True):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.left()
                screen.fill(background_color)
            elif event.key == pygame.K_RIGHT:
                player_1.right()
                screen.fill(background_color)
            elif event.key == pygame.K_UP:
                player_1.up()
                screen.fill(background_color)
            elif event.key == pygame.K_DOWN:
                player_1.down()
                screen.fill(background_color)
            elif event.key == pygame.K_ESCAPE:
                sys.exit()


        screen.blit(carImg, (player_1.x, player_1.y))
        pygame.display.update()





