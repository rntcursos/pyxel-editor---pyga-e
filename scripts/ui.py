import pygame

class Ui(pygame.sprite.Sprite):

    def __init__(self,size,pos,color, groups):
        super().__init__(groups)

        self.image = pygame.Surface(size)
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)