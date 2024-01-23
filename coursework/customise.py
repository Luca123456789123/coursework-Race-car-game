import Pygame

def car_customization_screen():
    SCREEN_WIDTH = 1220
    SCREEN_HEIGHT = 600

    customise = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Car Customization')
    customise.fill((255, 200, 200))  # Customize the background color if needed

    import pygame
    import sys

# Initialize Pygame
    pygame.init()

# Set up window parameters
    window_width = 1000
    window_height = 1200
    window_title = "Car Customization"

# Create the window
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(window_title)

# Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Clear the screen
        screen.fill((255, 255, 255))  # White background

    # Display text on the window
        font = pygame.font.Font(None, 36)
        text = font.render("Car Customization", True, (0, 0, 0))  # Black text
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        screen.blit(text, text_rect)

    # Update the display
        pygame.display.flip()

    # Control the frame rate
        pygame.time.Clock().tick(30)

        pygame.display.update()