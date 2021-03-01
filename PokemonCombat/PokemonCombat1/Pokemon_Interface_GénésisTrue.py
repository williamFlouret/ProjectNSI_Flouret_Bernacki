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


Xennemy = (20/100)*screenwidth
Xallie =  (25/100)*screenwidth
attackanimationallie = False
attackanimationennemy = False


#guépardent ennemi animé
class Guépardent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num = 1
        for i in range (1, 62):
            num += 1


            frame = pygame.image.load('3rdPokemon-' + str(num) + '.png')
            frame = pygame.transform.scale(frame, (int((25/100)*screenwidth), int((40/100)*screenheight)))

            self.sprites.append(frame)



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (Xennemy, (25/100)*screenheight)

    def update(self):
        self.current_sprite += 2

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
            Xennemy = (65/100)*screenwidth
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
        self.current_sprite += 0.9

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




class Pokeball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num4 = 1
        for i in range (1, 24):
            num4 += 1


            frame = pygame.image.load('Pokeball-' + str(num4) + '.png')
            frame = pygame.transform.scale(frame, (int((25/100)*screenwidth), int((40/100)*screenheight)))

            self.sprites.append(frame)



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((70/100)*screenwidth, (20/100)*screenheight)

    def update(self):
        updatePokeball =True
        if updatePokeball ==True:
            self.current_sprite += 0.7

        if self.current_sprite >= len(self.sprites):
            updatePokeball = False

        if updatePokeball == True:
            self.image = self.sprites[int(self.current_sprite)]



