import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FlappyBird")
big_font = pygame.font.SysFont(None, 42)

clock = pygame.time.Clock()

bird_x = 50
bird_y = 300
bird_radius = 20

bird_velocity = 0
gravity = 0.5

sky = (100, 180, 255)

running = True

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = -8
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird_velocity = -8

    screen.fill(sky)
    
    bird_velocity += gravity
    bird_y += bird_velocity
    
    pygame.draw.circle(screen, (255, 255, 0), (bird_x, bird_y), bird_radius)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()