import time

class Player:
    def __init__(self,window_width,window_height,player_size_x,player_size_y):
        self.x = window_width/2
        self.y = window_height/2
        self.window_width = window_width
        self.window_height = window_height
        self.player_size_x = player_size_x
        self.player_size_y = player_size_y
        self.speed = 1
    # moving player avatar
    def up(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            self.y = 0
    def down(self):
        if self.y < self.window_height - self.player_size_y:
            self.y = self.y + 1
        else:
            self.y = self.window_height - self.player_size_y

    def left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            self.x = 0
    def right(self):
        if self.x < self.window_width - self.player_size_x:
            self.x = self.x + 1
        else:
            self.x = self.window_width - self.player_size_x
    #changing speed
    def speed_me_up(self,percentage):
        self.speed = self.speed * percentage

    # updating window size
    def update_widow_size(self,window_width,window_height):
        self.window_width = window_width
        self.window_height = window_height
