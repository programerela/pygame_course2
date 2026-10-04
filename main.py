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

snake = [(5, 10)]
direction = (1, 0)
move_timer = 0
MOVE_DELAY = 30 

BG_COLOR = (60, 67, 70)

running = True

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    move_timer += 1
    if move_timer >= MOVE_DELAY:
        move_timer = 0
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)
        snake[0]= new_head
            
    screen.fill(BG_COLOR)
    x, y = snake[0]
    rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, (0, 255, 0), rect)
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (WIDTH, y))    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()