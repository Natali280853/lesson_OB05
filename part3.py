import pygame
import random

# инициализация Pygame
pygame.init()

# определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# определение игрового поля
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# начальные координаты цели
target_x = random.randint(50, WIDTH-50)
target_y = random.randint(50, HEIGHT-50)
target_radius = 20
speed_x = random.choice([-1, 1]) * random.randint(1, 3)
speed_y = random.choice([-1, 1]) * random.randint(1, 3)

# начальные координаты пули
bullet_radius = 5
bullet_x = WIDTH // 2
bullet_y = HEIGHT - 20
bullet_speed = 5
bullet_fired = False

# основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not bullet_fired:
                bullet_x, bullet_y = pygame.mouse.get_pos()
                bullet_fired = True

    # обновление координат цели
    target_x += speed_x
    target_y += speed_y
    if target_x + target_radius > WIDTH or target_x - target_radius < 0:
        speed_x = -speed_x
    if target_y + target_radius > HEIGHT or target_y - target_radius < 0:
        speed_y = -speed_y

    # обновление координат пули
    if bullet_fired:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_fired = False

    # проверка попадания пули в цель
    if bullet_fired and abs(bullet_x - target_x) < target_radius and abs(bullet_y - target_y) < target_radius:
        target_x = random.randint(50, WIDTH-50)
        target_y = random.randint(50, HEIGHT-50)
        speed_x = random.choice([-1, 1]) * random.randint(1, 3)
        speed_y = random.choice([-1, 1]) * random.randint(1, 3)
        bullet_fired = False

    # очистка экрана
    screen.fill(WHITE)

    # рисуем цель
    pygame.draw.circle(screen, RED, (target_x, target_y), target_radius)

    # рисуем пулю
    if bullet_fired:
        pygame.draw.circle(screen, RED, (bullet_x, bullet_y), bullet_radius)

    # обновляем экран
    pygame.display.flip()

    # устанавливаем частоту обновления экрана
    pygame.time.Clock().tick(60)

# завершение работы Pygame
pygame.quit()
