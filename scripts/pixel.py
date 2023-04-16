import pygame

class Pixel(pygame.sprite.Sprite):

    def __init__(self,canvas,color,rect, groups):
        super().__init__(groups)

        self.color = color
        self.rect = pygame.Rect(rect)
        pygame.draw.rect(canvas, self.color, self.rect)