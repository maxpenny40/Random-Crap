import pygame, random

pygame.init()

WHITE = [0,0,0]

class player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([30,30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def moveRight(self,pixels):
        self.rect.x += pixels

    def moveLeft(self,pixels):
        self.rect.x -= pixels

    def moveUp(self,speed):
        self.rect.y -= speed

    def moveDown(self,pixels):
         self.rect.y += speed