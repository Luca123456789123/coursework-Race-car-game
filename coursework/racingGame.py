import pygame
import time
import math
from functions import scale_image, blit_rotate_center

GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60


class AbstractCar:
    def __init__(self, max_vel, rotation_vel, START_POS):
        self.img = None
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
        win.blit(playercar, (self.x, self.y))

class Trackboarder:
    def __init__(self, collision,):
        self.img = self.IMG
        
        
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


class PlayerCar(AbstractCar):
    def __init__(self, max_vel, rotation_vel, START_POS, image):
        self.IMG = image
        START_POS = (180, 200)
        super().__init__(max_vel, rotation_vel, START_POS)
        
    IMG = RED_CAR
    START_POS = (180, 200)


def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()



def run():
    run = True
    clock = pygame.time.Clock()
    GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
    TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
    
    TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
    
    RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
    GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)
    images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
    player_car = PlayerCar(4, 4, RED_CAR)
    WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racing Game!")
    
    FPS = 60
    while run:
        clock.tick(FPS)
    
        draw(WIN, images, player_car)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        keys = pygame.key.get_pressed()
        moved = False
    
        if keys[pygame.K_a]:
            player_car.rotate(left=True)
        if keys[pygame.K_d]:
            player_car.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            player_car.move_forward()
    
        if not moved:
            player_car.reduce_speed()



pygame.quit()
