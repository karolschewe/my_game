import pygame
from screen import *
from player import *
from projectile import *
import sys

class Game():
    def __init__(self):

        # main class initialisation
        self.screen = Screen()
        size_x, size_y = self.screen.carImg.get_size()
        self.player = Player(self.screen.width,self.screen.height,size_x, size_y)
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.projectiles_vec = {}
        self.no_of_projectiles = 0
        self.max_projectiles = 100
    # changing resolution
    def change_game_res(self,width,height):
        self.screen.change_resolution(width,height)
        self.player.update_widow_size(width,height)
    #settings change
    def game_settings_change_check(self,event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_5:
                    self.change_game_res(round(self.screen.width * 1.2), round(self.screen.height * 1.2))

    def add_projectile(self,projectile):
        self.projectiles_vec[self.no_of_projectiles] = projectile
        self.no_of_projectiles = self.no_of_projectiles + 1
        if self.no_of_projectiles == self.max_projectiles:
            self.no_of_projectiles = 0

    # shooting
    def are_we_shooting(self,event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("w")
                    tmp_proj = Projectile(self.player,'UP',10)
                    self.add_projectile(tmp_proj)
                if event.key == pygame.K_s:
                    print("s")
                    tmp_proj = Projectile(self.player,'DOWN',10)
                    self.add_projectile(tmp_proj)
                if event.key == pygame.K_a:
                    print("a")
                    tmp_proj = Projectile(self.player,'LEFT',10)
                    self.add_projectile(tmp_proj)
                if event.key == pygame.K_d:
                    print("d")
                    tmp_proj = Projectile(self.player,'RIGHT',10)
                    self.add_projectile(tmp_proj)






    def where_we_goin(self,event_list):
        # function scanning arrows being pressed
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
        # main game loop
        nnn = 0
        while True:
            events_scanned = pygame.event.get()
            self.where_we_goin(events_scanned)
            self.game_settings_change_check(events_scanned)
            if self.move_down:
                self.player.down()
            if self.move_right:
                self.player.right()
            if self.move_up:
                self.player.up()
            if self.move_left:
                self.player.left()

            self.are_we_shooting(events_scanned)

            # recalculation of projectiles speed
            for i in self.projectiles_vec.keys():
                if not self.projectiles_vec[i].stopped:
                    self.projectiles_vec[i].timestep()
                    if self.projectiles_vec[i].v_x == 0 and self.projectiles_vec[i].v_y == 0:
                        print(self.projectiles_vec[i].y)
                        self.projectiles_vec[i].stopped = True





            self.player.discharge_movement_status()
            time.sleep(1/45)
            self.screen.screen.fill(self.screen.background_color)
            self.screen.screen.blit(self.screen.carImg, (self.player.x, self.player.y))
            # pygame.draw.rect(self.screen.screen, (255, 0, 0), pygame.Rect(40, 40, 20, 20))
            for i in self.projectiles_vec.values():
                if not i.stopped:
                    pygame.draw.rect(self.screen.screen, (255,0,0), pygame.Rect(i.x, i.y, 20, 20))
            pygame.display.update()
