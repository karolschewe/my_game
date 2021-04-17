import time

class Creature:
    def __init__(self,window_width,window_height,size_x,size_y):
        self.x = window_width/2
        self.y = window_height/2
        self.window_width = window_width
        self.window_height = window_height
        self.size_x = size_x
        self.size_y = size_y
        self.speed = 10 # projectile initial speed is a sum of Creature speed and projectile speed
        self.projectile_speed = 25 #warning the higher speed, the higher range

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
    pass