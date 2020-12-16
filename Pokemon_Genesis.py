import pygame, sys


pygame.init()
clock = pygame.time.Clock()

#screen width and height
screenwidth = 1500  #Choose your screen size
screenheight = int((625/1000)*screenwidth)


#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))


#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


#title and icon
pygame.display.set_caption("pokemon")
icon = pygame.image.load('Pokeball.png')
pygame.display.set_icon(icon)

#resize png image: fotoflexer



#background image
background1Img = pygame.image.load('Forest.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0

class Feuillosaure(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        image21 = pygame.image.load('2ndPokemon-1.png')
        image21 = pygame.transform.scale(image21, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image22 = pygame.image.load('2ndPokemon-2.png')
        image22 = pygame.transform.scale(image22, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image23 = pygame.image.load('2ndPokemon-3.png')
        image23 = pygame.transform.scale(image23, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image24 = pygame.image.load('2ndPokemon-4.png')
        image24 = pygame.transform.scale(image24, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image25 = pygame.image.load('2ndPokemon-5.png')
        image25 = pygame.transform.scale(image25, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image26 = pygame.image.load('2ndPokemon-6.png')
        image26 = pygame.transform.scale(image26, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image27 = pygame.image.load('2ndPokemon-7.png')
        image27 = pygame.transform.scale(image27, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image28 = pygame.image.load('2ndPokemon-8.png')
        image28 = pygame.transform.scale(image28, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image29 = pygame.image.load('2ndPokemon-9.png')
        image29 = pygame.transform.scale(image29, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image210 = pygame.image.load('2ndPokemon-10.png')
        image210 = pygame.transform.scale(image210, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image211 = pygame.image.load('2ndPokemon-11.png')
        image211 = pygame.transform.scale(image211, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image212 = pygame.image.load('2ndPokemon-12.png')
        image212 = pygame.transform.scale(image212, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image212 = pygame.image.load('2ndPokemon-14.png')
        image212 = pygame.transform.scale(image212, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image213 = pygame.image.load('2ndPokemon-15.png')
        image213 = pygame.transform.scale(image213, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image214 = pygame.image.load('2ndPokemon-16.png')
        image214= pygame.transform.scale(image214, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image215 = pygame.image.load('2ndPokemon-17.png')
        image215 = pygame.transform.scale(image215, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image216 = pygame.image.load('2ndPokemon-18.png')
        image216 = pygame.transform.scale(image216, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image217 = pygame.image.load('2ndPokemon-19.png')
        image217 = pygame.transform.scale(image217, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image218 = pygame.image.load('2ndPokemon-20.png')
        image218 = pygame.transform.scale(image218, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image219= pygame.image.load('2ndPokemon-21.png')
        image219 = pygame.transform.scale(image219, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image220 = pygame.image.load('2ndPokemon-22.png')
        image220= pygame.transform.scale(image220, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image221 = pygame.image.load('2ndPokemon-23.png')
        image221 = pygame.transform.scale(image221, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image222 = pygame.image.load('2ndPokemon-24.png')
        image222 = pygame.transform.scale(image222, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image223 = pygame.image.load('2ndPokemon-25.png')
        image223= pygame.transform.scale(image223, (int((22/100)*screenwidth), int((43/100)*screenheight)))


        self.sprites.append(image21)
        self.sprites.append(image22)
        self.sprites.append(image23)
        self.sprites.append(image24)
        self.sprites.append(image25)
        self.sprites.append(image26)
        self.sprites.append(image27)
        self.sprites.append(image28)
        self.sprites.append(image29)
        self.sprites.append(image210)
        self.sprites.append(image211)
        self.sprites.append(image212)
        self.sprites.append(image213)
        self.sprites.append(image214)
        self.sprites.append(image215)
        self.sprites.append(image216)
        self.sprites.append(image217)
        self.sprites.append(image218)
        self.sprites.append(image219)
        self.sprites.append(image220)
        self.sprites.append(image221)
        self.sprites.append(image222)
        self.sprites.append(image223)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((25/100)*screenwidth, (60/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]



all_sprites2 = pygame.sprite.Group()
feuillosaure = Feuillosaure()
all_sprites2.add(feuillosaure)



#Barre de vie pokemon 1
HPbar = pygame.image.load('Sprite barre de vie.png')
HPbar = pygame.transform.scale(HPbar, (int((43/100)*screenwidth), int((67/100)*screenheight)))
HPbarX = (1/100)*screenwidth
HPbarY = (5/100)*screenheight
colorHPbar = (0, 255, 0)

#barre vie 1
barposX = ((1/100)*screenwidth)+(1/100)*int((33/100)*screenwidth)
barposY = ((22/100)*screenheight)+(100/1000)*int((33/100)*screenheight)
barwidth = int((440/1000)*(33/100)*screenwidth)
barheight = int((17/100)*(9/100)*screenheight)



#pikachu ennemi animé
class Pikachu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        image1 = pygame.image.load('tile000.png')
        image1 = pygame.transform.scale(image1, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image2 = pygame.image.load('tile001.png')
        image2 = pygame.transform.scale(image2, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image3 = pygame.image.load('tile002.png')
        image3 = pygame.transform.scale(image3, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image4 = pygame.image.load('tile003.png')
        image4 = pygame.transform.scale(image4, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image5 = pygame.image.load('tile004.png')
        image5 = pygame.transform.scale(image5, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image6 = pygame.image.load('tile005.png')
        image6 = pygame.transform.scale(image6, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image7 = pygame.image.load('tile006.png')
        image7 = pygame.transform.scale(image7, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image8 = pygame.image.load('tile007.png')
        image8 = pygame.transform.scale(image8, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image9 = pygame.image.load('tile008.png')
        image9 = pygame.transform.scale(image9, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image10 = pygame.image.load('tile009.png')
        image10 = pygame.transform.scale(image10, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image11 = pygame.image.load('tile010.png')
        image11 = pygame.transform.scale(image11, (int((40/100)*screenwidth), int((60/100)*screenheight)))

        image12 = pygame.image.load('tile011.png')
        image12 = pygame.transform.scale(image12, (int((40/100)*screenwidth), int((60/100)*screenheight)))


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
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)
        self.sprites.append(image12)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((75/100)*screenwidth, (35/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]



all_sprites = pygame.sprite.Group()
pikachu = Pikachu()
all_sprites.add(pikachu)









#Barre de vie pokemon 2
HPbar2 = pygame.image.load('sprite barre de vie ennemy.png')
HPbar2 = pygame.transform.scale(HPbar2, (int((43/100)*screenwidth), int((67/100)*screenheight)))
HPbar2X = (68/100)*screenwidth
HPbar2Y = (5/100)*screenheight
colorHPbar = (0, 255, 0)

#barre vie 2
barpos2X = (HPbar2X+(11/100)*int((33/100)*screenwidth))
barpos2Y = (HPbar2Y+(105/1000)*int((33/100)*screenheight))
barwidth2 = int((783/1000)*(33/100)*screenwidth)
barheight2 = int((17/100)*(9/100)*screenheight)





#on defini les fonctions qui affichent à l'ecran

def button1():
    screen.blit(button1Img, (-80, 630))

def button1v2():
    screen.blit(button1v2Img, (-80, 630))

def background1():
    screen.blit(background1Img, (background1X, background1Y))

def barrevie1():
    screen.blit(HPbar, (855, 260))

def barrevie2():
    screen.blit(HPbar2, (-70, -160))



#button1
button1Img = pygame.image.load('attack.png')
button1Img = pygame.transform.scale(button1Img, (int((63/100)*screenwidth), int((62/100)*screenheight)))
button1X = (1/100)*screenwidth
button1Y = (80/100)*screenheight

widthB1 = int((63/100)*screenwidth)
heightB1 = int((62/100)*screenheight)
click1=0

#button1v2
button1v2Img = pygame.image.load('attack2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((63/100)*screenwidth), int((62/100)*screenheight)))
button1v2X = (1/100)*screenwidth
button1v2Y = (80/100)*screenheight



attackValue = 30

timeCount = 0





#game loop
running = True
while running:
                    #RGB
    screen.fill((50, 250, 50))

    #track pointeur
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        #si la souris est sur le button1
        if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
            if click[0] == 1:
                barwidth2 -= attackValue












    if barwidth2 < 0:
        attackValue = 0
        #print ('pikachu is dead')







    #on appelle les fonctions pour afficher un objet
    screen.fill(white)
    background1()
    button1()
    barrevie1()
    barrevie2()


    #appelle class sprite + affiche les sprites
    all_sprites.update()
    all_sprites.draw(screen)
    all_sprites2.update()
    all_sprites2.draw(screen)



    #si la souris passe sur le button1 alors il change de couleur
    if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
        button1v2()



    #dessine la barre de vie
    pygame.draw.rect(screen, colorHPbar, ((barposX, barposY, barwidth , barheight)))
    pygame.draw.rect(screen, colorHPbar, ((barpos2X, barpos2Y, barwidth2 , barheight2)))


    #rafraichi en continu

    pygame.display.update()
    clock.tick(20)














pygame.quit()