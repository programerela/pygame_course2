import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FlappyBird")
big_font = pygame.font.SysFont(None, 42)

clock = pygame.time.Clock()

sky = (90, 105, 205)

running = True

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    screen.fill(sky)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()