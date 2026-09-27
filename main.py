import pygame

pygame.init()

WIDTH = 400
HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Blast - Pygame")
clock = pygame.time.Clock()

BG_COLOR = (50, 30, 250)
TEXT_COLOR = (0, 0, 0)

font = pygame.font.Font(None, 52)

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
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()