import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self,img,pos,func, groups):
        super().__init__(groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=pos)
    
        self.func = func
    
    def input(self):

        pos = pygame.mouse.get_pos()
        key = pygame.mouse.get_pressed()

        if key[0]:
            if self.rect.collidepoint(pos):
                self.func()
    
    def update(self):
        self.input()
    
