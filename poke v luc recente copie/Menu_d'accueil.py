import pygame, sys


pygame.init()
clock = pygame.time.Clock()
import pygame.mixer
import pygame.mixer_music
pygame.mixer.init()
#screen width and height
screenwidth = 1500  #Choose your screen size
screenheight = int((700/1000)*screenwidth)





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

        image11 = pygame.image.load('POKEMON2-1.png')
        image11= pygame.transform.scale(image11, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image21 = pygame.image.load('POKEMON2-2.png')
        image21 = pygame.transform.scale(image21, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image31 = pygame.image.load('POKEMON2-31.png')
        image31 = pygame.transform.scale(image31, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image41 = pygame.image.load('POKEMON2-41.png')
        image41 = pygame.transform.scale(image41, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image51 = pygame.image.load('POKEMON2-51.png')
        image51 = pygame.transform.scale(image51, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image61 = pygame.image.load('POKEMON2-61.png')
        image61 = pygame.transform.scale(image61, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image71 = pygame.image.load('POKEMON2-7.png')
        image71 = pygame.transform.scale(image71, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image81 = pygame.image.load('POKEMON2-8.png')
        image81 = pygame.transform.scale(image81, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image91 = pygame.image.load('POKEMON2-9.png')
        image91 = pygame.transform.scale(image91, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image101 = pygame.image.load('POKEMON2-10.png')
        image101 = pygame.transform.scale(image101, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image111 = pygame.image.load('POKEMON2-11.png')
        image111 = pygame.transform.scale(image111, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image121 = pygame.image.load('POKEMON2-12.png')
        image121 = pygame.transform.scale(image121, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image131 = pygame.image.load('POKEMON2-13.png')
        image131 = pygame.transform.scale(image131, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image141 = pygame.image.load('POKEMON2-14.png')
        image141 = pygame.transform.scale(image141, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image151 = pygame.image.load('POKEMON2-15.png')
        image151= pygame.transform.scale(image151, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image161 = pygame.image.load('POKEMON2-16.png')
        image161 = pygame.transform.scale(image161, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image171 = pygame.image.load('POKEMON2-17.png')
        image171 = pygame.transform.scale(image171, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image181 = pygame.image.load('POKEMON2-18.png')
        image181 = pygame.transform.scale(image181, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image191 = pygame.image.load('POKEMON2-19.png')
        image191 = pygame.transform.scale(image191, (int((70/100)*screenwidth), int((50/100)*screenheight)))

        image201= pygame.image.load('POKEMON2-20.png')
        image201 = pygame.transform.scale(image201, (int((70/100)*screenwidth), int((50/100)*screenheight)))



        self.sprites.append(image11)
        self.sprites.append(image21)
        self.sprites.append(image31)
        self.sprites.append(image41)
        self.sprites.append(image51)
        self.sprites.append(image61)
        self.sprites.append(image71)
        self.sprites.append(image81)
        self.sprites.append(image91)
        self.sprites.append(image101)
        self.sprites.append(image111)
        self.sprites.append(image121)
        self.sprites.append(image131)
        self.sprites.append(image141)
        self.sprites.append(image151)
        self.sprites.append(image161)
        self.sprites.append(image171)
        self.sprites.append(image181)
        self.sprites.append(image191)
        self.sprites.append(image201)

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
                import PokeGenesis23versionBonSac

    
    
    
    if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
        button1v2()
    
    
    pygame.display.update()
    clock.tick(20)
                








