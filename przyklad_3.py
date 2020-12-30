import sys
import time
import pygame


class Screen:
    def __init__(self, width=500, height=500, background_color=(0, 0, 0)):
        pygame.init()
        self.background_color = background_color
        self.width = width
        self.height = height
        player_x = width / 2
        player_y = height / 2
        self.screen = pygame.display.set_mode((width, height))
        self.carImg = pygame.image.load('beniz.png')
        self.screen.blit(self.carImg, (player_x, player_y))
        pygame.display.update()


class Player:
    def __init__(self,window_width,window_height,player_size_x,player_size_y):
        self.x = window_width/2
        self.y = window_height/2
        self.window_width = window_width
        self.window_height = window_height
        self.player_size_x = player_size_x
        self.player_size_y = player_size_y
    def up(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            self.y = 0
    def down(self):
        if self.y < self.window_height:
            self.y = self.y + 1
        else:
            self.y = self.window_height - self.player_size_y

    def left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            self.x = 0
    def right(self):
        if self.x < self.window_width:
            self.x = self.x + 1
        else:
            self.x = self.window_width - self.player_size_x
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

            self.screen.screen.fill(self.screen.background_color)
            self.screen.screen.blit(self.screen.carImg, (self.player.x, self.player.y))
            pygame.display.update()


my_game_classes = Game()
my_game_classes.play_game()









