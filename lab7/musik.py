import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 500))
done = True
play = True
num = 0

# Полный путь к каталогу с музыкой
path = r'C:\Users\Алдияр\Desktop\Proggrams\pp2\lab7\musik'

# Создание списка из имен файлов .mp3 в каталоге
songs = []
for file in os.listdir(path):
    if file.endswith(".mp3"):
        songs.append(file)

# Загрузка первой песни и ее проигрывание
pygame.mixer.music.load(os.path.join(path, songs[0]))
pygame.mixer.music.play()

clock = pygame.time.Clock()

while done:
    current = num
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play
            elif event.key == pygame.K_RIGHT:
                if num < len(songs)-1:
                    num += 1
                else:
                    num = 0
            elif event.key == pygame.K_LEFT:
                if num > 0:
                    num -= 1
                else:
                    num = len(songs)-1

    # Очистка экрана и отображение названия текущей песни
    screen.fill((0, 250, 109))
    font = pygame.font.SysFont("balker", 60)
    name = songs[num].replace('.mp3','')
    text = font.render(name, False, (112, 112, 255))
    text_rect = text.get_rect(center=(800/2, 500/2))
    screen.blit(text, text_rect)

    # Пауза/возобновление воспроизведения в зависимости от значения переменной play
    if play == False:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

    # Если выбрана новая песня, загрузить и проиграть ее
    if current != num:
        pygame.mixer.music.load(os.path.join(path, songs[num]))
        pygame.mixer.music.play()
        
    pygame.display.flip()
    clock.tick(60)
