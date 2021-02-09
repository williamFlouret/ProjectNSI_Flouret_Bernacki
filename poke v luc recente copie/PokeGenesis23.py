import pygame, sys, random
import subprocess
import os
import sys
pygame.init()
clock = pygame.time.Clock()

#screen width and height
screenwidth = 1200  #Choose your screen size
screenheight = int((625/1000)*screenwidth)
import pygame.mixer
import pygame.mixer_music
pygame.mixer.init()

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
background1Img = pygame.image.load('forest.png')
background1Img = pygame.transform.scale(background1Img, (screenwidth, screenheight))
background1X = 0
background1Y = 0

Barretexte = pygame.image.load('barretexte.png')
Barretexte = pygame.transform.scale(Barretexte,(int((100/100)*screenwidth),int((75/100)*screenheight)))
BarretexteX= (0/100)*screenwidth
BarretexteY= (30/100)*screenheight

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


Xennemy = (70/100)*screenwidth
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
        self.rect.center = (Xennemy, (40/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            
        global Xennemy
        
        if deathennemy:
            Xennemy += 10
            self.rect.center = (Xennemy, (40/100)*screenheight)
            

        self.image = self.sprites[int(self.current_sprite)]



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

        image224 = pygame.image.load('2ndPokemon-26.png')
        image224 = pygame.transform.scale(image224, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image225 = pygame.image.load('2ndPokemon-27.png')
        image225 = pygame.transform.scale(image225, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image226 = pygame.image.load('2ndPokemon-28.png')
        image226 = pygame.transform.scale(image226, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image227 = pygame.image.load('2ndPokemon-29.png')
        image227 = pygame.transform.scale(image227, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image228 = pygame.image.load('2ndPokemon-30.png')
        image228 = pygame.transform.scale(image228, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image229 = pygame.image.load('2ndPokemon-31.png')
        image229 = pygame.transform.scale(image229, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image230 = pygame.image.load('2ndPokemon-32.png')
        image230 = pygame.transform.scale(image230, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image231 = pygame.image.load('2ndPokemon-33.png')
        image231 = pygame.transform.scale(image231, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image232 = pygame.image.load('2ndPokemon-34.png')
        image232 = pygame.transform.scale(image232, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image233 = pygame.image.load('2ndPokemon-35.png')
        image233 = pygame.transform.scale(image233, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image234 = pygame.image.load('2ndPokemon-36.png')
        image234 = pygame.transform.scale(image234, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image235 = pygame.image.load('2ndPokemon-37.png')
        image235= pygame.transform.scale(image235, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image236 = pygame.image.load('2ndPokemon-38.png')
        image236 = pygame.transform.scale(image236, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image237 = pygame.image.load('2ndPokemon-39.png')
        image237 = pygame.transform.scale(image237, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image238 = pygame.image.load('2ndPokemon-40.png')
        image238 = pygame.transform.scale(image238, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image239 = pygame.image.load('2ndPokemon-41.png')
        image239 = pygame.transform.scale(image239, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image240= pygame.image.load('2ndPokemon-42.png')
        image240 = pygame.transform.scale(image240, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image241 = pygame.image.load('2ndPokemon-43.png')
        image241= pygame.transform.scale(image241, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image242 = pygame.image.load('2ndPokemon-44.png')
        image242 = pygame.transform.scale(image242, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image243 = pygame.image.load('2ndPokemon-45.png')
        image243 = pygame.transform.scale(image243, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image244 = pygame.image.load('2ndPokemon-46.png')
        image244= pygame.transform.scale(image244, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image245 = pygame.image.load('2ndPokemon-47.png')
        image245 = pygame.transform.scale(image245, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image246 = pygame.image.load('2ndPokemon-48.png')
        image246 = pygame.transform.scale(image246, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image247 = pygame.image.load('2ndPokemon-49.png')
        image247 = pygame.transform.scale(image247, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image248 = pygame.image.load('2ndPokemon-50.png')
        image248 = pygame.transform.scale(image248, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image249 = pygame.image.load('2ndPokemon-51.png')
        image249 = pygame.transform.scale(image249, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image250 = pygame.image.load('2ndPokemon-52.png')
        image250 = pygame.transform.scale(image250, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image251 = pygame.image.load('2ndPokemon-53.png')
        image251 = pygame.transform.scale(image251, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image252 = pygame.image.load('2ndPokemon-54.png')
        image252= pygame.transform.scale(image252, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image253 = pygame.image.load('2ndPokemon-55.png')
        image253 = pygame.transform.scale(image253, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image254 = pygame.image.load('2ndPokemon-56.png')
        image254 = pygame.transform.scale(image254, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image255 = pygame.image.load('2ndPokemon-57.png')
        image255 = pygame.transform.scale(image255, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image256 = pygame.image.load('2ndPokemon-58.png')
        image256 = pygame.transform.scale(image256, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image257 = pygame.image.load('2ndPokemon-59.png')
        image257 = pygame.transform.scale(image257, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image258 = pygame.image.load('2ndPokemon-60.png')
        image258 = pygame.transform.scale(image258, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image259 = pygame.image.load('2ndPokemon-61.png')
        image259 = pygame.transform.scale(image259, (int((22/100)*screenwidth), int((43/100)*screenheight)))

        image260 = pygame.image.load('2ndPokemon-62.png')
        image260 = pygame.transform.scale(image260, (int((22/100)*screenwidth), int((43/100)*screenheight)))


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
        self.sprites.append(image224)
        self.sprites.append(image225)
        self.sprites.append(image226)
        self.sprites.append(image227)
        self.sprites.append(image228)
        self.sprites.append(image229)
        self.sprites.append(image230)
        self.sprites.append(image231)
        self.sprites.append(image232)
        self.sprites.append(image233)
        self.sprites.append(image234)
        self.sprites.append(image235)
        self.sprites.append(image236)
        self.sprites.append(image237)
        self.sprites.append(image238)
        self.sprites.append(image239)
        self.sprites.append(image240)
        self.sprites.append(image241)
        self.sprites.append(image242)
        self.sprites.append(image243)
        self.sprites.append(image244)
        self.sprites.append(image245)
        self.sprites.append(image246)
        self.sprites.append(image247)
        self.sprites.append(image248)
        self.sprites.append(image249)
        self.sprites.append(image250)
        self.sprites.append(image251)
        self.sprites.append(image252)
        self.sprites.append(image253)
        self.sprites.append(image254)
        self.sprites.append(image255)
        self.sprites.append(image256)
        self.sprites.append(image257)
        self.sprites.append(image258)
        self.sprites.append(image259)
        self.sprites.append(image260)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((25/100)*screenwidth, (60/100)*screenheight)

    def update(self):
        self.current_sprite += 0.7

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            
        global Xallie
        
        if deathallie:
            Xallie -= 10
            self.rect.center = (Xallie, (60/100)*screenheight)
           

        self.image = self.sprites[int(self.current_sprite)]







all_sprites = pygame.sprite.Group()
pikachu = Pikachu()
feuillosaure = Feuillosaure()
all_sprites.add(pikachu)
all_sprites.add(feuillosaure)







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
def barretexte():
    screen.blit(Barretexte, (BarretexteX, BarretexteY))

def button1():
    screen.blit(button1Img, (button1X, button1Y))

def button1v2():
    screen.blit(button1v2Img, (button1v2X, button1v2Y))
    
def B2button1():
    screen.blit(B2button1Img, (B2buttonX, B2buttonY))
    
def B2button2():
    screen.blit(B2button2Img, (B2buttonX, B2buttonY))

def BoutonSac1():
    screen.blit(SacButtonImg, (SacButtonX, SacButtonY))

def BoutonSac2():
    screen.blit(SacButtonImg2, (SacButtonX, SacButtonY))

def background1():
    screen.blit(background1Img, (background1X, background1Y))

def barrevie1():
    screen.blit(HPbar, (HPbarX, HPbarY))

def barrevie2():
    screen.blit(HPbar2, (HPbar2X, HPbar2Y))

def Tour():
    screen.blit(texttour, (int((40/100)*screenwidth), int((85/100)*screenheight)))

def Tour2():
    screen.blit(texttour2, (int((40/100)*screenwidth), int((85/100)*screenheight)))

def txtdeathallie():
    screen.blit(textdeathallie, (int((40/100)*screenwidth), int((85/100)*screenheight)))
    
def txtdeathennemy():
    screen.blit(textdeathennemy, (int((40/100)*screenwidth), int((85/100)*screenheight)))
    
def txtmiss():
    screen.blit(textmiss, (int((22/100)*screenwidth), int((85/100)*screenheight)))

def coupcritique():
    screen.blit(textcritique, (int((50/100)*screenwidth), int((85/100)*screenheight)))





#1ebutton1
button1Img = pygame.image.load('2attack.png')
button1Img = pygame.transform.scale(button1Img, (int((15/100)*screenwidth), int((10/100)*screenheight)))
button1X = (2/100)*screenwidth
button1Y = (82.2/100)*screenheight

widthB = int((15/100)*screenwidth)
heightB = int((10/100)*screenheight)
click1=0

#1ebutton1v2
button1v2Img = pygame.image.load('2attack2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((15/100)*screenwidth), int((10/100)*screenheight)))
button1v2X = (2/100)*screenwidth
button1v2Y = (82.2/100)*screenheight

#2ebutton1
B2button1Img = pygame.image.load('attack.png')
B2button1Img = pygame.transform.scale(B2button1Img, (int((15/100)*screenwidth), int((10/100)*screenheight)))

B2buttonX = (2/100)*screenwidth
B2buttonY = (90/100)*screenheight

#2ebutton2
B2button2Img = pygame.image.load('attack2.png')
B2button2Img = pygame.transform.scale(B2button2Img, (int((15/100)*screenwidth), int((10/100)*screenheight)))

#bouton sac
SacButtonImg = pygame.image.load('sac.png')
SacButtonImg = pygame.transform.scale(SacButtonImg, (int((15/100)*screenwidth), int((10/100)*screenheight)))

SacButtonImg2 = pygame.image.load('2sac.png')
SacButtonImg2 = pygame.transform.scale(SacButtonImg2, (int((15/100)*screenwidth), int((10/100)*screenheight)))

SacButtonX = (82.5/100)*screenwidth
SacButtonY = (90/100)*screenheight






attackValue = random.randint((10/100)*barwidthOG, (30/100)*barwidthOG)
precision = random.randint(1, 3)

timeCount = 0
sound=pygame.mixer.Sound('sound.wav')
yourturn = True

attack = False
current_tour = 0

deathennemy = False
deathallie = False
miss = False

policearial = pygame.font.Font("Pokemon.ttf", 35)
texttour = policearial.render("A vous de jouer.", 1, white)
texttour2 = policearial.render("Tour ennemi.", 1, white)
textdeathallie = policearial.render("Votre pokemon est K.O!", 1, white)
textdeathennemy = policearial.render("Pokemon ennemi est K.O!", 1, white)
textmiss = policearial.render("Pokemon ennemi a esquivé l'attaque!", 1, white)
textcritique = policearial.render("Un coup critique!",1, white)

soundmissed=pygame.mixer.Sound('sound-4.wav')
sound2ndattack=pygame.mixer.Sound('sound-3.wav')
sounddeath=pygame.mixer.Sound('sound-2.wav')
sound=pygame.mixer.Sound('sound.wav')
pygame.mixer_music.load("Musiquecombat.wav")
pygame.mixer.music.play(loops=-1, fade_ms=2)
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


        #si la souris est sur le button1 et clique
        if attack == False and deathallie == False:
            if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
                if click[0] == 1:
                  
                    #defini les couleurs de la barre de vie en fonction de sa taille/valeur
                    attack = True
                    miss = False
                    if barwidth2 > 0:
                        attackValue = random.randint((10/100)*barwidthOG, (20/100)*barwidthOG)
                    
                        if barwidth2 <= int((65/100)*barwidthOG):
                            colorHPbar2 = yellow
                            
                        if barwidth2 <= int((35/100)*barwidthOG):
                            colorHPbar2 = red
                            
                        #si il reste moins de vie que la valeur de l'attaque, on n'attaque de cette valeur restante, le pokemon meurt
                        if attackValue >= barwidth2:
                            attackValue = barwidth2
                            barwidth2 -= attackValue
                            deathennemy = True
                            sounddeath.play()
                            
                        #sinon on attaque avec une valeur aleatoire
                        else:
                            barwidth2 -= attackValue
                            sound.play()
                            if attackValue>=((5/100)*barwidthOG):
                                coupcritique()



       
 
         
         
        if attack == False and deathallie == False:
            if SacButtonX <= mouse[0] <= SacButtonX+widthB and SacButtonY <= mouse[1] <= SacButtonY+heightB:
                if click[0] == 1:          
                    subprocess.run([sys.executable,('Sac.py')])  
                    
                    
         
       
                
                           
                           
                           
                            



        #si la souris est sur le button2 et clique
        if attack == False and deathallie == False:
            if B2buttonX <= mouse[0] <= B2buttonX+widthB and B2buttonY <= mouse[1] <= B2buttonY+heightB:
                if click[0] == 1:
                    precision = random.randint(1, 3)

                    print (precision)
                    #defini les couleurs de la barre de vie en fonction de sa taille/valeur
                    attack = True
                    if precision > 1:
                        miss = False
                        if barwidth2 > 0:
                            attackValue = random.randint((30/100)*barwidthOG, (30/100)*barwidthOG)
                    
                            if barwidth2 <= int((65/100)*barwidthOG):
                                colorHPbar2 = yellow
                            
                            if barwidth2 <= int((35/100)*barwidthOG):
                                colorHPbar2 = red
                            
                            #si il reste moins de vie que la valeur de l'attaque, on n'attaque de cette valeur restante, le pokemon meurt
                            if attackValue >= barwidth2:
                                attackValue = barwidth2
                                barwidth2 -= attackValue
                                deathennemy = True
                                sounddeath.play()
                            
                            #sinon on attaque avec une valeur aleatoire
                            else:
                                sound2ndattack.play()
                                barwidth2 -= attackValue
                               
                            
                    else:
                        miss = True
                        soundmissed.play()
                            
                            
                            
    #on enleve le pokemon du screen lorsqu'il est mort et quitte l'ecran
    if Xennemy >= screenwidth+100:
        all_sprites.remove(pikachu)
        
    if Xallie <= -150:
        all_sprites.remove(feuillosaure)
                            

    
    

    #on appelle les fonctions pour afficher un objet
    
    background1()
    barretexte()
    button1()
    barrevie1()
    barrevie2()
    B2button1()
    BoutonSac1()
    
    
    


    #l'attaque de l'ennemi en retour
    if attack == True and deathennemy == False:
        current_tour += 0.1
        
        if miss == True:
            txtmiss()
        else:
            Tour2()
        
        if current_tour == 1.3 and barwidth > 0:
            attackValue = random.randint((10/100)*barwidthOG, (20/100)*barwidthOG)
            if barwidth <= int((65/100)*barwidthOG):
                colorHPbar = yellow
                            
            if barwidth <= int((35/100)*barwidthOG):
                colorHPbar = red
                
            if attackValue >= barwidth:
                attackValue = barwidth
                barwidth -= attackValue
                deathallie = True
                sounddeath.play()
                
            else:
                barwidth -= attackValue
                sound.play()
            
        if attackValue >= barwidth2:
            attackValue = barwidth2
            
            
        if current_tour >= 3:
            attack = False
    
    elif deathennemy == True:
        txtdeathennemy()
        
    elif deathallie == True:
        txtdeathallie()
        
    else:
        Tour()
        current_tour = 0
    
    




    #appelle class sprite + affiche les sprites
    all_sprites.update()
    all_sprites.draw(screen)




    #si la souris passe sur le button1 alors il change de couleur
    if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
        button1v2()

    #si la souris passe sur le button2 alors il change de couleur
    if B2buttonX <= mouse[0] <= B2buttonX+widthB and B2buttonY <= mouse[1] <= B2buttonY+heightB:
        B2button2()

    if SacButtonX <= mouse[0] <= SacButtonX+widthB and SacButtonY <= mouse[1] <= SacButtonY+heightB:
        BoutonSac2()


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