import pygame, sys


pygame.init()
clock = pygame.time.Clock()

#screen width and height
screenwidth = 1500  #Choose your screen size
screenheight = int((625/1000)*screenwidth)


#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))


#basic colors and text
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

policearial = pygame.font.SysFont("Arial", 35, 1, 1)
texttour = policearial.render("A vous de jouer.", 1, black)


#title and icon
pygame.display.set_caption("pokemon")
icon = pygame.image.load('Pokeball.png')
pygame.display.set_icon(icon)


#resize png image: fotoflexer


#background image
background1Img = pygame.image.load('background1.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0



#pokemon allié (lucario)
pokemon1Img = pygame.image.load('lucario.png')
pokemon1Img = pygame.transform.scale(pokemon1Img, (int((26/100)*screenwidth), int((57/100)*screenheight)))
pokemon1X = (1/100)*screenwidth
pokemon1Y = (10/100)*screenheight

#Barre de vie pokemon 1
HPbar = pygame.image.load('HPbar.png')
HPbar = pygame.transform.scale(HPbar, (int((33/100)*screenwidth), int((9/100)*screenheight)))
HPbarX = (1/100)*screenwidth
HPbarY = (5/100)*screenheight
colorHPbar = (0, 255, 0)

#barre vie 1
barposX = ((1/100)*screenwidth)+(11/100)*int((33/100)*screenwidth)
barposY = ((5/100)*screenheight)+(105/1000)*int((33/100)*screenheight)
barwidth = int((783/1000)*(33/100)*screenwidth)
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
        self.rect.center = ((75/100)*screenwidth, (45/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]



all_sprites = pygame.sprite.Group()
pikachu = Pikachu()
all_sprites.add(pikachu)









#Barre de vie pokemon 2
HPbar2 = pygame.image.load('HPbar.png')
HPbar2 = pygame.transform.scale(HPbar2, (int((33/100)*screenwidth), int((9/100)*screenheight)))
HPbar2X = (68/100)*screenwidth
HPbar2Y = (5/100)*screenheight
colorHPbar = (0, 255, 0)

#barre vie 2
barpos2X = (HPbar2X+(11/100)*int((33/100)*screenwidth))
barpos2Y = (HPbar2Y+(105/1000)*int((33/100)*screenheight))
barwidth2 = int((783/1000)*(33/100)*screenwidth)
barheight2 = int((17/100)*(9/100)*screenheight)





#on defini les fonctions qui affichent à l'ecran
def pokemon1():
    screen.blit(pokemon1Img, (pokemon1X, pokemon1Y))

def button1():
    screen.blit(button1Img, (button1X, button1Y))

def button1v2():
    screen.blit(button1v2Img, (button1v2X, button1v2Y))

def background1():
    screen.blit(background1Img, (background1X, background1Y))

def barrevie1():
    screen.blit(HPbar, (HPbarX, HPbarY))

def barrevie2():
    screen.blit(HPbar2, (HPbar2X, HPbar2Y))





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



attackValue = 40

timeCount = 0

yourturn = True

attack = False

def Tour():
    screen.blit(texttour, (500, 700))

def Tour2():
    screen.blit(texttour2, (500, 700))




#game loop
running = True
while running:

                    #RGB
    screen.fill((50, 250, 50))

    attack = False
    yourturn = True

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
                attack = True
                print (barwidth2)




    if yourturn:
        screen.blit(texttour, (500, 700))
        if attack:
            yourturn = False








    if barwidth2 < 0:
        attackValue = 0
        #print ('pikachu is dead')







    #on appelle les fonctions pour afficher un objet
    screen.fill(white)
    background1()
    pokemon1()
    button1()
    barrevie1()
    barrevie2()
    #screen.blit(texttour, (500, 700))
    Tour()

    #appelle class sprite + affiche les sprites
    all_sprites.update()
    all_sprites.draw(screen)




    #si la souris passe sur le button1 alors il change de couleur
    if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
        button1v2()



    #dessine la barre de vie
    pygame.draw.rect(screen, colorHPbar, ((barposX, barposY, barwidth , barheight)))
    pygame.draw.rect(screen, colorHPbar, ((barpos2X, barpos2Y, barwidth2 , barheight2)))


    #rafraichi en continu

    pygame.display.update()
    clock.tick(20)







#inutile stuff


#pokemon ennemi (pikachu)
pokemon2Img = pygame.image.load('pikachu.png')
pokemon2Img = pygame.transform.scale(pokemon2Img, (int((26/100)*screenwidth), int((57/100)*screenheight)))
pokemon2X = (68/100)*screenwidth
pokemon2Y = (10/100)*screenheight

def pokemon2():
    screen.blit(pokemon2Img, (pokemon2X, pokemon2Y))






pygame.quit()