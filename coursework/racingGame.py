import pygame
import time
import math
from functions import scale_image, blit_rotate_center
import random


GRASS = scale_image(pygame.image.load("imgs/cartoon-grass.jpg"), 0.42)
# TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

# WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIDTH, HEIGHT = GRASS.get_width(), GRASS.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60



class ObstacleGenerator:
    def __init__(self):
        self.levels = [1,2,3,4,5,6,7,8,9,10]

    def generate_level_1(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)]
        ]

    def generate_level_2(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)]
        ]

    def generate_level_3(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)]
        ]

    def generate_level_4(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)],
            [(260, 260), (290, 260), (290, 290), (260, 290)]
        ]

    def generate_level_5(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)],
            [(260, 260), (290, 260), (290, 290), (260, 290)],
            [(330, 330), (360, 330), (360, 360), (330, 360)]
        ]

    def generate_level_6(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)],
            [(260, 260), (290, 260), (290, 290), (260, 290)],
            [(330, 330), (360, 330), (360, 360), (330, 360)],
            [(400, 400), (430, 400), (430, 430), (400, 430)]
        ]

    def generate_level_7(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)],
            [(260, 260), (290, 260), (290, 290), (260, 290)],
            [(330, 330), (360, 330), (360, 360), (330, 360)],
            [(400, 400), (430, 400), (430, 430), (400, 430)],
            [(470, 470), (500, 470), (500, 500), (470, 500)]
        ]

    def generate_level_8(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)],
            [(260, 260), (290, 260), (290, 290), (260, 290)],
            [(330, 330), (360, 330), (360, 360), (330, 360)],
            [(400, 400), (430, 400), (430, 430), (400, 430)],
            [(470, 470), (500, 470), (500, 500), (470, 500)],
            [(540, 540), (570, 540), (570, 570), (540, 570)]
        ]

    def generate_level_9(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)],
            [(260, 260), (290, 260), (290, 290), (260, 290)],
            [(330, 330), (360, 330), (360, 360), (330, 360)],
            [(400, 400), (430, 400), (430, 430), (400, 430)],
            [(470, 470), (500, 470), (500, 500), (470, 500)],
            [(540, 540), (570, 540), (570, 570), (540, 570)],
            [(610, 610), (640, 610), (640, 640), (610, 640)]
        ]

    def generate_level_10(self):
        return [
            [(50, 50), (80, 50), (80, 80), (50, 80)],
            [(120, 120), (150, 120), (150, 150), (120, 150)],
            [(20, 20), (23, 20), (23, 23), (20, 23)],
            [(260, 260), (290, 260), (290, 290), (260, 290)],
            [(330, 330), (360, 330), (360, 360), (330, 360)],
            [(400, 400), (430, 400), (430, 430), (400, 430)],
            [(470, 470), (500, 470), (500, 500), (470, 500)],
            [(540, 540), (570, 540), (570, 570), (540, 570)],
            [(610, 610), (640, 610), (640, 640), (610, 640)],
            [(680, 680), (710, 680), (710, 710), (680, 710)]
        ]    

    def generate_obstacles(self, level):
        if level == 1:
            return self.generate_level_1()
        elif level == 2:
            return self.generate_level_2()
        elif level == 3:
            return self.generate_level_3()
        elif level == 4:
            return self.generate_level_4()
        elif level == 5:
            return self.generate_level_5()
        elif level == 6:
            return self.generate_level_6()
        elif level == 7:
            return self.generate_level_7()
        elif level == 8:
            return self.generate_level_8()
        elif level == 9:
            return self.generate_level_9()
        elif level == 10:
            return self.generate_level_10()
        else:
            print("Level must be between 1 and 10.")
    
    def generate_finish_box_position(self, level):

        x_range = (50, 750)
        y_range = (50, 750)

        if level <= 0:
            print("Level must be greater than 0.")

        # positions = [(50, 50), (80, 50), (80, 80), (50, 80)]
        positions = [(random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])) for _ in range(level)]
        if level <= len(positions):
            return positions[level - 1]
        else:
            print("No predefined position for the current level.")

class FinishBox:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 255), self.rect)

    def check_collision(self, car_rect):
        return self.rect.colliderect(car_rect)
     
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
            print("At least three points are required to define a polygon.")

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

    
def draw(win, images, player_car, track_border, finish_box):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    track_border.draw(win)
    finish_box.draw(win) 
    pygame.display.update()



def run():
    run = True
    clock = pygame.time.Clock()
    GRASS = scale_image(pygame.image.load("imgs/cartoon-grass.jpg"), 0.42)
    LEVEL = 1

    obstacle_generator = ObstacleGenerator()
    obstacles = obstacle_generator.generate_obstacles(LEVEL)


    track_border = Obstacles(obstacles)

    RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
    images = [(GRASS, (0, 0))]
    player_car = PlayerCar(4, 4, RED_CAR)
    WIDTH, HEIGHT = GRASS.get_width(), GRASS.get_height()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Racing Game!")
    
    FINISH_BOX_SIZE = (40, 40)
    finish_box_position = obstacle_generator.generate_finish_box_position(LEVEL)
    finish_box = FinishBox(finish_box_position, FINISH_BOX_SIZE)

    FPS = 60
    while run:
        clock.tick(FPS)

        draw(WIN, images, player_car, track_border, finish_box) 

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

        if finish_box.check_collision(player_car.rect):
            if LEVEL == 10:
                print("You won!")
                run = False
                break
            LEVEL += 1
            print(f"Level Up! Now on Level {LEVEL}")
            obstacles = obstacle_generator.generate_obstacles(LEVEL)
            finish_box_position = obstacle_generator.generate_finish_box_position(LEVEL)
            finish_box = FinishBox(finish_box_position, FINISH_BOX_SIZE)
            track_border = Obstacles(obstacles)
            player_car.x, player_car.y = player_car.START_POS
            player_car.vel = 0
            player_car.angle = 0
            
        if not moved:
            player_car.reduce_speed(track_border)


pygame.quit()
