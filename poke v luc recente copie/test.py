import pygame, sys


pygame.init()
clock = pygame.time.Clock()
import pygame.mixer
import pygame.mixer_music
pygame.mixer.init()
#screen width and height
screenwidth = 1500  #Choose your screen size
screenheight = int((800/1000)*screenwidth)





#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))


#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

policearial = pygame.font.Font("Pokemon.ttf", 35)

background1Img = pygame.image.load('Zone1.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0

def background1():
    screen.blit(background1Img, (background1X, background1Y))

running = True
while running:

    

    background1()


    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        


    pygame.display.update()
    clock.tick(20)