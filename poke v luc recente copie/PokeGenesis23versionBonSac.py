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
pygame.display.set_caption("Combat Pokemon!")
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
HPbar = pygame.image.load('PVbar.png')
HPbar = pygame.transform.scale(HPbar, (int((33/100)*screenwidth), int((50/100)*screenheight)))
HPbarX = (-4/100)*screenwidth
HPbarY = (-15/100)*screenheight
colorHPbar = green



#barre vie 1
barposX = ((-2.4/100)*screenwidth)+(11/100)*int((33/100)*screenwidth)
barposY = ((13.7/100)*screenheight)+(105/1000)*int((33/100)*screenheight)
barwidth = int((330/1000)*(33/100)*screenwidth)
barheight = int((9.2/100)*(9/100)*screenheight)
barwidthOG = int((330/1000)*(33/100)*screenwidth)


Xennemy = (70/100)*screenwidth
Xallie =  (25/100)*screenwidth
attackanimationallie = False
attackanimationennemy = False


#pikachu ennemi animé
class Pikachu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num = -1
        for i in range (0, 20):
            if num <= 10:
                num += 1

            name = 'tile' + str(num) + '.png'

            frame = pygame.image.load(name)
            frame = pygame.transform.scale(frame, (int((30/100)*screenwidth), int((50/100)*screenheight)))

            self.sprites.append(frame)



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

        if attackanimationennemy and deathallie == False and deathennemy == False:
                Xennemy -= 10
                self.rect.center = (Xennemy, (40/100)*screenheight)

        elif deathallie == False and deathennemy ==  False:
            Xennemy = (70/100)*screenwidth
            self.rect.center = (Xennemy, (40/100)*screenheight)


        self.image = self.sprites[int(self.current_sprite)]



class Feuillosaure(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num2 = 1
        for i in range (1, 60):
            num2 += 1

            name2 = str('2ndPokemon-' + str(num2) + '.png')

            frame2 = pygame.image.load(name2)
            frame2 = pygame.transform.scale(frame2, (int((22/100)*screenwidth), int((43/100)*screenheight)))

            self.sprites.append(frame2)



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((25/100)*screenwidth, (60/100)*screenheight)

    def update(self):
        self.current_sprite += 0.7

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global Xallie
        global attackanimationallie

        if deathallie:
            Xallie -= 10
            self.rect.center = (Xallie, (60/100)*screenheight)

        if attackanimationallie and deathallie == False and deathennemy == False:
                Xallie += 10
                self.rect.center = (Xallie, (60/100)*screenheight)
        elif deathallie == False and deathennemy ==  False:
            Xallie = (25/100)*screenwidth
            self.rect.center = (Xallie, (60/100)*screenheight)




        self.image = self.sprites[int(self.current_sprite)]






#creation d'un groupe avec tous les pokemons
all_sprites = pygame.sprite.Group()
pikachu = Pikachu()
feuillosaure = Feuillosaure()
all_sprites.add(pikachu)
all_sprites.add(feuillosaure)







#Barre de vie pokemon 2
HPbar2 = pygame.image.load('PVbar2.png')
HPbar2 = pygame.transform.scale(HPbar2, (int((33/100)*screenwidth), int((50/100)*screenheight)))
HPbar2X = (68/100)*screenwidth
HPbar2Y = (-20/100)*screenheight
colorHPbar2 = green

#barre vie 2
barpos2X = ((268/100)*int((33/100)*screenwidth))
barpos2Y = ((525/1000)*int((33/100)*screenheight))
barwidth2 = int((330/1000)*(33/100)*screenwidth)
barheight2 = int((9.2/100)*(9/100)*screenheight)
barwidthOG2 = int((330/1000)*(33/100)*screenwidth)





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

def sac():
    screen.blit(sacimg, (sacimgX, sacimgY))

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

def txtmissennemi():
    screen.blit(textmissennemi, (int((22/100)*screenwidth), int((85/100)*screenheight)))

def Vierestante():
    screen.blit(NbdePV, (int((2/100)*screenwidth), int((19/100)*screenheight)))

def Vieentière():
    screen.blit(NbdePVentier, (int((8.5/100)*screenwidth), int((19/100)*screenheight)))

def VierestanteEnnemy():
    screen.blit(NbdePVEnnemy, (int((88.5/100)*screenwidth), int((19/100)*screenheight)))

def VieentièreEnnemy():
    screen.blit(NbdePVEntierEnnemi, (int((95/100)*screenwidth), int((19/100)*screenheight)))

def BoutonPotion1():
    screen.blit(potion1img, (potionimgX, potionimgY))

def BoutonPotion2():
    screen.blit(potion2img, (potionimgX, potionimgY))

def NBpotiontxt():
    screen.blit(nbpotiontxt, (int((845/1000)*screenwidth), int((58/100)*screenheight)))

def NBpotiontxt2():
    screen.blit(nbpotiontxt2, (int((96/100)*screenwidth), int((27/100)*screenheight)))

def BerryImg():
    screen.blit(berryimg, (berryimgX, berryimgY))


#sac
sacimg = pygame.image.load('MenuSac.png')
sacimg = pygame.transform.scale(sacimg, (int((20/100)*screenwidth), int((39.5/100)*screenheight)))
sacimgX = (79/100)*screenwidth
sacimgY = (42/100)*screenheight






#1ebutton1
button1Img = pygame.image.load('2attack.png')
button1Img = pygame.transform.scale(button1Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))
button1X = (2/100)*screenwidth
button1Y = (82.2/100)*screenheight

