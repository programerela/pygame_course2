#meni za menjanje boje zmije i menjanje vockica

import random
from tkinter import font
import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 40
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None, 38)
big_font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

def random_food(snake):
    while True:
        food_position = (random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT))
        if food_position not in snake:
            return food_position


def reset_game():
    snake = [(9, 10), (8, 10), (7, 10)]
    food = random_food(snake)
    direction = (1, 0)
    return snake, food, direction, 0, False

snake, food, direction, score, game_over = reset_game()
move_timer = 0
MOVE_DELAY = 20
BG_COLOR = (120, 89, 150)

last_score = 0

running = True

#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                snake, food, direction, score, game_over = reset_game()
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)  
    
    if not game_over:
        move_timer += 1
        if move_timer >= MOVE_DELAY:
            move_timer = 0
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)
            
            x, y = new_head
            hit_self = new_head in snake[:-1]
            hit_wall = x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT
            
            if score % 5 == 0 and score != 0 and score != last_score:
                MOVE_DELAY -= 2
                last_score = score

            if hit_self or hit_wall:
                game_over = True
            else:
                snake.insert(0, new_head)
                if(new_head == food):
                    food = random_food(snake)
                    score += 1
                else:
                    snake.pop()
            
    screen.fill(BG_COLOR)
    for x, y in snake[1:]:
        pygame.draw.rect(screen, (35, 180, 70), (x*CELL_SIZE+2, y*CELL_SIZE+2, CELL_SIZE-4, CELL_SIZE-4), border_radius=5)
    
    hx, hy = snake[0]
    head_rect = pygame.Rect(hx*CELL_SIZE+1, hy*CELL_SIZE+1, CELL_SIZE-2, CELL_SIZE-2)
    pygame.draw.rect(screen, (70, 235, 100), head_rect, border_radius=7)
    
    if direction == (1, 0):
        pygame.draw.circle(screen, (0,0,0), (head_rect.right-8, head_rect.top+9), 3)
        pygame.draw.circle(screen, (0,0,0), (head_rect.right-8, head_rect.bottom-9), 3)
    elif direction == (-1, 0):
        pygame.draw.circle(screen, (0,0,0), (head_rect.left+8, head_rect.top+9), 3)
        pygame.draw.circle(screen, (0,0,0), (head_rect.left+8, head_rect.bottom-9), 3)
    elif direction == (0, 1):
        pygame.draw.circle(screen, (0,0,0), (head_rect.left+9, head_rect.bottom-8), 3)
        pygame.draw.circle(screen, (0,0,0), (head_rect.right-9, head_rect.bottom-8), 3)
    elif direction == (0, -1):
        pygame.draw.circle(screen, (0,0,0), (head_rect.left+9, head_rect.top+8), 3)
        pygame.draw.circle(screen, (0,0,0), (head_rect.right-9, head_rect.top+8), 3)
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (WIDTH, y))    

    fx, fy = food
    food_center = (fx * CELL_SIZE + CELL_SIZE // 2, fy * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, (235, 65, 70), food_center, CELL_SIZE //2 -3)
    
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    
    if game_over:
        screen.blit(big_font.render("Game Over!", True, (255, 255, 255)), (WIDTH//2 - 180, HEIGHT//2 - 30))
        screen.blit(font.render("Press R to Restart", True, (255, 255, 255)), (WIDTH//2 - 130, HEIGHT//2 + 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()