import pygame
import racingGame


SCREEN_WIDTH = 1220
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('button')


#load button image

start_img = pygame.image.load('./imgs/start_button.png').convert_alpha()
exit_img = pygame.image.load('./imgs/exit_button.png').convert_alpha()
car_custom_img = pygame.image.load('./imgs/purple-car.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
    
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False 

        #get pouse pos
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True 

                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        
        screen.blit(self. image,(self.rect.x, self.rect.y))

        return action 
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



start_button = Button(864, 200, start_img, 1.0)
exit_button = Button (864, 300, exit_img, 1.0)
car_button = Button(400, 500, car_custom_img, 1.0) 

run = True
while run:

    screen.fill((202, 228, 241))
    if start_button.draw() == True:
        racingGame.run()
    if exit_button.draw() == True:
        run = False
    if car_button.draw() == True:
        print('customize')


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()