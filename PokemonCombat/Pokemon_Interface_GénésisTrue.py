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
            self.current_sprite += 0.9

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
            self.current_sprite += 0.9

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
    screen.blit(textmiss, (int((35/100)*screenwidth), int((85/100)*screenheight)))

def coupcritique():
    screen.blit(textcritique, (int((50/100)*screenwidth), int((85/100)*screenheight)))

def txtmissennemi():
    screen.blit(textmissennemi, (int((35/100)*screenwidth), int((85/100)*screenheight)))

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

def BoutonDefense1():
    screen.blit(DefenseButtonImg, (DefenseButtonX, DefenseButtonY))

def BoutonDefense2():
    screen.blit(DefenseButtonImg2, (DefenseButtonX, DefenseButtonY))

def NBabritxt():
    screen.blit(nbabritxt, (int((28/100)*screenwidth), int((87/100)*screenheight)))

def TXTabri():
    screen.blit(txtabri, (int((35/100)*screenwidth), int((86/100)*screenheight)))

def BoutonAttaque1():
    screen.blit(AttackButtonImg, (AttackButtonX, AttackButtonY))

def BoutonAttaque2():
    screen.blit(AttackButtonImg2, (AttackButtonX, AttackButtonY))

def TXTattaquebonus():
    screen.blit(txtattaquebonus, (int((35/100)*screenwidth), int((86/100)*screenheight)))




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
Ennemy2X = (105/100)*screenwidth
Ennemy2Y = (20/100)*screenheight

Ennemy = pygame.image.load('Kal2.png')
Ennemy = pygame.transform.scale(Ennemy, (int((12/100)*screenwidth), int((36/100)*screenheight)))
EnnemyX = (105/100)*screenwidth
EnnemyY = (20/100)*screenheight

Heros1 = pygame.image.load('Nathan1.png')
Heros1 = pygame.transform.scale(Heros1, (int((15/100)*screenwidth), int((45/100)*screenheight)))
Heros1X = (-15/100)*screenwidth
Heros1Y = (55/100)*screenheight

Heros2 = pygame.image.load('Nathan2.png')
Heros2 = pygame.transform.scale(Heros2, (int((15/100)*screenwidth), int((45/100)*screenheight)))
Heros2X = (-15/100)*screenwidth
Heros2Y = (55/100)*screenheight

Heros3 = pygame.image.load('Nathan3.png')
Heros3 = pygame.transform.scale(Heros3, (int((15/100)*screenwidth), int((45/100)*screenheight)))
Heros3X = (-15/100)*screenwidth
Heros3Y = (55/100)*screenheight

#2ebutton1
B2button1Img = pygame.image.load('attack.png')
B2button1Img = pygame.transform.scale(B2button1Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))

B2buttonX = (2/100)*screenwidth
B2buttonY = (90.5/100)*screenheight

#2ebutton2
B2button2Img = pygame.image.load('attack2.png')
B2button2Img = pygame.transform.scale(B2button2Img, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))


#bouton defense
DefenseButtonImg = pygame.image.load('defense.png')
DefenseButtonImg = pygame.transform.scale(DefenseButtonImg, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))

DefenseButtonImg2 = pygame.image.load('defense2.png')
DefenseButtonImg2 = pygame.transform.scale(DefenseButtonImg2, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))

DefenseButtonX = (16/100)*screenwidth
DefenseButtonY = (82/100)*screenheight


#bouton attaque +
AttackButtonImg = pygame.image.load('attaque+.png')
AttackButtonImg = pygame.transform.scale(AttackButtonImg, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))

AttackButtonImg2 = pygame.image.load('attaque+2.png')
AttackButtonImg2 = pygame.transform.scale(AttackButtonImg2, (int((15/100)*screenwidth), int((9.5/100)*screenheight)))

AttackButtonX = (16/100)*screenwidth
AttackButtonY = (90.5/100)*screenheight


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
attackValue2 = random.randint((10/100)*barwidthOG, (30/100)*barwidthOG)


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
abri = False
nbabri = 2
tourabri = 0
attaquebonus = 0
attaqueplus = False