widthB = int((15/100)*screenwidth)
heightB = int((9.5/100)*screenheight)
click1=0

#1ebutton1v2
button1v2Img = pygame.image.load('2attack2.png')
button1v2Img = pygame.transform.scale(button1v2Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))
button1v2X = (2/100)*screenwidth
button1v2Y = (82.2/100)*screenheight

#2ebutton1
B2button1Img = pygame.image.load('attack.png')
B2button1Img = pygame.transform.scale(B2button1Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))

B2buttonX = (2/100)*screenwidth
B2buttonY = (90.5/100)*screenheight

#2ebutton2
B2button2Img = pygame.image.load('attack2.png')
B2button2Img = pygame.transform.scale(B2button2Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))

#bouton sac
SacButtonImg = pygame.image.load('sac.png')
SacButtonImg = pygame.transform.scale(SacButtonImg, (int((15/100)*screenwidth), int((10/100)*screenheight)))

SacButtonImg2 = pygame.image.load('2sac.png')
SacButtonImg2 = pygame.transform.scale(SacButtonImg2, (int((15/100)*screenwidth), int((10/100)*screenheight)))

SacButtonX = (82.5/100)*screenwidth
SacButtonY = (82/100)*screenheight

#potion dans sac
potionimgX = (80/100)*screenwidth
potionimgY = (50/100)*screenheight
widthpotion = int((5/100)*screenwidth)
heightpotion = int((10/100)*screenheight)

potion1img = pygame.image.load('potion1.png')
potion1img = pygame.transform.scale(potion1img, (widthpotion, heightpotion))

potion2img = pygame.image.load('potion2.png')
potion2img = pygame.transform.scale(potion2img, (widthpotion, heightpotion))

nbpotion = 2
nbpotion2 = 2


berryimgX = (93/100)*screenwidth
berryimgY = (25/100)*screenheight
berryimg = pygame.image.load('berry.png')
berryimg = pygame.transform.scale(berryimg, ((int((7/100)*screenwidth)), (int((6/100)*screenheight))))


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
missennemi = False


policearial = pygame.font.Font("Pokemon.ttf", 35)
policearialpv = pygame.font.Font("Pokemon.ttf", 20)
policearialpt = pygame.font.Font("Pokemon.ttf", 15)
texttour = policearial.render("A vous de jouer.", 1, white)
texttour2 = policearial.render("Tour ennemi.", 1, white)
textdeathallie = policearial.render("Votre pokemon est K.O!", 1, white)
textdeathennemy = policearial.render("Pokemon ennemi est K.O!", 1, white)
textmiss = policearial.render("Pokemon ennemi a esquivé l'attaque!", 1, white)
textcritique = policearial.render("Un coup critique!",1, white)
textmissennemi = policearial.render("Votre pokemon a esquivé l'attaque!", 1, white)
NbdePV = policearialpv.render(str(barwidth), 1, black)
NbdePVentier = policearialpv.render(str(barwidth), 1, black)
NbdePVEnnemy = policearialpv.render(str(barwidth2), 1,black)
NbdePVEntierEnnemi = policearialpv.render(str(barwidth2), 1,black)
nbpotiontxt = policearialpt.render(str(nbpotion), 1, white)
nbpotiontxt2 = policearialpt.render(str(nbpotion2), 1, white)