class PokeballAll(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num6= 1
        for i in range (1, 16):
            num6 += 1


            frame = pygame.image.load('PokeballAll-' + str(num6) + '.png')
            frame = pygame.transform.scale(frame, (int((25/100)*screenwidth), int((40/100)*screenheight)))

            self.sprites.append(frame)



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = ((20/100)*screenwidth, (60/100)*screenheight)

    def update(self):
        updatePokeballAll =True
        if updatePokeballAll ==True:
            self.current_sprite += 0.7

        if self.current_sprite >= len(self.sprites):
            updatePokeballAll = False

        if updatePokeballAll == True:
            self.image = self.sprites[int(self.current_sprite)]

class PokemonOuverture(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num5 = 1
        for i in range (1, 15):
            num5 += 1


            frame = pygame.image.load('3rdPokemonOuverture-' + str(num5) + '.png')
            frame = pygame.transform.scale(frame, (int((25/100)*screenwidth), int((40/100)*screenheight)))

            self.sprites.append(frame)



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (((65/100)*screenwidth, (39/100)*screenheight))


    def update (self):
        updatePokemon =True
        if updatePokemon ==True:
            self.current_sprite += 0.5

        if self.current_sprite >= len(self.sprites):
            updatePokemon = False

        if updatePokemon == True:
            self.image = self.sprites[int(self.current_sprite)]

class PokemonOuvertureAllié(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num7 = 1
        for i in range (1, 12):
            num7 += 1


            frame = pygame.image.load('2ndPokemonOuverture-' + str(num7) + '.png')
            frame = pygame.transform.scale(frame, (int((22/100)*screenwidth), int((43/100)*screenheight)))

            self.sprites.append(frame)



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (((25/100)*screenwidth, (60/100)*screenheight))


    def update (self):
        updatePokemonAllié =True
        if updatePokemonAllié ==True:
            self.current_sprite += 0.5

        if self.current_sprite >= len(self.sprites):
            updatePokemonAllié = False

        if updatePokemonAllié == True:
            self.image = self.sprites[int(self.current_sprite)]







#creation d'un groupe avec tous les pokemons
all_spritesGuépardent = pygame.sprite.Group()
all_spritesPokeballAll = pygame.sprite.Group()
all_spritesFeuillosaure = pygame.sprite.Group()
all_spritesPokemonOuvertureAllié = pygame.sprite.Group()
all_spritesPokemonOuverture = pygame.sprite.Group()
guépardent = Guépardent()
pokeballall =PokeballAll()
feuillosaure = Feuillosaure()
pokeball = Pokeball()
pokemonouvertureallié = PokemonOuvertureAllié()
pokemonouverture = PokemonOuverture()
all_spritesPokemonOuverture.add(pokemonouverture)
all_spritesGuépardent.add(guépardent)
all_spritesFeuillosaure.add(feuillosaure)
all_spritesPokeball = pygame.sprite.Group()
all_spritesPokeball.add(pokeball)
all_spritesPokeballAll.add(pokeballall)
all_spritesPokemonOuvertureAllié.add(pokemonouvertureallié)







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

def Opposant():
    screen.blit(DebutCombat,(DebutCombatX,DebutCombatY))

def RivalSurTerrain():
    screen.blit(Ennemy, (EnnemyX, EnnemyY))

def RivalSurTerrain2():
    screen.blit(Ennemy2, (Ennemy2X, Ennemy2Y))

def Nathan_1():
    screen.blit(Heros1, (Heros1X, Heros1Y))

def Nathan_2():
    screen.blit(Heros2, (Heros2X, Heros2Y))

def Nathan_3():
    screen.blit(Heros3, (Heros3X, Heros3Y))




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

DebutCombat = pygame.image.load('VSKalTrue.png')
DebutCombat = pygame.transform.scale(DebutCombat, (int((80/100)*screenwidth), int((90/100)*screenheight)))
DebutCombatX = (8/100)*screenwidth
DebutCombatY = (15/100)*screenheight

Ennemy2 = pygame.image.load('Kal.png')
Ennemy2 = pygame.transform.scale(Ennemy2, (int((12/100)*screenwidth), int((36/100)*screenheight)))
Ennemy2X = (-15/100)*screenwidth
Ennemy2Y = (20/100)*screenheight

Ennemy = pygame.image.load('Kal2.png')
Ennemy = pygame.transform.scale(Ennemy, (int((12/100)*screenwidth), int((36/100)*screenheight)))
EnnemyX = (-15/100)*screenwidth
EnnemyY = (20/100)*screenheight

Heros1 = pygame.image.load('Nathan1.png')
Heros1 = pygame.transform.scale(Heros1, (int((15/100)*screenwidth), int((45/100)*screenheight)))
Heros1X = (-183/100)*screenwidth
Heros1Y = (55/100)*screenheight

Heros2 = pygame.image.load('Nathan2.png')
Heros2 = pygame.transform.scale(Heros2, (int((15/100)*screenwidth), int((45/100)*screenheight)))
Heros2X = (-183/100)*screenwidth
Heros2Y = (55/100)*screenheight

Heros3 = pygame.image.load('Nathan3.png')
Heros3 = pygame.transform.scale(Heros3, (int((15/100)*screenwidth), int((45/100)*screenheight)))
Heros3X = (-183/100)*screenwidth
Heros3Y = (55/100)*screenheight

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
texttour = policearial.render("À vous de jouer !", 1, white)
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
soundheal=pygame.mixer.Sound('potion.wav')
sacopen=pygame.mixer.Sound('OuvertureSac.wav')
sacclose=pygame.mixer.Sound('FermetureSac.wav')
soundhealennemy=pygame.mixer.Sound('potionennemy.wav')
sounddeath=pygame.mixer.Sound('sound-2.wav')
sound=pygame.mixer.Sound('sound.wav')
pygame.mixer_music.load("RivalFight.wav")
pygame.mixer.music.play(loops=-1, fade_ms=2)



running = True
JeuSac=True
SacOuvert = False
StartFight=False
StartFight2=False
AnimationDebut=True
DresseurMove=True
DresseurMove2=True
ThrowPokeball=False
Dresseur1=True
HerosBouger=False
HerosApparition=True
HerosApparition2=True
HerosApparition3=True
HerosRevenir=False
ThrowPokeBallAll=False


#game loop
while running:

                    #RGB
    #screen.fill((50, 250, 50))

    #on appelle les fonctions pour afficher un objet

    background1()
    if HerosApparition3==True:
        Nathan_3()
    if HerosApparition2==True:
        Nathan_2()
    if HerosApparition==True:
        Nathan_1()
    if Dresseur1 ==True:
        RivalSurTerrain()
    if DresseurMove2 ==True:
        RivalSurTerrain2()
    if AnimationDebut==True:
        Opposant()
    pygame.time.wait(10)
    if StartFight==False:
        DebutCombatY -= 5
    if DebutCombatY <= -500:
        AnimationDebut = False
        
        if DresseurMove==True:
           EnnemyX += 10
           Ennemy2X += 10
           

    if EnnemyX <= 840:
        HerosBouger=True
    
    if HerosBouger==True:
        Heros1X += 10
        Heros2X += 10
        Heros3X += 10

    if HerosRevenir==True:
        Heros3X -=10
        
    

    if EnnemyX>=840:
        DresseurMove=False
        pygame.time.wait(10)
        DresseurMove2=False
        ThrowPokeball=True
        HerosBouger=False
  
        
    if EnnemyX>=1100:
        HerosApparition=False
        

        
    if ThrowPokeball ==True:
        all_spritesPokeball.update()
        all_spritesPokeball.draw(screen)
        DresseurMove =True
        
        

    if ThrowPokeBallAll ==True:
        all_spritesPokeballAll.update()
        all_spritesPokeballAll.draw(screen)
        HerosRevenir =True



    if EnnemyX>=2500:
        Dresseur1=False
        DresseurMove=False
       

    
    if Heros3X==-600:
        HerosApparition3=False
        HerosRevenir=False
       
       

    if  EnnemyX>=1300: 
        HerosApparition2=False
        pygame.time.wait(20)
        ThrowPokeBallAll=True
        

    if EnnemyX>=1000:
        all_spritesGuépardent.update()
        all_spritesGuépardent.draw(screen)
        all_spritesPokemonOuverture.update()
        all_spritesPokemonOuverture.draw(screen)

    if EnnemyX>=1470:
        all_spritesFeuillosaure.update()
        all_spritesFeuillosaure.draw(screen)
        all_spritesPokemonOuvertureAllié.update()
        all_spritesPokemonOuvertureAllié.draw(screen)
       
       
      
        
        
    if EnnemyX>=1600:
        StartFight=True
        StartFight2=True

    if StartFight2==True and StartFight==True:
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
                        sacopen.play()
                        SacOuvert=True
                    else:
                        SacOuvert = False
                        sacclose.play()








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
                            pygame.mixer_music.load("WIN.wav")
                            pygame.mixer.music.play(loops=-1)
                            


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
                                pygame.mixer_music.load("WIN.wav")
                                pygame.mixer.music.play(loops=-1)

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
        all_spritesGuépardent.remove(guépardent)

    if Xallie <= -150:
        all_spritesFeuillosaure.remove(feuillosaure)



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
                    soundheal.play()
                    
                else:
                    barwidth += 30
                    attack = True
                    NbdePV = policearialpv.render(str(barwidth), 1, black)
                    miss = False
                    nbpotion -= 1
                    nbpotiontxt = policearialpt.render(str(nbpotion), 1, white)
                    soundheal.play()



    #l'attaque de l'ennemi en retour
    if attack == True and deathennemy == False:
        current_tour += 1

        healornot = random.randint(1,3)
        whatattack = random.randint(1,3)
        precision = random.randint(1, 3)


        if int(current_tour) == 20 and barwidth2 <= 30 and healornot < 3 and nbpotion2 > 0:
            barwidth2 += 30
            NbdePVEnnemy = policearialpv.render(str(barwidth2), 1, black)
            soundhealennemy.play()
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
                            NbdePV = policearialpv.render(str(barwidth), 1, black)

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
        current_tour = 0
        if StartFight==True:
            Tour()
        



    if SacOuvert==True:
        sac()
        

        NBpotiontxt()

        if potionimgX <= mouse[0] <= potionimgX+widthpotion and potionimgY <= mouse[1] <= potionimgY+heightpotion:
            BoutonPotion2()

        else:
            BoutonPotion1()





    #si la souris passe sur le button1 alors il change de couleur
    if StartFight==True:
        if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
            button1v2()

    #si la souris passe sur le button2 alors il change de couleur

        if B2buttonX <= mouse[0] <= B2buttonX+widthB and B2buttonY <= mouse[1] <= B2buttonY+heightB:
            B2button2()

        if SacButtonX <= mouse[0] <= SacButtonX+widthB and SacButtonY <= mouse[1] <= SacButtonY+heightB:
            BoutonSac2()


    #dessine la barre de vie
    if StartFight==True:
        pygame.draw.rect(screen, colorHPbar, ((barposX, barposY, barwidth , barheight)))
        pygame.draw.rect(screen, colorHPbar2, ((barpos2X, barpos2Y, barwidth2 , barheight2)))


    #rafraichi en continu

    pygame.display.update()
    clock.tick(20)