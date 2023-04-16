import pygame

class Text(pygame.sprite.Sprite):

    def __init__(self,size,text, color,pos, groups):
        super().__init__(groups)

        self.color = color
        self.font = pygame.font.Font(None, size)
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect(topleft=pos)
    
    def update_text(self, text):
        self.image = self.font.render(text, True, self.color)