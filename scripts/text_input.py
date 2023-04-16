import pygame

class Text_input(pygame.sprite.Sprite):

    def __init__(self,rect,surf, groups):
        super().__init__(groups)

        self.surf = surf

        self.field_rect = pygame.Rect(rect)
        self.field_color = [220,220,220]
        pygame.draw.rect(self.surf, self.field_color, self.field_rect)

        self.value = ""
        self.active = False

        self.font = pygame.font.Font(None, 20)
        self.image = self.font.render("Digite aqui", True, "black")
        self.rect = self.image.get_rect(center = self.field_rect.center)
    
    def update_text(self):
        self.image = self.font.render(self.value, True, "black")
        self.rect = self.image.get_rect(center = self.field_rect.center)
    
    def events_handle(self, events):

        pos = pygame.mouse.get_pos()
        key = pygame.mouse.get_pressed()

        if self.field_rect.collidepoint(pos):
            if key[0]:
                self.active = True
                self.update_text()
                pygame.draw.rect(self.surf, "white", self.field_rect)
                
        else:
            self.active = False
            pygame.draw.rect(self.surf, self.field_color, self.field_rect)

        if events.type == pygame.KEYDOWN:
            
            if events.key == pygame.K_BACKSPACE and self.active:
                self.value = self.value[:-1]
                self.update_text()

            if events.unicode.isnumeric() and len(self.value) < 2 and self.active:
                self.value += events.unicode
                self.update_text()
            

