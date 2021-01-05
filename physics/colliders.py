class BoxCollider:
    def __init__(self, x, y, width, height, gravity=False, gravity_scale=0.3, max_gravity=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gravity = gravity
        self.gravity_scale = gravity_scale
        self.max_gravity = max_gravity
        self.velocity = [0, 0]
    
    def update(self):
        if self.gravity:
            self.velocity[1] = min(self.velocity[1] + self.gravity_scale, self.max_gravity)
        
        self.x += self.velocity[0]
        self.y += self.velocity[1]
    
    @property
    def rect(self):
        return [self.x, self.y, self.width, self.height]
    
    def collide_point(self, pos):
        if (self.x < pos[0] < self.x + self.width) and (self.y < pos[1] < self.y + self.height):
            return True
        elif not (self.x < pos[0] < self.x + self.width) and not (self.y < pos[1] < self.y + self.height):
            return False
    
    def collide_rect(self, rect):
        if ((self.x < rect.x < self.x + self.width) or (self.x < rect.x + rect.width < self.x + self.width)) and ((self.y < rect.y < self.y + self.height) or (self.y < rect.y + rect.height < self.y + self.height)):
            return True
        elif not ((self.x < rect.x < self.x + self.width) or (self.x < rect.x + rect.width < self.x + self.width)) and not ((self.y < rect.y < self.y + self.height) or (self.y < rect.y + rect.height < self.y + self.height)):
            return False