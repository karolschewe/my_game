import time
import pygame

class Creature:
    def __init__(self,window_width,window_height,graphic_directory):

        self.window_width = window_width
        self.window_height = window_height
        self.health = 100
        self.dead = False



        # current movement status (used for calculation of projectiles speed)
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    # moving Creature avatar
    def up(self):
        if self.y > 0:
            self.y = self.y - self.speed
            self.moving_up = True
        else:
            self.y = 0
    def down(self):
        if self.y < self.window_height - self.size_y:
            self.y = self.y + self.speed
            self.moving_down = True
        else:
            self.y = self.window_height - self.size_y

    def left(self):
        if self.x > 0:
            self.x = self.x - self.speed
            self.moving_left = True
        else:
            self.x = 0
    def right(self):
        if self.x < self.window_width - self.size_x:
            self.x = self.x + self.speed
            self.moving_right = True
        else:
            self.x = self.window_width - self.size_x
    #changing speed
    def speed_me_up(self,percentage):
        self.speed = self.speed * percentage

    def damage(self,damage_points):
        self.health = self.health - damage_points
        if self.health <= 0:
            self.dead = True


    #reset moving status
    def discharge_movement_status(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    # updating window size
    def update_widow_size(self,window_width,window_height):
        self.window_width = window_width
        self.window_height = window_height

class Player(Creature):
    def __init__(self,window_width,window_height,graphic_directory):
        super().__init__(window_width,window_height,graphic_directory)
        self.x = window_width / 2
        self.y = window_height / 2
        self.speed = 10  # projectile initial speed is a sum of Creature speed and projectile speed
        self.projectile_speed = 25  # warning the higher speed, the higher range
        self.img = pygame.image.load(graphic_directory)
        self.size_x, self.size_y = self.img.get_size()
        self.health = 100


class Walaszek(Creature):
    def __init__(self,window_width,window_height,graphic_directory,starting_x,starting_y):
        super().__init__(window_width, window_height, graphic_directory)
        self.x = starting_x
        self.y = starting_y
        self.speed = 10  # projectile initial speed is a sum of Creature speed and projectile speed
        self.projectile_speed = 25  # warning the higher speed, the higher range
        self.img = pygame.image.load(graphic_directory)
        self.size_x, self.size_y = self.img.get_size()
        self.health = 100
