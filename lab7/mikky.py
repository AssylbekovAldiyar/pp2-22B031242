import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((1400, 1000))

clock = pygame.time.Clock()

image = pygame.image.load(r'C:\Users\Алдияр\Desktop\Proggrams\pp2\lab7\mikkyclock\mickeyclockbase.png')
image_Sec=pygame.image.load(r'C:\Users\Алдияр\Desktop\Proggrams\pp2\lab7\mikkyclock\second.png')
image_Min=pygame.image.load(r'C:\Users\Алдияр\Desktop\Proggrams\pp2\lab7\mikkyclock\minut.png')

topleft = (0, 0)
done = False

def blitRotateCenter(surf, image, topleft, angle):
    print(angle)
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        t = datetime.datetime.now()
        angleS = -(int(t.strftime("%S")) * 6) - 6
        angleM = -(int(t.strftime("%M")) * 6 + (int(t.strftime("%S")) * 6 / 60)) - 54
        screen.blit(image, topleft) 
        
        blitRotateCenter(screen,image_Min,topleft,angleM)
        blitRotateCenter(screen,image_Sec,topleft,angleS)
        pygame.display.flip()
        clock.tick(60)