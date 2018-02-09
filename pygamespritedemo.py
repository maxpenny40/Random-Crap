class adam(pygame.sprite.Sprite):
    colour = ((255,255,0))
    x = 30
    y = 30

    def __init__(self,colour,width,height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.rect_rect()
    
