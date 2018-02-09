import pygame, random, time

from boundries import wall, player

pygame.init()

colour = (0,100,255)
pcolour = (230,55,90)
size = [800,800]
surface = pygame.display.set_mode(size)
pygame.display.set_caption('The Maze v1.0')

player1 = player(pcolour, 50,50)
wall1 = wall(colour, 60, 80)
wall1.rect.x = 100
wall1.rect.y = 100

allwalls = pygame.sprite.Group()
allwalls.add(wall1)

everything = pygame.sprite.Group()
everything.add(wall1)
everything.add(player1)


clock = pygame.time.Clock()

finish = False

while finish == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.moveleft(1)
    if keys[pygame.K_RIGHT]:
        player.moveright(1)
    if keys[pygame.K_UP]:
        player.moveup(1)
    if keys[pygame.K_DOWN]:
        player.movedown(1)

    everything.update()

    surface.fill((0,0,50))

    allwalls.draw(surface)
    everything.draw(surface)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

