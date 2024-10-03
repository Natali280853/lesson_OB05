import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# Размер экрана
WIDTH = 400
HEIGHT = 600

# Размер блока
BLOCK_SIZE = 20

# Сетка игрового поля
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')

# Функция отрисовки блока
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Инициализация игрового поля
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Тетрамино
tetrominos = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]]  # S
]

# Цвета тетрамино
colors = [CYAN, MAGENTA, YELLOW, GREEN, RED, BLUE, WHITE]

# Генерация нового тетрамино
def new_tetromino():
    tetromino = random.choice(tetrominos)
    color = random.choice(colors)
    x = GRID_WIDTH // 2 - len(tetromino[0]) // 2
    y = 0
    return tetromino, color, x, y

# Падение тетрамино на один блок вниз
def move_down():
     global tetromino, color, x, y
     if check_collision(tetromino, x, y + 1):
         merge_tetromino(tetromino, x, y, color)
         tetromino, color, x, y = new_tetromino()
     else:
         y += 1

# Проверка столкновения
def check_collision(tetromino, x, y):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[0])):
            if tetromino[i][j] and (y + i >= GRID_HEIGHT or x + j < 0 or x + j >= GRID_WIDTH or grid[y + i][x + j]):
                return True
    return False

# Объединение тетрамино с игровым полем
def merge_tetromino(tetromino, x, y, color):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[0])):
            if tetromino[i][j]:
                grid[y + i][x + j] = color

# Отрисовка игрового поля
def draw_grid():
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            draw_block(j, i, grid[i][j] if grid[i][j] else BLACK)

# Поворот тетрамино по часовой стрелке
def rotate_tetromino(tetromino):
    return [list(row) for row in zip(*tetromino[::-1])]

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
tetromino, color, x, y = new_tetromino()

while running:
    screen.fill(BLACK)
    draw_grid()
    for i in range(len(tetromino)):
        for j in range(len(tetromino[0])):
            if tetromino[i][j]:
                draw_block(x + j, y + i, color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Обработка нажатия клавиши вверх для вращения тетрамино
            if event.key == pygame.K_UP:
                rotated_tetromino = rotate_tetromino(tetromino)
                if not check_collision(rotated_tetromino, x, y):
                    tetromino = rotated_tetromino
            if event.key == pygame.K_LEFT:
                if not check_collision(tetromino, x - 1, y):
                    x -= 1
            elif event.key == pygame.K_RIGHT:
                if not check_collision(tetromino, x + 1, y):
                    x += 1
            elif event.key == pygame.K_DOWN:
                if not check_collision(tetromino, x, y + 1):
                    y += 1

    move_down()
    pygame.display.flip()
    clock.tick(5)


pygame.quit()
