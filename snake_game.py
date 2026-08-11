import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

snake = [(300, 200), (280, 200), (260, 200)]
direction = (20, 0)

food = (
    random.randrange(0, WIDTH, BLOCK),
    random.randrange(0, HEIGHT, BLOCK)
)

score = 0
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)

            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)

            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)

            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

    # Move snake
    x, y = snake[0]
    new_head = (x + direction[0], y + direction[1])

    # Wall collision
    if new_head[0] < 0 or new_head[0] >= WIDTH:
        running = False

    if new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False

    # Body collision
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1

        food = (
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK)
        )
    else:
        snake.pop()

    # Draw
    screen.fill(BLACK)

    for part in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (part[0], part[1], BLOCK, BLOCK)
        )

    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], BLOCK, BLOCK)
    )

    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(10)

pygame.quit()