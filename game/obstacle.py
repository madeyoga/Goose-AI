import pygame

class Obstacle:
    """
    Obstacle contains image, size, and position
    """

    def __init__(self, post, image_path, size=(50,50), walkable=False):
        self.position = post
        self.surface = pygame.transform.scale(pygame.image.load(image_path), size)
        self.surface_to_draw = self.surface
        self.rect = self.surface_to_draw.get_rect()
        self.walkable = walkable
    
    def draw(self, win):
        self.rect = self.rect.move(self.position)
        self.rect.center = self.position

        win.blit(self.surface, self.rect)

class Pond(Obstacle):
    def __init__(self, post, image_path, size=(50,50)):
        super().__init__(post, image_path, size, True)
    
    def draw(self, win):
        win.blit(self.surface, self.position)