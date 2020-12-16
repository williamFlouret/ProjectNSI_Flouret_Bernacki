import pygame, sys
pygame.init()


screenwidth = 1200
screenheight = 1200

screen = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption ('test')


clock = pygame.time.Clock()


pikachu1 = pygame.image.load('pika1.png')

pikachu2 = [pygame.image.load('pika1.png'), pygame.image.load('pika2.png'), pygame.image.load('pika3.png')]
pikaX = 100
pikaY = 100

#basic colors and text
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

policearial = pygame.font.SysFont("Arial", 35, 1, 1)
texttour = policearial.render("A vous de jouer.", 1, white)
texttour2 = policearial.render("Tour ennemi.", 1, white)







class Pikachu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        image1 = pygame.image.load('tile000.png')
        image1 = pygame.transform.scale(image1, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image2 = pygame.image.load('tile001.png')
        image2 = pygame.transform.scale(image2, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image3 = pygame.image.load('tile002.png')
        image3 = pygame.transform.scale(image3, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image4 = pygame.image.load('tile003.png')
        image4 = pygame.transform.scale(image4, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image5 = pygame.image.load('tile004.png')
        image5 = pygame.transform.scale(image5, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image6 = pygame.image.load('tile005.png')
        image6 = pygame.transform.scale(image6, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image7 = pygame.image.load('tile006.png')
        image7 = pygame.transform.scale(image7, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image8 = pygame.image.load('tile007.png')
        image8 = pygame.transform.scale(image8, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image9 = pygame.image.load('tile008.png')
        image9 = pygame.transform.scale(image9, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image10 = pygame.image.load('tile009.png')
        image10 = pygame.transform.scale(image10, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image11 = pygame.image.load('tile010.png')
        image11 = pygame.transform.scale(image11, (int((70/100)*screenwidth), int((70/100)*screenheight)))

        image12 = pygame.image.load('tile011.png')
        image12 = pygame.transform.scale(image12, (int((70/100)*screenwidth), int((70/100)*screenheight)))


        self.sprites.append(image1)
        self.sprites.append(image2)
        self.sprites.append(image3)
        self.sprites.append(image4)
        self.sprites.append(image5)
        self.sprites.append(image6)
        self.sprites.append(image7)
        self.sprites.append(image8)
        self.sprites.append(image9)
        self.sprites.append(image10)
        self.sprites.append(image11)
        self.sprites.append(image12)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (screenwidth/2, screenheight/2)

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


#animationcount = 0

def pikapika():
    screen.blit(pikachu, (pikaX, pikaY))

def button1():
    screen.blit(button1Img, (button1X, button1Y))

def button1v2():
    screen.blit(button1v2Img, (button1v2X, button1v2Y))

def Tour():
    screen.blit(texttour, (500, 700))

def Tour2():
    screen.blit(texttour2, (500, 700))



all_sprites = pygame.sprite.Group()
pikachu = Pikachu()
all_sprites.add(pikachu)
#attak = Texte()
#all_sprites.add(attak)

#button1
button1Img = pygame.image.load('attack1.png')
button1Img = pygame.transform.scale(button1Img, (int((27/100)*screenwidth), int((20/100)*screenheight)))
button1X = (1/100)*screenwidth
button1Y = (80/100)*screenheight

widthB1 = int((27/100)*screenwidth)
heightB1 = int((20/100)*screenheight)
click1=0

#button1v2
button1v2Img = pygame.image.load('attack2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((27/100)*screenwidth), int((20/100)*screenheight)))
button1v2X = (1/100)*screenwidth
button1v2Y = (80/100)*screenheight

attack = False
attackvalue = 0
current_tour = 0

#gameloop
run = True
while run:
    clock.tick(10)
    screen.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()


    for event in pygame.event.get():



        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #si la souris est sur le button1
        if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
            if click[0] == 1:
                attackvalue += 1

                attack = True







    all_sprites.update()
    all_sprites.draw(screen)

    if attack:
        Tour2()
        current_tour += 0.1
        print (current_tour)
        if current_tour >= 2:
            attack = False

    else:
        Tour()
        current_tour = 0

    button1()

    #si la souris passe sur le button1 alors il change de couleur
    if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
        button1v2()





        #pikapika()

    pygame.display.update()


#inutile stuff


#class Texte(pygame.sprite.Sprite):
    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.sprites = []
        #self.sprites.append(texttour)
        #self.sprites.append(texttour2)


        #self.current_sprite = 0
        #self.image = self.sprites[self.current_sprite]

        #self.rect = self.image.get_rect()
        #self.rect.center = (screenwidth/2, screenheight/2)

    #def update(self):
        #if attack:
            #self.current_sprite = 1
            #self.current_sprite -= 0.1
            #if self.current_sprite < 0:
                #self.current_sprite = 1


        #self.image = self.sprites[int(self.current_sprite)]


