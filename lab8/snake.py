import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Создание окна игры
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Заголовок окна
pygame.display.set_caption('Змейка')

# Создание часов для управления временем
clock = pygame.time.Clock()

# Определение переменных для игры
snake_block_size = 10
snake_speed = 15

# Определение функции для рисования змеи
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block_size, snake_block_size])

# Определение функции для вывода сообщения на экран
def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    message = font_style.render(msg, True, color)
    screen.blit(message, [SCREEN_WIDTH/6, SCREEN_HEIGHT/3])

# Определение функции для запуска игры
def game_loop():

    # Определение переменных для змеи и еды
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block_size) / 10.0) * 10.0

    # Определение переменных для уровней и счетчика
    level = 1
    score = 0

    while not game_over:

        while game_close == True:
            # Вывод сообщения на экран при проигрыше и определение дальнейших действий игрока
            screen.fill(WHITE)
            message("Вы проиграли! Нажмите Q-выход или C-играть еще раз", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Обработка событий в игре
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Проверка на столкновение со стеной и покидание игровой зоны
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        # Обновление координат змеи
        x1 += x1_change
        y1 += y1_change

        # Закраска экрана белым цветом
        screen.fill(WHITE)

        # Рисование еды
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block_size, snake_block_size])

        # Обновление координат еды, если змея съела ее
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block_size) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10

            # Увеличение скорости при переходе на следующий уровень
            if score <= 0:
                snake_speed += 5
                level += 1

        # Добавление головы змеи в начало списка
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Удаление последнего элемента списка, если длина змеи превышает текущую
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с телом змеи
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Рисование змеи
        draw_snake(snake_block_size, snake_List)

        # Отображение счета на экране
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(text, (10, 10))

        # Отображение уровня на экране
        text = font.render("Level: " + str(level), True, BLACK)
        screen.blit(text, (SCREEN_WIDTH - 80, 10))

        # Обновление экрана
        pygame.display.update()

        # Установка FPS и обновление времени
        clock.tick(15)

    # Закрытие окна Pygame
    pygame.quit()

# Запуск игры
game_loop()

