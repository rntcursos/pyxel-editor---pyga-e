import pygame

class Ui(pygame.sprite.Sprite):

    def __init__(self,size,pos,color, groups):
        super().__init__(groups)

        self.image = pygame.Surface(size, pygame.SRCALPHA).convert_alpha()
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)

class Canvas(pygame.sprite.Sprite):

    def __init__(self,size,pos,color, groups):
        super().__init__(groups)

        
        self.image = pygame.Surface(size, pygame.SRCALPHA).convert_alpha()
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)
        pygame.draw.rect(self.image, "white", self.rect, 1)
    
    def canvas_clean(self, surf,rect):
        self.image.fill(self.color)
        pygame.draw.rect(surf, "white", rect, 1)