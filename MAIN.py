import pygame
from car.py import Car

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
SKYBLUE = (0,150,255)
YELLOW = (255,255,0)
GREY = (210,210,210)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame Demo')

all_sprites = pygame.sprite.Group()

playerCar = Car(RED,20,30)
playerCar.rect.x = 350
playerCar.rect.y

all_sprites.add(playerCar)

done = False

clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites.update()

    screen.fill(GREEN)

    pygame.draw.rect(screen, GREY, [40,0,200,300],0)
    pygame.draw.line(screen, WHITE, [140,0], [140,300], 5)

    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
