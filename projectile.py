
class Projectile:

    def __init__(self,x,y,v_x,v_y,damage,dangerous = False):
        #can projectile hurt player??
        self.damages_player = dangerous
        # projectile initial position
        self.x = x
        self.y = y
        # projectile velocity
        self.v_x = v_x
        self.v_y = v_y
        # projectile damage
        self.damage = damage

    def timestep(self):
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y
