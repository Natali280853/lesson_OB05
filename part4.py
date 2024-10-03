import pygame
import time
import random

pygame.init()

# Размер экрана
width = 800
height = 600

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Размер блока и скорость змейки
block_size = 20
snake_speed = 15

# Инициализация экрана
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Шрифт и размер текста
font = pygame.font.SysFont(None, 30)

# Функция отрисовки змейки
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

# Отображение сообщения на экране
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [width/2, height/2])

# Основной игровой цикл
def game_loop():
    game_over = False
    game_close = False

    # Позиция змейки
    lead_x = width/2
    lead_y = height/2
    lead_x_change = 0
    lead_y_change = 0

    # Длина змейки
    snake_list = []
    snake_length = 1

    # Позиция еды
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message_to_screen("Вы проиграли! Нажмите C для продолжения или Q для выхода", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(white)
        pygame.draw.rect(game_display, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(block_size, snake_list)

        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()

game_loop()
