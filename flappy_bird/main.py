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
gap = 130
pipe_top_height = 150
pipe_speed = 5

score = 0
passed_pipe = False

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
    
    #logika ptice
    bird_velocity += gravity
    bird_y += bird_velocity
    
    #logika cevi
    bottom_pipe_y = pipe_top_height + gap
    pipe_x -= pipe_speed
        
    if pipe_x + pipe_width < bird_x and not passed_pipe:
        score += 1
        passed_pipe = True
    
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_top_height = random.randint(100, 300)
        passed_pipe = False
        
    bird_rect = pygame.Rect(
        bird_x - bird_radius,
        bird_y - bird_radius,
        bird_radius * 2,
        bird_radius * 2
    )
    top_pipe_rect = pygame.Rect(
        pipe_x,
        0,
        pipe_width,
        pipe_top_height
    )
    bottom_pipe_rect = pygame.Rect(
        pipe_x,
        pipe_top_height + gap,
        pipe_width,
        HEIGHT - (pipe_top_height + gap)
    )
    
    if bird_rect.colliderect(top_pipe_rect):
        running = False
        game_over_text = big_font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    
    if bird_rect.colliderect(bottom_pipe_rect):
        running = False
        game_over_text = big_font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        running = False
        game_over_text = big_font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

    #crtanje ptice i cevi
    pygame.draw.circle(screen, (255, 255, 0), (bird_x, bird_y), bird_radius)
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, pipe_width, pipe_top_height))
    pygame.draw.rect(screen, (0, 255, 0), (pipe_x, bottom_pipe_y, pipe_width, HEIGHT - bottom_pipe_y))

    score_text = big_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    clock.tick(60)
    pygame.display.flip()
pygame.quit()