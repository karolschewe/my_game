import pygame
from screen import *
from player import *
import sys

class Game():
    def __init__(self):


        self.screen = Screen()
        player_size_x, player_size_y = self.screen.carImg.get_size()
        self.player = Player(self.screen.width,self.screen.height,player_size_x, player_size_y)
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False


    def where_we_goin(self,event_list):

        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                elif event.key == pygame.K_RIGHT:
                    self.move_right = True
                elif event.key == pygame.K_UP:
                    self.move_up = True
                elif event.key == pygame.K_DOWN:
                    self.move_down = True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                elif event.key == pygame.K_RIGHT:
                    self.move_right = False
                elif event.key == pygame.K_UP:
                    self.move_up = False
                elif event.key == pygame.K_DOWN:
                    self.move_down = False

    def play_game(self):
        while True:
            self.where_we_goin(pygame.event.get())
            if self.move_down:
                self.player.down()
            if self.move_right:
                self.player.right()
            if self.move_up:
                self.player.up()
            if self.move_left:
                self.player.left()

            time.sleep(1/200/self.player.speed)
            self.screen.screen.fill(self.screen.background_color)
            self.screen.screen.blit(self.screen.carImg, (self.player.x, self.player.y))
            pygame.display.update()