policearial = pygame.font.Font("Pokemon.ttf", 35)
policeariallong = pygame.font.Font("Pokemon.ttf", 25)
policearialpv = pygame.font.Font("Pokemon.ttf", 20)
policearialpt = pygame.font.Font("Pokemon.ttf", 15)
texttour = policearial.render("À vous de jouer !", 1, white)
texttour2 = policearial.render("Tour ennemi.", 1, white)
textdeathallie = policearial.render("Votre pokemon est K.O!", 1, white)
textdeathennemy = policearial.render("Pokemon ennemi est K.O!", 1, white)
textmiss = policeariallong.render("Pokemon ennemi a esquivé l'attaque!", 1, white)
textcritique = policearial.render("Un coup critique!",1, white)
textmissennemi = policeariallong.render("Votre pokemon a esquivé l'attaque!", 1, white)
NbdePV = policearialpv.render(str(barwidth), 1, black)
NbdePVentier = policearialpv.render(str(barwidth), 1, black)
NbdePVEnnemy = policearialpv.render(str(barwidth2), 1,black)
NbdePVEntierEnnemi = policearialpv.render(str(barwidth2), 1,black)
nbpotiontxt = policearialpt.render(str(nbpotion), 1, white)
nbpotiontxt2 = policearialpt.render(str(nbpotion2), 1, white)
nbabritxt = policearialpt.render(str(nbabri), 1, white)
txtabri = policearial.render("Votre pokemon est protegé!", 1, white)
txtattaquebonus = policeariallong.render("L'attaque de votre pokemon augmente!", 1, white)


