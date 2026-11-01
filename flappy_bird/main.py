import random
import pygame

pygame.init()

WIDTH = 500
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FlappyBird")
big_font = pygame.font.SysFont(None, 42)

clock = pygame.time.Clock()

bird_x = 150
bird_y = 300
bird_radius = 25
bird_velocity = 0
gravity = 0.5

pipe_x = 450
pipe_width = 80
gap = 125
pipe_top_height = 150
pipe_speed = 5

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
    
    #logika cevi
    pipe_x -= pipe_speed
    
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_top_height = random.randint(100,300)

    pygame.draw.circle(screen, (255, 255, 0), (bird_x, bird_y), bird_radius)
    
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, pipe_width, pipe_top_height))
    bottom_pipe_y = pipe_top_height + gap
    
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, bottom_pipe_y, pipe_width, HEIGHT - bottom_pipe_y))

    clock.tick(60)
    pygame.display.flip()
pygame.quit()