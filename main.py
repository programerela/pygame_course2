#meni za menjanje boje zmije i menjanje vockica

import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 40
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

snake = [(5, 10), (4, 10), (3, 10)]
direction = (1, 0)
move_timer = 0
MOVE_DELAY = 18 

BG_COLOR = (60, 67, 70)

running = True

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)  
    
    move_timer += 1
    if move_timer >= MOVE_DELAY:
        move_timer = 0
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)
        snake.insert(0, new_head)
        snake.pop()
            
    screen.fill(BG_COLOR)
    for x, y in snake:
        pygame.draw.rect(screen, (50, 220, 80), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (WIDTH, y))    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()