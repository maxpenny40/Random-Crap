import pygame, random

pygame.init()

colour = (0,0,255)

class wall(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.image.set_colorkey(colour)

        self.width = width
        self.height = height
        self.colour = colour


        pygame.draw.rect(self.image, self.colour, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def repaint(self,colour):
        colour = (random.randint(0,255),random.randint(0,255).random.randint(0,255))
        self.colour = colour


class player(pygame.sprite.Sprite):
    def __init__(self,pcolour, pwidth, pheight):
        super().__init__()

        self.image = pygame.Surface([pwidth,pheight])
        self.image.fill(pcolour)
        self.image.set_colorkey(pcolour)

        self.width = pwidth
        self.height = pheight
        self.colour = pcolour

        pygame.draw.rect(self.image, self.colour, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()

    def moveleft(self,pixels):
            self.rect.x -= pixels

    def moveright(self,pixels):
            self.rect.x += pixels

    def moveup(self,pixels):
            self.rect.y -= pixels

    def movedown(self,pixels):
            self.rect.y += pixels
