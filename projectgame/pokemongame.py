import pygame, sys, random


pygame.init()
clock = pygame.time.Clock()

#screen width and height
screenwidth = 1200  #Choose your screen size
screenheight = int((625/1000)*screenwidth)


#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))


#basic colors and text
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)




#title and icon
pygame.display.set_caption("pokemon")
icon = pygame.image.load('Pokeball.png')
pygame.display.set_icon(icon)


#resize png image: fotoflexer


#background image
background1Img = pygame.image.load('hills2.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0





#Barre de vie pokemon 1
HPbar = pygame.image.load('HPbar.png')
HPbar = pygame.transform.scale(HPbar, (int((33/100)*screenwidth), int((9/100)*screenheight)))
HPbarX = (1/100)*screenwidth
HPbarY = (5/100)*screenheight
colorHPbar = green

#barre vie 1
barposX = ((1/100)*screenwidth)+(11/100)*int((33/100)*screenwidth)
barposY = ((5/100)*screenheight)+(105/1000)*int((33/100)*screenheight)
barwidth = int((783/1000)*(33/100)*screenwidth)
barheight = int((17/100)*(9/100)*screenheight)
barwidthOG = int((783/1000)*(33/100)*screenwidth)


Xennemy = (78/100)*screenwidth
Xallie =  (20/100)*screenwidth


#pikachu ennemi animé
class Pikachu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        image1 = pygame.image.load('tile000.png')
        image1 = pygame.transform.scale(image1, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image2 = pygame.image.load('tile001.png')
        image2 = pygame.transform.scale(image2, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image3 = pygame.image.load('tile002.png')
        image3 = pygame.transform.scale(image3, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image4 = pygame.image.load('tile003.png')
        image4 = pygame.transform.scale(image4, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image5 = pygame.image.load('tile004.png')
        image5 = pygame.transform.scale(image5, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image6 = pygame.image.load('tile005.png')
        image6 = pygame.transform.scale(image6, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image7 = pygame.image.load('tile006.png')
        image7 = pygame.transform.scale(image7, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image8 = pygame.image.load('tile007.png')
        image8 = pygame.transform.scale(image8, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image9 = pygame.image.load('tile008.png')
        image9 = pygame.transform.scale(image9, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image10 = pygame.image.load('tile009.png')
        image10 = pygame.transform.scale(image10, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image11 = pygame.image.load('tile010.png')
        image11 = pygame.transform.scale(image11, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        image12 = pygame.image.load('tile011.png')
        image12 = pygame.transform.scale(image12, (int((30/100)*screenwidth), int((50/100)*screenheight)))


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
        self.rect.center = (Xennemy, (25/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            
        global Xennemy
        
        if deathennemy:
            Xennemy += 10
            self.rect.center = (Xennemy, (25/100)*screenheight)
            


        self.image = self.sprites[int(self.current_sprite)]



class Feuillausaure(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        imageB1 = pygame.image.load('feuill1.png')
        imageB1 = pygame.transform.scale(imageB1, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        imageB2 = pygame.image.load('feuill2.png')
        imageB2 = pygame.transform.scale(imageB2, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        imageB3 = pygame.image.load('feuill3.png')
        imageB3 = pygame.transform.scale(imageB3, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        imageB4 = pygame.image.load('feuill4.png')
        imageB4 = pygame.transform.scale(imageB4, (int((30/100)*screenwidth), int((50/100)*screenheight)))

        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB1)
        self.sprites.append(imageB2)
        self.sprites.append(imageB3)
        self.sprites.append(imageB4)
        self.sprites.append(imageB4)
        self.sprites.append(imageB4)
        self.sprites.append(imageB4)
        self.sprites.append(imageB4)
        self.sprites.append(imageB3)
        self.sprites.append(imageB2)


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


        self.rect = self.image.get_rect()
        self.rect.center = ((20/100)*screenwidth, (50/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            
        global Xallie
        
        if deathallie:
            Xallie -= 10
            self.rect.center = (Xallie, (50/100)*screenheight)
           

        self.image = self.sprites[int(self.current_sprite)]







all_sprites = pygame.sprite.Group()
pikachu = Pikachu()
feuillausaure = Feuillausaure()
all_sprites.add(pikachu)
all_sprites.add(feuillausaure)







#Barre de vie pokemon 2
HPbar2 = pygame.image.load('HPbar.png')
HPbar2 = pygame.transform.scale(HPbar2, (int((33/100)*screenwidth), int((9/100)*screenheight)))
HPbar2X = (68/100)*screenwidth
HPbar2Y = (5/100)*screenheight
colorHPbar2 = green

#barre vie 2
barpos2X = (HPbar2X+(11/100)*int((33/100)*screenwidth))
barpos2Y = (HPbar2Y+(105/1000)*int((33/100)*screenheight))
barwidth2 = int((783/1000)*(33/100)*screenwidth)
barheight2 = int((17/100)*(9/100)*screenheight)
barwidthOG2 = int((783/1000)*(33/100)*screenwidth)





#on defini les fonctions qui affichent à l'ecran


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

def Tour():
    screen.blit(texttour, (int((30/100)*screenwidth), int((90/100)*screenheight)))

def Tour2():
    screen.blit(texttour2, (int((30/100)*screenwidth), int((90/100)*screenheight)))





#button1
button1Img = pygame.image.load('attack1.png')
button1Img = pygame.transform.scale(button1Img, (int((20/100)*screenwidth), int((15/100)*screenheight)))
button1X = (1/100)*screenwidth
button1Y = (84/100)*screenheight

widthB1 = int((27/100)*screenwidth)
heightB1 = int((20/100)*screenheight)
click1=0

#button1v2
button1v2Img = pygame.image.load('attack2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((20/100)*screenwidth), int((15/100)*screenheight)))
button1v2X = (1/100)*screenwidth
button1v2Y = (84/100)*screenheight



attackValue = random.randint((10/100)*barwidthOG, (30/100)*barwidthOG)

timeCount = 0

yourturn = True

attack = False
current_tour = 0

deathennemy = False
deathallie = False

policearial = pygame.font.SysFont("Arial", 35, 1, 1)
texttour = policearial.render("A vous de jouer.", 1, white)
texttour2 = policearial.render("Tour ennemi.", 1, white)



#game loop
running = True
while running:

                    #RGB
    #screen.fill((50, 250, 50))

    

    
    #track pointeur
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        #si la souris est sur le button1
        if attack == False:
            if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
                if click[0] == 1:
                    #barwidth2 -= attackValue
                    attack = True
                    if barwidth2 > 0:
                        attackValue = random.randint(20, 80)
                    
                        if barwidth2 <= int((65/100)*barwidthOG):
                            colorHPbar2 = yellow
                            
                        if barwidth2 <= int((35/100)*barwidthOG):
                            colorHPbar2 = red
                            
                        if attackValue >= barwidth2:
                            attackValue = barwidth2
                            barwidth2 -= attackValue
                            deathennemy = True
                        else:
                            barwidth2 -= attackValue
                            
    if Xennemy >= screenwidth+100:
        deathennemy = False
        all_sprites.remove(pikachu)
        
    if Xallie <= -150:
        deathallie = False
        all_sprites.remove(feuillausaure)
                            

    
    


    #•if deathennemy:
        #Xennemy += 100

    #on appelle les fonctions pour afficher un objet
    #screen.fill(white)
    background1()
    button1()
    barrevie1()
    barrevie2()
    #screen.blit(texttour, (500, 700))



    if attack == True and deathennemy == False:
        Tour2()
        current_tour += 0.1
        #print (current_tour)
        
        if current_tour == 1.3 and barwidth > 0:
            attackValue = random.randint(10, 80)
            if barwidth <= int((65/100)*barwidthOG):
                colorHPbar = yellow
                            
            if barwidth <= int((35/100)*barwidthOG):
                colorHPbar = red
                
            if attackValue >= barwidth:
                attackValue = barwidth
                barwidth -= attackValue
                deathallie = True
            else:
                barwidth -= attackValue
            
        if attackValue >= barwidth2:
            attackValue = barwidth2
            
        #if barwidth < 0:
            #print ('pikachu fainted')
            
        if current_tour >= 3:
            attack = False

    else:
        Tour()
        current_tour = 0



    #if barwidth2 < 0:
        #attackValue = 0
        #print ('pikachu ennemi K.O')




    #appelle class sprite + affiche les sprites
    all_sprites.update()
    all_sprites.draw(screen)




    #si la souris passe sur le button1 alors il change de couleur
    if button1X <= mouse[0] <= button1X+widthB1 and button1Y <= mouse[1] <= button1Y+heightB1:
        button1v2()



    #dessine la barre de vie
    pygame.draw.rect(screen, colorHPbar, ((barposX, barposY, barwidth , barheight)))
    pygame.draw.rect(screen, colorHPbar2, ((barpos2X, barpos2Y, barwidth2 , barheight2)))


    #rafraichi en continu

    pygame.display.update()
    clock.tick(20)







#inutile stuff

#pokemon allié (lucario)
pokemon1Img = pygame.image.load('lucario.png')
pokemon1Img = pygame.transform.scale(pokemon1Img, (int((26/100)*screenwidth), int((57/100)*screenheight)))
pokemon1X = (1/100)*screenwidth
pokemon1Y = (10/100)*screenheight

def pokemon1():
    screen.blit(pokemon1Img, (pokemon1X, pokemon1Y))


#pokemon ennemi (pikachu)
pokemon2Img = pygame.image.load('pikachu.png')
pokemon2Img = pygame.transform.scale(pokemon2Img, (int((26/100)*screenwidth), int((57/100)*screenheight)))
pokemon2X = (68/100)*screenwidth
pokemon2Y = (10/100)*screenheight

def pokemon2():
    screen.blit(pokemon2Img, (pokemon2X, pokemon2Y))






pygame.quit()