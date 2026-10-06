
import pygame as pg
import random

pg.init()

# Screen
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")

clock = pg.time.Clock()

# Food
food = pg.Rect(
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE),
    CELL_SIZE,
    CELL_SIZE
)

font = pg.font.Font(None, 36)

# Snake
snake = [(200, 200)]
snake_dir = (0, 0)

score = 0


# Reset game function
def reset_game():
    global snake, snake_dir, score, food

    snake = [(200, 200)]
    snake_dir = (0, 0)
    score = 0

    food.topleft = (
        random.randrange(0, WIDTH, CELL_SIZE),
        random.randrange(0, HEIGHT, CELL_SIZE)
    )


# Main game loop
running = True

while running:

    # -------------------------
    # EVENT HANDLING
    # -------------------------
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        # Handle keyboard input
        if event.type == pg.KEYDOWN:

            if event.key == pg.K_UP and snake_dir != (0, 20):
                snake_dir = (0, -20)

            elif event.key == pg.K_DOWN and snake_dir != (0, -20):
                snake_dir = (0, 20)

            elif event.key == pg.K_LEFT and snake_dir != (20, 0):
                snake_dir = (-20, 0)

            elif event.key == pg.K_RIGHT and snake_dir != (-20, 0):
                snake_dir = (20, 0)


    # -------------------------
    # SNAKE MOVEMENT
    # -------------------------
    if snake_dir != (0, 0):

        head = (
            snake[0][0] + snake_dir[0],
            snake[0][1] + snake_dir[1]
        )

        snake.insert(0, head)

        # Check if snake ate food
        if pg.Rect(head, (CELL_SIZE, CELL_SIZE)).colliderect(food):

            score += 1

            # Place food in a position not occupied by snake
            while True:

                new_food_position = (
                    random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE)
                )

                if new_food_position not in snake:
                    food.topleft = new_food_position
                    break

        else:
            # Remove tail if food was not eaten
            snake.pop()


        # -------------------------
        # COLLISION DETECTION
        # -------------------------

        # Collision with itself
        if head in snake[1:]:

            reset_game()

        # Collision with screen boundaries
        elif (
            head[0] < 0
            or head[0] >= WIDTH
            or head[1] < 0
            or head[1] >= HEIGHT
        ):

            reset_game()


    # -------------------------
    # RENDERING
    # -------------------------

    screen.fill((0, 0, 0))

    # Draw snake
    for pos in snake:

        pg.draw.rect(
            screen,
            (0, 255, 0),
            (pos[0], pos[1], CELL_SIZE, CELL_SIZE)
        )

    # Draw food
    pg.draw.rect(screen, (255, 0, 0), food)

    # Draw score
    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    # Update display
    pg.display.flip()

    # Control game speed
    clock.tick(10)


pg.quit()
