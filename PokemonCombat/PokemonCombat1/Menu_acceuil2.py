import pygame, sys


pygame.init()
clock = pygame.time.Clock()
import pygame.mixer
import pygame.mixer_music
pygame.mixer.init()
#screen width and height
screenwidth = 1200  #Choose your screen size
screenheight = int((625/1000)*screenwidth)





#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))


#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

policearial = pygame.font.Font("Pokemon.ttf", 15)


class POKEMON2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []



        num3 = 1
        for i in range (1, 20):
            num3 += 1

            name3 = str('POKEMON2-' + str(num3) + '.png')

            frame3 = pygame.image.load(name3)
            frame3 = pygame.transform.scale(frame3, (int((70/100)*screenwidth), int((50/100)*screenheight)))

            self.sprites.append(frame3)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((50/100)*screenwidth, (20/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]



all_sprites3 = pygame.sprite.Group()
Pokemon2 = POKEMON2()
all_sprites3.add(Pokemon2)


button1Img = pygame.image.load('Jouer.png')
button1Img = pygame.transform.scale(button1Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))
button1X = (41.5/100)*screenwidth
button1Y = (85/100)*screenheight

button1v2Img = pygame.image.load('Jouer2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))
button1v2X = (41.5/100)*screenwidth
button1v2Y = (85/100)*screenheight

background1Img = pygame.image.load('ImageMenuTitre.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0



widthB = int((15/100)*screenwidth)
heightB = int((9.5/100)*screenheight)
click1=0

textcredits = policearial.render("Réalisé par Luc Bernacki et William Flouret",1,black)


pygame.mixer_music.load("PokemonTitleTrue.wav")
pygame.mixer.music.play(loops=-1, fade_ms=2)


def button1():
    screen.blit(button1Img, (button1X, button1Y))

def button1v2():
    screen.blit(button1v2Img, (button1v2X, button1v2Y))

def background1():
    screen.blit(background1Img, (background1X, background1Y))

def credits():
    screen.blit(textcredits, (int((2/100)*screenwidth), int((95/100)*screenheight)))

gameopen=pygame.mixer.Sound('opengame.wav')

running = True
while running:



    background1()
    button1()
    all_sprites3.update()
    all_sprites3.draw(screen)
    credits()



    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
            if click[0] == 1:
                gameopen.play()
                import Pokemon_Interface_GénésisTrue




    if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
        button1v2()


    pygame.display.update()
    clock.tick(20)