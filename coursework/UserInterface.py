import pygame
import racingGame

SCREEN_WIDTH = 1220
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('button')

# Load button images
start_img = pygame.image.load('./imgs/green-start-button.png').convert_alpha()
exit_img = pygame.image.load('./imgs/exit-button.png').convert_alpha()

# Define a common size for both buttons
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

# Button class
class Button():
    def __init__(self, x, y, image, width, height):
        self.width = width
        self.height = height

        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()

        # Center the button on the screen
        self.rect.center = (x, y)

    def draw(self):
        action = False

        # Get mouse pos
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect.topleft)

        return action

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Center the buttons horizontally
start_button = Button(SCREEN_WIDTH // 2, 200, start_img, BUTTON_WIDTH, BUTTON_HEIGHT)
exit_button = Button(SCREEN_WIDTH // 2, 300, exit_img, BUTTON_WIDTH, BUTTON_HEIGHT)

run = True
while run:
    screen.fill((202, 228, 241))

    if start_button.draw():
        racingGame.run()
    if exit_button.draw():
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()