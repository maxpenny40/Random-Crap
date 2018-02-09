import random, pygame, time, os
#pygame.init()
##screen = pygame.display.set_mode((400,400))
#ssurface = pygame.Surface((100,100))
#image = pygame.image.load('teal.png')

x = 30
y = 30

#FIND IMAGE
_image_library = {}


def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((800,800))
done = False
is_circle = True
clock = pygame.time.Clock()
speed = 3
imgchoice = True
while not done:


        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_circle = not is_circle

    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= speed
    if pressed[pygame.K_DOWN]: y += speed
    if pressed[pygame.K_LEFT]: x -= speed
    if pressed[pygame.K_RIGHT]: x += speed

    screen.fill((255,255,0))

    if is_circle:
        colour = (255,100,0)

    else:
        colour = (0,0,0)
    #pygame.draw.circle(screen,colour,(x,y),10)

    if imgchoice == True:
        screen.blit(get_image('ADAM.jpeg'),(x,y))
    else:
        pygame.draw.circle(screen, colour, (x,y), 10)

    """
    screen.fill((0,255,255))

    screen.blit(get_image('teal.png'),(20,20))
    """   
    pygame.display.flip()
    clock.tick(60)
    speed += 0.01
    imgchoice = not imgchoice
pygame.quit()
exit()
