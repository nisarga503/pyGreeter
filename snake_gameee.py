import pygame
import random

pygame.init()

WIDTH = 700
HEIGHT = 500
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (20, 20, 20)
GREEN = (40, 180, 60)
DARK_GREEN = (20, 120, 40)
LIGHT_GREEN = (80, 220, 80)
RED = (240, 50, 50)
WHITE = (255, 255, 255)
YELLOW = (255, 220, 50)

font = pygame.font.Font(None, 32)


def create_food(snake):
    while True:
        food = (
            random.randrange(20, WIDTH - 20, CELL),
            random.randrange(40, HEIGHT - 20, CELL)
        )

        if food not in snake:
            return food


def draw_snake(snake, direction):

    # Draw body as connected circles
    for i in range(len(snake) - 1, 0, -1):

        x, y = snake[i]

        pygame.draw.circle(
            screen,
            GREEN,
            (x + CELL // 2, y + CELL // 2),
            CELL // 2 + 2
        )

    # Draw head
    x, y = snake[0]

    center = (x + CELL // 2, y + CELL // 2)

    pygame.draw.circle(
        screen,
        DARK_GREEN,
        center,
        CELL // 2 + 4
    )

    # Eyes
    if direction == (CELL, 0):
        eye1 = (x + 14, y + 5)
        eye2 = (x + 14, y + 15)

    elif direction == (-CELL, 0):
        eye1 = (x + 6, y + 5)
        eye2 = (x + 6, y + 15)

    elif direction == (0, -CELL):
        eye1 = (x + 5, y + 6)
        eye2 = (x + 15, y + 6)

    else:
        eye1 = (x + 5, y + 14)
        eye2 = (x + 15, y + 14)

    pygame.draw.circle(screen, WHITE, eye1, 4)
    pygame.draw.circle(screen, WHITE, eye2, 4)

    pygame.draw.circle(screen, BLACK, eye1, 2)
    pygame.draw.circle(screen, BLACK, eye2, 2)


# Starting snake
snake = [
    (300, 240),
    (280, 240),
    (260, 240),
    (240, 240),
    (220, 240)
]

direction = (CELL, 0)

food = create_food(snake)

score = 0
running = True

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if direction != (0, CELL):
                    direction = (0, -CELL)

            elif event.key == pygame.K_DOWN:
                if direction != (0, -CELL):
                    direction = (0, CELL)

            elif event.key == pygame.K_LEFT:
                if direction != (CELL, 0):
                    direction = (-CELL, 0)

            elif event.key == pygame.K_RIGHT:
                if direction != (-CELL, 0):
                    direction = (CELL, 0)

    # Move
    head_x, head_y = snake[0]

    new_x = head_x + direction[0]
    new_y = head_y + direction[1]

    # Screen wrapping
    if new_x < 0:
        new_x = WIDTH - CELL

    if new_x >= WIDTH:
        new_x = 0

    if new_y < 40:
        new_y = HEIGHT - CELL

    if new_y >= HEIGHT:
        new_y = 40

    new_head = (new_x, new_y)

    # If snake hits itself, restart automatically
    if new_head in snake:

        snake = [
            (300, 240),
            (280, 240),
            (260, 240),
            (240, 240),
            (220, 240)
        ]

        direction = (CELL, 0)
        score = 0
        food = create_food(snake)

    else:

        snake.insert(0, new_head)

        # Food eaten
        if new_head == food:
            score += 1
            food = create_food(snake)

        else:
            snake.pop()

    # Background
    screen.fill(BLACK)

    # Title
    title = font.render(
        "SNAKE GAME",
        True,
        LIGHT_GREEN
    )

    screen.blit(title, (20, 8))

    # Score
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (WIDTH - 130, 8))

    # Food
    pygame.draw.circle(
        screen,
        RED,
        (food[0] + CELL // 2, food[1] + CELL // 2),
        CELL // 2 - 2
    )

    # Draw snake
    draw_snake(snake, direction)

    pygame.display.update()

    # Speed
    clock.tick(8)


pygame.quit()
