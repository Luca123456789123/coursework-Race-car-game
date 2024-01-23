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
    def __init__(self, max_vel, rotation_vel, START_POS, img):
        self.img = img
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.START_POS = START_POS
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
        win.blit(self.img, (self.x, self.y))

class Obstacles:
    def __init__(self, obstacles):
        self.obstacles = [self.create_obstacle(points) for points in obstacles]
        self.angle = 0

    def create_obstacle(self, points):
        if len(points) < 3:
            raise ValueError("At least three points are required to define a polygon.")

        min_x = min(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_x = max(p[0] for p in points)
        max_y = max(p[1] for p in points)

        rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)

        return {"points": points, "rect": rect}

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        for obstacle in self.obstacles:
            pygame.draw.polygon(win, (255, 0, 0), obstacle["points"])

    def check_collision(self, car_rect):
        for obstacle in self.obstacles:
            if obstacle["rect"].colliderect(car_rect):
                return True
        return False

class PlayerCar(AbstractCar):
    def __init__(self, max_vel, rotation_vel, image):
        self.img = image
        START_POS = (180, 200)
        super().__init__(max_vel, rotation_vel, START_POS, image)
        self.rect = self.img.get_rect(center=(self.x, self.y))

    def reduce_speed(self, track_border):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move(track_border)

    def move(self, track_border):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
    
        new_y = self.y - vertical
        new_x = self.x - horizontal
    
        if not track_border.check_collision(self.rect):
            self.y = new_y
            self.x = new_x
            self.rect.center = (self.x, self.y)
            self.rotate()
    
    def move_forward(self, track_border):
        new_vel = min(self.vel + self.acceleration, self.max_vel)
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * new_vel
        horizontal = math.sin(radians) * new_vel

        new_y = self.y - vertical
        new_x = self.x - horizontal

        new_rect = pygame.Rect((new_x, new_y), self.rect.size)

        if not track_border.check_collision(new_rect):
            self.y = new_y
            self.x = new_x
            self.vel = new_vel
            self.rect.center = (self.x, self.y)
            
    def move_backward(self, track_border):
        new_vel = max(self.vel - self.acceleration, -self.max_vel)
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * new_vel
        horizontal = math.sin(radians) * new_vel

        new_y = self.y - vertical
        new_x = self.x - horizontal

        new_rect = pygame.Rect((new_x, new_y), self.rect.size)

        if not track_border.check_collision(new_rect):
            self.y = new_y
            self.x = new_x
            self.vel = new_vel
            self.rect.center = (self.x, self.y)

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

        self.rect = self.img.get_rect(center=(self.x, self.y))

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def check_collision(self, track_border):
        return self.rect.colliderect(track_border.rect)

    
def draw(win, images, player_car, track_border):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    track_border.draw(win)
    pygame.display.update()



def run():
    run = True
    clock = pygame.time.Clock()
    GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)

    # On level 1 - one obstacle is created, on level 2 - two obstacles are created etc. 
    # The obstacles are defined by a list of points.
    # The obstacles are randomly placed on the track.
    # The obstacles are rotated randomly.
    
    # Create a finish button to increase the level and restart the game. 
    # Define the points for the border
    
    OBSTACLE1_POINTS = [
        (50, 50),
        (80, 50),
        (80, 80),
        (50, 80)
    ]
    
    OBSTACLE2_POINTS = [
        (120, 120),
        (150, 120),
        (150, 150),
        (120, 150)
    ]
    
    OBSTACLES = [OBSTACLE1_POINTS, OBSTACLE2_POINTS]

    track_border = Obstacles(OBSTACLES)

    RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
    images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
    player_car = PlayerCar(4, 4, RED_CAR)
    WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racing Game!")
    
    FPS = 60
    while run:
        clock.tick(FPS)

        draw(WIN, images, player_car, track_border)  # Pass the track_border object to the draw function

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
            player_car.move_forward(track_border)
        if keys[pygame.K_s]: 
            moved = True
            player_car.move_backward(track_border)
            
        if not moved:
            player_car.reduce_speed(track_border)


pygame.quit()
