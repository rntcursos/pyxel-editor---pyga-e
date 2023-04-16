import pygame

class Color_indicator(pygame.sprite.Sprite):

    def __init__(self,color,pos, groups):
        super().__init__(groups)

        self.image = pygame.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
    
    def color_update(self, color):
        self.image.fill(color)