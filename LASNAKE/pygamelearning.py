


import pygame, time, os, random, math

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#Background = Background('safari.jpeg', [0,0])

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

x = 30
y = 30

pygame.init()

screen = pygame.display.set_mode((1024,576))
background = pygame.image.load("safari.jpeg")
louistherat = pygame.image.load('louisrat.png').convert_alpha()
jamestherat = pygame.image.load('jamesrat.png').convert_alpha()
ewantherat = pygame.image.load("ewanrat.png").convert_alpha()

done = False

clock = pygame.time.Clock()
speed = 3

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= speed
    if pressed[pygame.K_DOWN]: y += speed
    if pressed[pygame.K_LEFT]: x -= speed
    if pressed[pygame.K_RIGHT]: x += speed

    screen.fill([0,0,0])
    screen.blit(background, (0,0))
    screen.blit(louistherat, (400,400))
    screen.blit(jamestherat, (100,500))
    screen.blit(ewantherat, (900,60))

    colour = (255,100,0)

 #   pygame.draw.circle(screen, colour, (x,y) , 10)
    screen.blit(get_image('ADAMLASNAKE.png'),(x,y))
    pygame.display.flip()
    clock.tick(60)
    speed += 0.01

pygame.quit()
exit()
