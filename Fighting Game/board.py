import pygame, random
from PLayer import player

pygame.init()

screen = pygame.display.set_mode([500,500])

pygame.display.set_caption('FIGHT')
screen.fill([50,100,250])

player1 = player(30,30)

player2 = player(100,100)

players = pygame.sprite.Group(player1, player2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break


    players.draw(screen)

    pygame.display.flip()