soundmissed=pygame.mixer.Sound('sound-4.wav')
sound2ndattack=pygame.mixer.Sound('sound-3.wav')
soundheal=pygame.mixer.Sound('potion.wav')
sacopen=pygame.mixer.Sound('OuvertureSac.wav')
sacclose=pygame.mixer.Sound('FermetureSac.wav')
soundhealennemy=pygame.mixer.Sound('potionennemy.wav')
sounddeath=pygame.mixer.Sound('sound-2.wav')
sound=pygame.mixer.Sound('sound.wav')
pygame.mixer_music.load("RivalFight.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1, fade_ms=2)




running = True
JeuSac=True
SacOuvert = False

StartFight=False
AnimationDebut=True
Dresseur1=False
Dresseur2=False
HerosApparition=False
HerosApparition2=False
HerosApparition3=False
KalWait = 0
VSwait = 0
POKE1 = False
NatWait = 0
POKE2 = False


#game loop
while running:


    #on appelle les fonctions pour afficher un objet, ici on lance l'animation de debut de combat

    background1()

    if AnimationDebut == True:
        Opposant()
        VSwait += 1

    if VSwait > 25:
        DebutCombatY -= 20

    if VSwait > 20:
        Dresseur1 = True
        Dresseur2 = True
        HerosApparition = True
        HerosApparition2 = True
        HerosApparition3 = True

    if VSwait > 50:
        AnimationDebut = False
        VSwait = 0

    if Dresseur1 == True:
        RivalSurTerrain()

    if Dresseur2 == True:
        RivalSurTerrain2()
        Ennemy2X -= 10
        EnnemyX -= 10

    if Ennemy2X < 940:
        Dresseur2 = False
        all_spritesPokeball.update()
        all_spritesPokeball.draw(screen)
        KalWait += 1

    if KalWait >= 18:
        POKE1 = True

    if KalWait >= 28:
        EnnemyX += 10
        Ennemy2X += 10
        StartFight = True

    if POKE1:
        all_spritesGuépardent.update()
        all_spritesGuépardent.draw(screen)
        all_spritesPokemonOuverture.update()
        all_spritesPokemonOuverture.draw(screen)

    if Ennemy2X > 1350:
        Dresseur1 = False
        KalWait = 0

    if HerosApparition2==True:
        Nathan_3()
    if HerosApparition==True:
        Nathan_1()
        Heros1X += 5
        Heros2X += 5
        Heros3X += 5

    if Heros1X >= 0:
        HerosApparition = False
        all_spritesPokeballAll.update()
        all_spritesPokeballAll.draw(screen)
        NatWait += 1

    if NatWait >= 12:
        Heros1X -= 5
        Heros2X -= 5
        Heros3X -= 5
        POKE2 = True

    if Heros3X < -200:
        HerosApparition2 = False
        NatWait = 0

    if POKE2 == True:
        all_spritesFeuillosaure.update()
        all_spritesFeuillosaure.draw(screen)
        all_spritesPokemonOuvertureAllié.update()
        all_spritesPokemonOuvertureAllié.draw(screen)


    if StartFight==True:
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
        BoutonDefense1()
        BoutonAttaque1()



    #track pointeur
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if attack == False and deathallie == False and StartFight==True:
            if SacButtonX <= mouse[0] <= SacButtonX+widthB and SacButtonY <= mouse[1] <= SacButtonY+heightB:
                if click[0] == 1:
                    if SacOuvert == False:
                        sacopen.play()
                        SacOuvert=True
                    else:
                        SacOuvert = False
                        sacclose.play()








        #si la souris est sur le button1 et clique
        if attack == False and deathallie == False and StartFight==True:
            if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
                if click[0] == 1:

                    tourabri -= 1
                    if tourabri <= 0:
                        abri = False

                    #defini les couleurs de la barre de vie en fonction de sa taille/valeur
                    attack = True
                    miss = False
                    attackanimationallie = True

                    if barwidth2 > 0:

                        attackValue = random.randint(int((5/100)*barwidthOG), int((8/100)*barwidthOG))
                        attackValue += attaquebonus

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
        if attack == False and deathallie == False and StartFight==True:
            if B2buttonX <= mouse[0] <= B2buttonX+widthB and B2buttonY <= mouse[1] <= B2buttonY+heightB:
                if click[0] == 1:
                    precision = random.randint(1, 3)

                    tourabri -= 1
                    if tourabri <= 0:
                        abri = False


                    #defini les couleurs de la barre de vie en fonction de sa taille/valeur
                    attack = True
                    if precision > 1:
                        miss = False
                        attackanimationallie = True
                        if barwidth2 > 0:

                            attackValue = random.randint(int((15/100)*barwidthOG), int((15/100)*barwidthOG))
                            attackValue += attaquebonus

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


        #si la souris clique sur defense alors le pokemon se defend
        if attack == False and deathallie == False and nbabri > 0 and tourabri <= 0 and StartFight==True:
            if DefenseButtonX <= mouse[0] <= DefenseButtonX + int((15/100)*screenwidth) and DefenseButtonY <= mouse[1] <= DefenseButtonY + int((10/100)*screenheight):
                if click[0] == 1:

                    attack = True
                    miss = False
                    abri = True
                    nbabri -= 1
                    tourabri = 1
                    nbabritxt = policearialpt.render(str(nbabri), 1, white)
                    print ('tourabri' + str(tourabri))
                    print ('abri' + str(abri))



        #2si on clique sur le bouton attaque + l'attaque du pokemon augmente
        if attack == False and deathallie == False and StartFight==True:
            if AttackButtonX <= mouse[0] <= AttackButtonX + int((15/100)*screenwidth) and AttackButtonY <= mouse[1] <= AttackButtonY + int((10/100)*screenheight):
                if click[0] == 1:

                    attack = True
                    miss = False
                    attaquebonus += 3
                    attaqueplus = True






    #on enleve le pokemon du screen lorsqu'il est mort et quitte l'ecran
    if Xennemy >= screenwidth+100:
        all_spritesGuépardent.remove(guépardent)

    if Xallie <= -150:
        all_spritesFeuillosaure.remove(feuillosaure)



    #SAC ET POTION
    if SacOuvert == True and attack == False and deathallie == False and StartFight==True:
        if potionimgX <= mouse[0] <= potionimgX+widthpotion and potionimgY <= mouse[1] <= potionimgY+heightpotion:

            if attack == False and click[0] == 1 and nbpotion > 0:

                if barwidth + 35 >= barwidthOG:
                    barwidth += barwidthOG - barwidth
                    attack = True
                    NbdePV = policearialpv.render(str(barwidth), 1, black)
                    miss = False
                    nbpotion -=1
                    nbpotiontxt = policearialpt.render(str(nbpotion), 1, white)
                    soundheal.play()

                else:
                    barwidth += 35
                    attack = True
                    NbdePV = policearialpv.render(str(barwidth), 1, black)
                    miss = False
                    nbpotion -= 1
                    nbpotiontxt = policearialpt.render(str(nbpotion), 1, white)
                    soundheal.play()



    #l'attaque de l'ennemi en retour
    if attack == True and deathennemy == False and StartFight==True:
        current_tour += 1

        healornot = random.randint(1,3)
        whatattack = random.randint(1,3)
        precision = random.randint(1, 3)


        if int(current_tour) == 20 and barwidth2 <= 40 and healornot < 3 and nbpotion2 > 0:
            barwidth2 += 40
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
                        attackValue2 = random.randint(int((16/100)*barwidthOG), int((16/100)*barwidthOG))

                        if abri == True:
                            attackValue2 = 0

                        if barwidth > int((50/100)*barwidthOG):
                            colorHPbar = green

                        if barwidth <= int((50/100)*barwidthOG):
                            colorHPbar = yellow

                        if barwidth <= int((18/100)*barwidthOG):
                            colorHPbar = red

                        if attackValue2 >= barwidth:
                            attackValue2 = barwidth
                            barwidth -= attackValue2
                            deathallie = True
                            sounddeath.play()
                            NbdePV = policearialpv.render(str(barwidth), 1, black)

                        else:
                            barwidth -= attackValue2
                            sound2ndattack.play()
                            NbdePV = policearialpv.render(str(barwidth), 1, black)

                    if attackValue2 >= barwidth2:
                        attackValue2 = barwidth2


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
                    attackValue2 = random.randint(int((8/100)*barwidthOG), int((9/100)*barwidthOG))

                    if abri == True:
                        attackValue2 = 0

                    if barwidth > int((30/100)*barwidthOG):
                        colorHPbar = green

                    if barwidth <= int((50/100)*barwidthOG):
                        colorHPbar = yellow

                    if barwidth <= int((18/100)*barwidthOG):
                        colorHPbar = red

                    if attackValue2 >= barwidth:
                        attackValue2 = barwidth
                        barwidth -= attackValue2
                        deathallie = True
                        sounddeath.play()
                        NbdePV = policearialpv.render(str(barwidth), 1, black)

                    else:
                        barwidth -= attackValue2
                        sound.play()
                        NbdePV = policearialpv.render(str(barwidth), 1, black)




                if attackValue2 >= barwidth2:
                    attackValue2 = barwidth2


                if current_tour >= 40:
                    attack = False


        if missennemi == False and 20 < current_tour < 40 and abri == True:
            TXTabri()

        if miss == True and current_tour <= 20:
            txtmiss()
        if miss == False and current_tour <= 20 and attaqueplus == False:
            Tour2()
        elif attaqueplus == True and miss == False and current_tour <= 20:
            TXTattaquebonus()

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
            attaqueplus = False




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

        #si la souris passe sur le bouton attaque alors il change de couleur
        if AttackButtonX <= mouse[0] <= AttackButtonX + int((15/100)*screenwidth) and AttackButtonY <= mouse[1] <= AttackButtonY + int((10/100)*screenheight):
            BoutonAttaque2()

        #si la souris passe sur le bouton defense alors il change de couleur
        if DefenseButtonX <= mouse[0] <= DefenseButtonX + int((15/100)*screenwidth) and DefenseButtonY <= mouse[1] <= DefenseButtonY + int((10/100)*screenheight):
            BoutonDefense2()
        #affiche le nombre d'abri restant
        NBabritxt()


    #dessine la barre de vie
    if StartFight==True:
        pygame.draw.rect(screen, colorHPbar, ((barposX, barposY, barwidth , barheight)))
        pygame.draw.rect(screen, colorHPbar2, ((barpos2X, barpos2Y, barwidth2 , barheight2)))


    #rafraichi en continu

    pygame.display.update()
    clock.tick(20)