soundmissed=pygame.mixer.Sound('sound-4.wav')
sound2ndattack=pygame.mixer.Sound('sound-3.wav')
sounddeath=pygame.mixer.Sound('sound-2.wav')
sound=pygame.mixer.Sound('sound.wav')
pygame.mixer_music.load("Musiquecombat.wav")
pygame.mixer.music.play(loops=-1, fade_ms=2)



running = True
JeuSac=True
SacOuvert = False



#game loop
while running:

                    #RGB
    #screen.fill((50, 250, 50))

    #on appelle les fonctions pour afficher un objet

    background1()
    barretexte()
    button1()
    barrevie1()
    barrevie2()
    B2button1()
    BoutonSac1()
    Vierestante()
    Vieentière()
    VierestanteEnnemy()
    VieentièreEnnemy()
    BerryImg()
    NBpotiontxt2()


    #appelle class sprite + affiche les sprites
    all_sprites.update()
    all_sprites.draw(screen)


    #track pointeur
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if attack == False and deathallie == False:
            if SacButtonX <= mouse[0] <= SacButtonX+widthB and SacButtonY <= mouse[1] <= SacButtonY+heightB:
                if click[0] == 1:
                    if SacOuvert == False:
                        SacOuvert=True
                    else:
                        SacOuvert = False








        #si la souris est sur le button1 et clique
        if attack == False and deathallie == False:
            if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
                if click[0] == 1:

                    #defini les couleurs de la barre de vie en fonction de sa taille/valeur
                    attack = True
                    miss = False
                    attackanimationallie = True

                    if barwidth2 > 0:
                        attackValue = random.randint(int((5/100)*barwidthOG), int((8/100)*barwidthOG))

                        if barwidth2 > int((30/100)*barwidthOG):
                            colorHPbar2 = green

                        if barwidth2 <= int((30/100)*barwidthOG):
                            colorHPbar2 = yellow

                        if barwidth2 <= int((18/100)*barwidthOG):
                            colorHPbar2 = red

                        #si il reste moins de vie que la valeur de l'attaque, on n'attaque de cette valeur restante, le pokemon meurt
                        if attackValue >= barwidth2:
                            attackValue = barwidth2
                            barwidth2 -= attackValue
                            deathennemy = True
                            sounddeath.play()
                            NbdePVEnnemy = policearialpv.render(str(barwidth2), 1,black,)

                        #sinon on attaque avec une valeur aleatoire
                        else:
                            barwidth2 -= attackValue
                            sound.play()
                            NbdePVEnnemy = policearialpv.render(str(barwidth2), 1,black,)












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
                        attackanimationallie = True
                        if barwidth2 > 0:
                            attackValue = random.randint(int((15/100)*barwidthOG), int((15/100)*barwidthOG))

                            if barwidth2 > int((30/100)*barwidthOG):
                                colorHPbar2 = green

                            if barwidth2 <= int((30/100)*barwidthOG):
                                colorHPbar2 = yellow

                            if barwidth2 <= int((18/100)*barwidthOG):
                                colorHPbar2 = red

                            #si il reste moins de vie que la valeur de l'attaque, on n'attaque de cette valeur restante, le pokemon meurt
                            if attackValue >= barwidth2:
                                attackValue = barwidth2
                                barwidth2 -= attackValue
                                deathennemy = True
                                sounddeath.play()
                                NbdePVEnnemy = policearialpv.render(str(barwidth2), 1,black,)

                            #sinon on attaque avec une valeur aleatoire
                            else:
                                sound2ndattack.play()
                                barwidth2 -= attackValue
                                NbdePVEnnemy = policearialpv.render(str(barwidth2), 1,black,)



                    else:
                        miss = True
                        attackanimationallie = False
                        soundmissed.play()



    #on enleve le pokemon du screen lorsqu'il est mort et quitte l'ecran
    if Xennemy >= screenwidth+100:
        all_sprites.remove(pikachu)

    if Xallie <= -150:
        all_sprites.remove(feuillosaure)



    #SAC ET POTION
    if SacOuvert == True and attack == False and deathallie == False:
        if potionimgX <= mouse[0] <= potionimgX+widthpotion and potionimgY <= mouse[1] <= potionimgY+heightpotion:

            if attack == False and click[0] == 1 and nbpotion > 0:

                if barwidth + 30 >= barwidthOG:
                    barwidth += barwidthOG - barwidth
                    attack = True
                    NbdePV = policearialpv.render(str(barwidth), 1, black)
                    miss = False
                    nbpotion -=1
                    nbpotiontxt = policearialpt.render(str(nbpotion), 1, white)
                else:
                    barwidth += 30
                    attack = True
                    NbdePV = policearialpv.render(str(barwidth), 1, black)
                    miss = False
                    nbpotion -= 1
                    nbpotiontxt = policearialpt.render(str(nbpotion), 1, white)



    #l'attaque de l'ennemi en retour
    if attack == True and deathennemy == False:
        current_tour += 1

        healornot = random.randint(1,3)
        whatattack = random.randint(1,3)
        precision = random.randint(1, 3)


        if int(current_tour) == 20 and barwidth2 <= 30 and healornot < 3 and nbpotion2 > 0:
            barwidth2 += 30
            NbdePVEnnemy = policearialpv.render(str(barwidth2), 1, black)
            missennemy = False
            nbpotion2 -= 1
            nbpotiontxt2 = policearialpt.render(str(nbpotion2), 1, white)
            attack = False

        else:

            if whatattack > 2:
                if precision > 1:
                    if int(current_tour) == 20 and barwidth > 0:
                        missennemi = False
                        attackanimationennemy = True
                        attackValue = random.randint(int((15/100)*barwidthOG), int((15/100)*barwidthOG))

                        if barwidth > int((50/100)*barwidthOG):
                            colorHPbar = green

                        if barwidth <= int((50/100)*barwidthOG):
                            colorHPbar = yellow

                        if barwidth <= int((18/100)*barwidthOG):
                            colorHPbar = red

                        if attackValue >= barwidth:
                            attackValue = barwidth
                            barwidth -= attackValue
                            deathallie = True
                            sounddeath.play()

                        else:
                            barwidth -= attackValue
                            sound2ndattack.play()
                            NbdePV = policearialpv.render(str(barwidth), 1, black)

                    if attackValue >= barwidth2:
                        attackValue = barwidth2


                    if current_tour >= 40:
                        attack = False

                    if current_tour >= 3:
                        attackanimationallie = False

                elif int(current_tour) == 20:
                    missennemi = True
                    soundmissed.play()

            else:
                if int(current_tour) == 20 and barwidth > 0:
                    missennemi = False
                    attackanimationennemy = True
                    attackValue = random.randint(int((7/100)*barwidthOG), int((9/100)*barwidthOG))

                    if barwidth > int((30/100)*barwidthOG):
                        colorHPbar = green

                    if barwidth <= int((50/100)*barwidthOG):
                        colorHPbar = yellow

                    if barwidth <= int((18/100)*barwidthOG):
                        colorHPbar = red

                    if attackValue >= barwidth:
                        attackValue = barwidth
                        barwidth -= attackValue
                        deathallie = True
                        sounddeath.play()
                        NbdePV = policearialpv.render(str(barwidth), 1, black)

                    else:
                        barwidth -= attackValue
                        sound.play()
                        NbdePV = policearialpv.render(str(barwidth), 1, black)




                if attackValue >= barwidth2:
                    attackValue = barwidth2


                if current_tour >= 40:
                    attack = False

        if miss == True and current_tour <= 20:
            txtmiss()
        if miss == False and current_tour <= 20:
            Tour2()
        if missennemi == True and 20 < current_tour < 40:
            txtmissennemi()

        if current_tour >= 3:
            attackanimationallie = False
        if current_tour >= 23:
            attackanimationennemy = False


    elif deathennemy == True:
        txtdeathennemy()

    elif deathallie == True:
        txtdeathallie()

    else:
        Tour()
        current_tour = 0



    if SacOuvert==True:
        sac()

        NBpotiontxt()

        if potionimgX <= mouse[0] <= potionimgX+widthpotion and potionimgY <= mouse[1] <= potionimgY+heightpotion:
            BoutonPotion2()

        else:
            BoutonPotion1()





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