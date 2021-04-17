from player import Creature

from time import sleep
class Projectile:


    def __init__(self,owner: Creature,direction,damage,dangerous = False):
        #can projectile hurt player??
        self.damages_player = dangerous
        # projectile initial position
        self.x = owner.x + owner.size_x / 2
        self.y = owner.y + owner.size_y / 2
        # projectile starting velocity
        self.v_x = round(owner.moving_right * owner.speed*1.2 + owner.moving_left * -owner.speed*1.2)
        self.v_y = round(owner.moving_up * -owner.speed*1.2 + owner.moving_down * owner.speed*1.2)
        if direction == 'UP':
            if not owner.moving_down:
                self.v_y = round(
                    owner.moving_up * -owner.speed*1.2 + owner.moving_down * owner.speed*1.2)- owner.projectile_speed
            else:
                self.v_y = round(
                    owner.moving_up * -owner.speed * 1.2 + owner.moving_down * owner.speed * 0.5) - owner.projectile_speed
            self.v_x = round(owner.moving_right * owner.speed * 1.2 + owner.moving_left * -owner.speed * 1.2)

        elif direction == 'DOWN':
            if not owner.moving_up:
                self.v_y = round(
                    owner.moving_up * -owner.speed * 1.2 + owner.moving_down * owner.speed * 1.2) + owner.projectile_speed
            else:
                self.v_y = round(
                    owner.moving_up * -owner.speed * 0.5 + owner.moving_down * owner.speed * 1.2) + owner.projectile_speed
            self.v_x = round(owner.moving_right * owner.speed * 1.2 + owner.moving_left * -owner.speed * 1.2)

        elif direction == 'LEFT':
            if not owner.moving_right:
                self.v_x = round(
                    owner.moving_right * owner.speed * 1.2 + owner.moving_left * -owner.speed * 1.2) - owner.projectile_speed
            else:
                self.v_x = round(
                    owner.moving_right * owner.speed * 0.5 + owner.moving_left * -owner.speed * 1.2) - owner.projectile_speed
            self.v_y = round(owner.moving_up * -owner.speed * 1.2 + owner.moving_down * owner.speed * 1.2)

        elif direction == 'RIGHT':
            if not owner.moving_left:
                self.v_x = round(owner.moving_right * owner.speed * 1.2 + owner.moving_left * -owner.speed * 1.2) + owner.projectile_speed
            else:
                self.v_x = round(
                    owner.moving_right * owner.speed * 1.2 + owner.moving_left * -owner.speed * 0.5) + owner.projectile_speed
            self.v_y = round(owner.moving_up * -owner.speed*1.2 + owner.moving_down * owner.speed*1.2)

        # projectile damage
        self.damage = damage
        # if stopped it is omitted from further calculations
        self.stopped = False
        self.active = False

    def not_so_fast(self):
        # drag forces slow projectile down
        self.v_x = int(self.v_x*0.93)
        self.v_y = int(self.v_y*0.93)

    def timestep(self):
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y
        self.not_so_fast()

    def activate_projectile(self):
        self.active = True


