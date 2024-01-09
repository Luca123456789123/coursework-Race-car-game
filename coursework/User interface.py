import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw(self):
    
    pos = pygame.mouse.get_pos()

    if self.rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and slef.clicked == False:
            self.clicked = True
            print('Clicked')
    if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False


