import pygame
def scale_image(img, factor):
    size= round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(window, image, top_left, angle):
    rotated_image = pygame.transform.rotate(iage, angle)
    new_rect = rotated image.get_rect(center image.get_rect(topleft = top_left).center)
    window.blit(rotated image, new_rect.topleft)
