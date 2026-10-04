import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 30
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

BG_COLOR = (50, 80, 22)

running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(BG_COLOR)
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (45, 45, 45), (x, 0), (x, HEIGHT))
        
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (45, 45, 45), (0, y), (WIDTH, y))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()