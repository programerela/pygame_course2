import pygame

pygame.init()

WIDTH = 400
HEIGHT = 500
FPS = 60
ROWS = 8
COLUMNS = 8
CELL_SIZE = 35
BOARD_SIZE = ROWS * CELL_SIZE
BOARD_X = (WIDTH - BOARD_SIZE) // 2
BOARD_Y = 115

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Blast - Pygame")
clock = pygame.time.Clock()

BG_COLOR = (50, 30, 250)
TEXT_COLOR = (0, 0, 0)
GRID_COLOR = (200, 208, 218)
EMPTY_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 52)

board = []
for row in range(ROWS):
    board.append([None] * COLUMNS)
    
def draw_board():
    for row in range(ROWS):
        for col in range(COLUMNS):
            x = BOARD_X + col * CELL_SIZE
            y = BOARD_Y + row * CELL_SIZE
            
            rect = pygame.Rect(x, y, CELL_SIZE - 4, CELL_SIZE - 4)
            border_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            pygame.draw.rect(screen, GRID_COLOR, border_rect, 1)
            pygame.draw.rect(screen, GRID_COLOR, border_rect, 1)
            
running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(BG_COLOR)
    title = font.render("BLOCK BLAST", True, TEXT_COLOR)
    title_rect = title.get_rect(center=(WIDTH // 2, 70))
    screen.blit(title, title_rect)
    
    draw_board()
    
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()