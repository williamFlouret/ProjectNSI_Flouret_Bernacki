import pygame, sys, subprocess, random


pygame.init()               #importation de tous les modules
clock = pygame.time.Clock()
import pygame.mixer
import pygame.mixer_music
pygame.mixer.init()
#screen width and height
screenwidth = 1200  #Choose your screen size
screenheight = int((610/1000)*screenwidth)





#create screen
screen = pygame.display.set_mode((screenwidth, screenheight))



#title and icon
pygame.display.set_caption("POKEMON GENESIS")
icon = pygame.image.load('Pokeball.png')
pygame.display.set_icon(icon)


#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


#musicplay (boolenes qui gerent quelle musique jouer, combat ou map)
musicplaycombat = False
musicplaymap = True


############################################################################################## Interface Combat

#on importe les premieres images que l'on a implementé au jeu
#background image
backgroundImg = pygame.image.load('forest.png')
backgroundImg = pygame.transform.scale(backgroundImg, (screenwidth, screenheight))
backgroundX = 0
backgroundY = 0

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



#barre vie 1 (on lui defini une taille en fonction de la taille de l'ecran)
barposX = ((-2.4/100)*screenwidth)+(11/100)*int((33/100)*screenwidth)
barposY = ((13.7/100)*screenheight)+(105/1000)*int((33/100)*screenheight)
barwidth = int((330/1000)*(33/100)*screenwidth)
barheight = int((11/1000)*screenheight)
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
        for i in range (1, 62):        #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
            num += 1


            frame = pygame.image.load('3rdPokemon-' + str(num) + '.png')
            frame = pygame.transform.scale(frame, (int((25/100)*screenwidth), int((40/100)*screenheight)))

            self.sprites.append(frame)



        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (Xennemy, (25/100)*screenheight)

    def update(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global Xennemy

        if deathennemy:     #quand ce pokemon meurt, il se deplace vers la droite pour disparaitre
            Xennemy += 6
            self.rect.center = (Xennemy, (40/100)*screenheight)

        if attackanimationennemy and deathallie == False and deathennemy == False:  #la petite animation lorsque le pokemon attaque (un petit coup vers la gauche)
                Xennemy -= 4
                self.rect.center = (Xennemy, (40/100)*screenheight)

        elif deathallie == False and deathennemy ==  False:
            Xennemy = (65/100)*screenwidth
            self.rect.center = (Xennemy, (40/100)*screenheight)


        self.image = self.sprites[int(self.current_sprite)]


#classe du pokemon allié Feuillosaure
class Feuillosaure(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num2 = 1
        for i in range (1, 60):     #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
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
        self.current_sprite += 0.36

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        global Xallie
        global attackanimationallie

        if deathallie:   #pareil que pour geupardent, il sort de l'ecran quand il meurt
            Xallie -= 6
            self.rect.center = (Xallie, (60/100)*screenheight)

        if attackanimationallie and deathallie == False and deathennemy == False:
                Xallie += 4
                self.rect.center = (Xallie, (60/100)*screenheight)
        elif deathallie == False and deathennemy ==  False:
            Xallie = (25/100)*screenwidth
            self.rect.center = (Xallie, (60/100)*screenheight)




        self.image = self.sprites[int(self.current_sprite)]



#classe de l'animation de la pokeball alliée en debut de combat
class Pokeball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num4 = 1
        for i in range (1, 24):     #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
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
            self.current_sprite += 0.28

        if self.current_sprite >= len(self.sprites):
            updatePokeball = False

        if updatePokeball == True:
            self.image = self.sprites[int(self.current_sprite)]


#classe de la pokeball ennemie
class PokeballAll(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num6= 1
        for i in range (1, 16):     #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
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
            self.current_sprite += 0.28

        if self.current_sprite >= len(self.sprites):
            updatePokeballAll = False

        if updatePokeballAll == True:
            self.image = self.sprites[int(self.current_sprite)]


#classe de l'animation d'ouverture de pokemon (lorsqu'il sort de pokeball et qu'il est blanc
class PokemonOuverture(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num5 = 1
        for i in range (1, 15):     #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
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
            self.current_sprite += 0.36

        if self.current_sprite >= len(self.sprites):
            updatePokemon = False

        if updatePokemon == True:
            self.image = self.sprites[int(self.current_sprite)]


#de meme, avec le pokemon allié
class PokemonOuvertureAllié(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []


        num7 = 1
        for i in range (1, 12):     #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
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
            self.current_sprite += 0.36

        if self.current_sprite >= len(self.sprites):
            updatePokemonAllié = False

        if updatePokemonAllié == True:
            self.image = self.sprites[int(self.current_sprite)]







#creation de groupes avec tous les pokemons et animations
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
barheight2 = int((11/1000)*screenheight)
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

def background():
    screen.blit(backgroundImg, (backgroundX, backgroundY))

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


#on continue d'importer des images pour le jeu avec leur coordonnées et tailles

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


nbpotion = 2  #nombre de potions que peut utiliser le joueur et l'adversaire
nbpotion2 = 2


berryimgX = (93/100)*screenwidth
berryimgY = (25/100)*screenheight
berryimg = pygame.image.load('berry.png')
berryimg = pygame.transform.scale(berryimg, ((int((7/100)*screenwidth)), (int((6/100)*screenheight))))


attackValue = random.randint((10/100)*barwidthOG, (30/100)*barwidthOG)  #valeur de l'attaque allié
attackValue2 = random.randint((10/100)*barwidthOG, (30/100)*barwidthOG)  #valeur de l'attaque de l'ennemi


precision = random.randint(1, 3)  #precision aléatoire

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

#toutes les polices et textes du jeu importées et definies ici
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

#son et musiques du jeu
soundmissed=pygame.mixer.Sound('sound-4.wav')
sound2ndattack=pygame.mixer.Sound('sound-3.wav')
soundheal=pygame.mixer.Sound('potion.wav')
sacopen=pygame.mixer.Sound('OuvertureSac.wav')
sacclose=pygame.mixer.Sound('FermetureSac.wav')
soundhealennemy=pygame.mixer.Sound('potionennemy.wav')
sounddeath=pygame.mixer.Sound('sound-2.wav')
sound=pygame.mixer.Sound('sound.wav')




#quelques booleens qui gerent certains aspects du jeu

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



##############################################################################################
############################################################################################## Interface Combat

############################################################################################## Map Pokemon
##############################################################################################







global vitesse
vitesse = 5  #vitesse de base du personnage de 5px par deplacement

#creation du dictionnaire qui contient toutes les collisions de la map, oui il y en a beaucoup et ce fut laborieux...

obstacles = {"house1": [675-vitesse, 820+vitesse, 254-vitesse, 385+vitesse], "house2": [930-vitesse, screenwidth, 75-vitesse, 246+vitesse], "bushligne": [855-vitesse, screenwidth-vitesse-10, 30-vitesse, 155+vitesse], "barriere1": [855-vitesse, 880+vitesse, 160-vitesse, 368+vitesse], "barriere2": [855-vitesse, 1025+vitesse, 345-vitesse, 374+vitesse], "barriere3": [1075-vitesse, screenwidth, 345-vitesse, 374+vitesse], "barriere4": [0, 40+vitesse, 31-vitesse, 360+vitesse], "house3": [1100-vitesse, screenwidth, 475-vitesse, 595+vitesse], "house3bis": [0, 36+vitesse, 475-vitesse, 595+vitesse], "house4": [190-vitesse, 338+vitesse, 134-vitesse, 262+vitesse], "house5": [858-vitesse, 1035+vitesse, 352-vitesse, 460+vitesse], "house5bis": [930-vitesse, 1035+vitesse, 352-vitesse, 490+vitesse], "marketbis": [140-vitesse, 268+vitesse, 0, 7+vitesse], "3bush1": [436-vitesse, 524+vitesse, 37-vitesse, 101+vitesse], "3bush2": [436-vitesse, 524+vitesse, 309-vitesse, 373+vitesse], "3bush3": [436-vitesse, 524+vitesse, 633-vitesse, 693+vitesse], "3bush4": [196-vitesse, 284+vitesse, 145-vitesse, 209+vitesse], "3bush5": [196-vitesse, 284+vitesse, 417-vitesse, 481+vitesse], "3bush6": [196-vitesse, 284+vitesse, 685-vitesse, screenheight], "Hautarbrepart2":[0, 78+vitesse, 272-vitesse, 404+vitesse], "Droitearbrepart2":[0, 110+vitesse, 288-vitesse, 372+vitesse], "barriere1part2":[0, 518+vitesse, 332-vitesse, 352+vitesse], "barriere2part2":[478-vitesse, 518+vitesse, 332-vitesse, 504+vitesse], "barriere3part2":[458-vitesse, 518+vitesse, 468-vitesse, 504+vitesse], "barriere4part2":[0, 386+vitesse, 468-vitesse, 504+vitesse], "arbre1part2":[126-vitesse, 278+vitesse, 600-vitesse, screenheight], "arbre2part2":[906-vitesse, 1066+vitesse, 380-vitesse, 528+vitesse], "arbre1part1":[186-vitesse, 294+vitesse, 0, 144+vitesse], "house1.1part1":[786-vitesse, 990+vitesse, 0, 176+vitesse], "house1.2part1":[862-vitesse, 990+vitesse, 0, 204+vitesse], "arbre2part1":[426-vitesse, 534+vitesse, 220-vitesse, 300+vitesse], "arbre3part1":[186-vitesse, 294+vitesse, 328-vitesse, 408+vitesse], "arbre4part1":[426-vitesse, 534+vitesse, 488-vitesse, 563+vitesse], "arbre5part1":[186-vitesse, 294+vitesse, 600-vitesse, 680+vitesse], "Centrepokemon":[598-vitesse, 778+vitesse, 524-vitesse, 680+vitesse], "Hautarbrepart1":[1158-vitesse, screenwidth, 272-vitesse, 404+vitesse], "barriere1part1":[1106-vitesse, screenwidth, 332-vitesse, 352+vitesse], "barriere2part1":[1106-vitesse, 1142+vitesse, 332-vitesse, 504+vitesse], "barriere3part1":[1106-vitesse, screenwidth, 468-vitesse, 504+vitesse], "arbre1part5":[196-vitesse, 294+vitesse, 0, 64+vitesse], "arbre2part5":[426-vitesse, 534+vitesse, 0, 20+vitesse], "GrandArbreHautpart5":[132-vitesse, 294+vitesse, 448-vitesse, 560+vitesse], "GrandArbreTroncpart5":[166-vitesse, 250+vitesse, 448-vitesse, 632+vitesse], "arbre3part5":[850-vitesse, 946+vitesse, 480-vitesse, 556+vitesse], "arbre4part5":[1034-vitesse, 1130+vitesse, 372-vitesse, 448+vitesse], "arbre1part6":[18-vitesse, 106+vitesse, 480-vitesse, 556+vitesse], "arbre2part6":[194-vitesse, 280+vitesse, 372-vitesse, 448+vitesse], "arbre3part6":[378-vitesse, 466+vitesse, 480-vitesse, 556+vitesse], "arbre4part6":[554-vitesse, 646+vitesse, 372-vitesse, 448+vitesse], "arbre5part6":[734-vitesse, 830+vitesse, 480-vitesse, 556+vitesse]}

XNat=450   #gere la taille du personnage, qui peut varier
YNat=650
WidthNatH = int((3/100)*screenwidth)
HeightNatH = int((6/100)*screenheight)
WidthNatB = int((3/100)*screenwidth)
HeightNatB = int((6/100)*screenheight)
WidthNatD = int((3/100)*screenwidth)
HeightNatD = int((6/100)*screenheight)
WidthNatG = int((3/100)*screenwidth)
HeightNatG = int((6/100)*screenheight)

spriteplus = 0.2
currentSprite = 0

class NATHANOVERH(pygame.sprite.Sprite):    #classe qui gere l'animation et le deplacement du personnage lorsqu'il va vers le haut
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        global WidthNatH
        global HeightNatH

        for j in range (2):
            num26 = 0
            for i in range (1, 5):          #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
                num26 += 1

                name26 = str('HerosOverworldHaut-' + str(num26) + '.png')

                frame26 = pygame.image.load(name26)
                frame26 = pygame.transform.scale(frame26, (WidthNatH, HeightNatH))

                self.sprites.append(frame26)

            WidthNatH = (int((3/100)*screenwidth))+30
            HeightNatH = (int((6/100)*screenheight))+40

        global currentSprite
        self.current_sprite = currentSprite
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)




    def update(self):

        global LAB    #si on se trouve dans le labo, on passe a une autre partie des images de l'animation, cette fois plus grandes, le personnage parait donc zoomé
        if LAB:
            if self.current_sprite < 4:
                self.current_sprite = 4
            self.current_sprite += spriteplus
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 4
        else:
            self.current_sprite += spriteplus

            if self.current_sprite >= (len(self.sprites)-4):
                self.current_sprite = 0


        global XNat
        global YNat
        global Statik



        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:       #en fonction de la partie de map, la classe va verifier si le joueur n'est pas dans une zone d'obstacle, alors il peut avancer ou pas... c'est un peu bourrin vu le nombre d'obstacles differents mais c'est la seule solution que nous avons trouvé
            if MapPart1 == True :
                if (YNat > vitesse + 100) and (not((obstacles["arbre1part1"][0] < XNat < obstacles["arbre1part1"][1]) and (obstacles["arbre1part1"][2] < YNat < obstacles["arbre1part1"][3]+9))) and (not((obstacles["house1.1part1"][0] < XNat < obstacles["house1.1part1"][1]) and (obstacles["house1.1part1"][2] < YNat < obstacles["house1.1part1"][3]+9))) and (not((obstacles["house1.2part1"][0] < XNat < obstacles["house1.2part1"][1]) and (obstacles["house1.2part1"][2] < YNat < obstacles["house1.2part1"][3]+9))) and (not((obstacles["arbre2part1"][0] < XNat < obstacles["arbre2part1"][1]) and (obstacles["arbre2part1"][2] < YNat < obstacles["arbre2part1"][3]+9))) and (not((obstacles["arbre3part1"][0] < XNat < obstacles["arbre3part1"][1]) and (obstacles["arbre3part1"][2] < YNat < obstacles["arbre3part1"][3]+9))) and (not((obstacles["arbre4part1"][0] < XNat < obstacles["arbre4part1"][1]) and (obstacles["arbre4part1"][2] < YNat < obstacles["arbre4part1"][3]+9))) and (not((obstacles["arbre5part1"][0] < XNat < obstacles["arbre5part1"][1]) and (obstacles["arbre5part1"][2] < YNat < obstacles["arbre5part1"][3]+9))) and (not((obstacles["Centrepokemon"][0] < XNat < obstacles["Centrepokemon"][1]) and (obstacles["Centrepokemon"][2] < YNat < obstacles["Centrepokemon"][3]+9))) and (not((obstacles["Hautarbrepart1"][0] < XNat < obstacles["Hautarbrepart1"][1]) and (obstacles["Hautarbrepart1"][2] < YNat < obstacles["Hautarbrepart1"][3]+9))) and (not((obstacles["barriere1part1"][0] < XNat < obstacles["barriere1part1"][1]) and (obstacles["barriere1part1"][2] < YNat < obstacles["barriere1part1"][3]+9))) and (not((obstacles["barriere2part1"][0] < XNat < obstacles["barriere2part1"][1]) and (obstacles["barriere2part1"][2] < YNat < obstacles["barriere2part1"][3]+9))) and (not((obstacles["barriere3part1"][0] < XNat < obstacles["barriere3part1"][1]) and (obstacles["barriere3part1"][2] < YNat < obstacles["barriere3part1"][3]+9))):
                     YNat -= vitesse

            elif MapPart2 == True:
                if (YNat > vitesse + 100) and (not((obstacles["Hautarbrepart2"][0] < XNat < obstacles["Hautarbrepart2"][1]) and (obstacles["Hautarbrepart2"][2] < YNat < obstacles["Hautarbrepart2"][3]+10))) and (not((obstacles["Droitearbrepart2"][0] < XNat < obstacles["Droitearbrepart2"][1]) and (obstacles["Droitearbrepart2"][2] < YNat < obstacles["Droitearbrepart2"][3]+10))) and (not((obstacles["barriere1part2"][0] < XNat < obstacles["barriere1part2"][1]) and (obstacles["barriere1part2"][2] < YNat < obstacles["barriere1part2"][3]+10))) and (not((obstacles["barriere2part2"][0] < XNat < obstacles["barriere2part2"][1]) and (obstacles["barriere2part2"][2] < YNat < obstacles["barriere2part2"][3]+10))) and (not((obstacles["barriere3part2"][0] < XNat < obstacles["barriere3part2"][1]) and (obstacles["barriere3part2"][2] < YNat < obstacles["barriere3part2"][3]+10))) and (not((obstacles["barriere4part2"][0] < XNat < obstacles["barriere4part2"][1]) and (obstacles["barriere4part2"][2] < YNat < obstacles["barriere4part2"][3]+10))) and (not((obstacles["arbre1part2"][0] < XNat < obstacles["arbre1part2"][1]) and (obstacles["arbre1part2"][2] < YNat < obstacles["arbre1part2"][3]+9))) and (not((obstacles["arbre2part2"][0] < XNat < obstacles["arbre2part2"][1]) and (obstacles["arbre2part2"][2] < YNat < obstacles["arbre2part2"][3]+9))):
                    YNat -= vitesse


            elif MapPart3 == True:
                if (not((obstacles["house1"][0] < XNat < obstacles["house1"][1]) and (obstacles["house1"][2] < YNat < obstacles["house1"][3]+10))) and (not((obstacles["house2"][0] < XNat < obstacles["house2"][1]) and (obstacles["house2"][2] < YNat < obstacles["house2"][3]+9))) and (not((obstacles["bushligne"][0] < XNat < obstacles["bushligne"][1]) and (obstacles["bushligne"][2] < YNat < obstacles["bushligne"][3]+9))) and (not((obstacles["barriere1"][0] < XNat < obstacles["barriere1"][1]) and (obstacles["barriere1"][2] < YNat < obstacles["barriere1"][3]+6))) and (not((obstacles["barriere2"][0] < XNat < obstacles["barriere2"][1]) and (obstacles["barriere2"][2] < YNat < obstacles["barriere2"][3]+9))) and (not((obstacles["barriere3"][0] < XNat < obstacles["barriere3"][1]) and (obstacles["barriere3"][2] < YNat < obstacles["barriere3"][3]+9))) and (not((obstacles["house3"][0] < XNat < obstacles["house3"][1]) and (obstacles["house3"][2] < YNat < obstacles["house3"][3]+10))) and (not((obstacles["3bush1"][0] < XNat < obstacles["3bush1"][1]) and (obstacles["3bush1"][2] < YNat < obstacles["3bush1"][3]+10))) and (not((obstacles["3bush2"][0] < XNat < obstacles["3bush2"][1]) and (obstacles["3bush2"][2] < YNat < obstacles["3bush2"][3]+10))) and (not((obstacles["3bush3"][0] < XNat < obstacles["3bush3"][1]) and (obstacles["3bush3"][2] < YNat < obstacles["3bush3"][3]+10))) and (not((obstacles["3bush4"][0] < XNat < obstacles["3bush4"][1]) and (obstacles["3bush4"][2] < YNat < obstacles["3bush4"][3]+10))) and (not((obstacles["3bush5"][0] < XNat < obstacles["3bush5"][1]) and (obstacles["3bush5"][2] < YNat < obstacles["3bush5"][3]+10))) and (not((obstacles["3bush6"][0] < XNat < obstacles["3bush6"][1]) and (obstacles["3bush6"][2] < YNat < obstacles["3bush6"][3]+10))):
                    YNat -= vitesse

            elif MapPart4 == True:
                if not((obstacles["barriere4"][0] < XNat < obstacles["barriere4"][1]) and (obstacles["barriere4"][2] < YNat < obstacles["barriere4"][3]+10)) and (not((obstacles["house3bis"][0] < XNat < obstacles["house3bis"][1]) and (obstacles["house3bis"][2] < YNat < obstacles["house3bis"][3]+10))) and (not((obstacles["house4"][0] < XNat < obstacles["house4"][1]) and (obstacles["house4"][2] < YNat < obstacles["house4"][3]+10))) and (not((obstacles["house5"][0] < XNat < obstacles["house5"][1]) and (obstacles["house5"][2] < YNat < obstacles["house5"][3]+10))) and (not((obstacles["house5bis"][0] < XNat < obstacles["house5bis"][1]) and (obstacles["house5"][2] < YNat < obstacles["house5bis"][3]+10)))and (not((obstacles["marketbis"][0] < XNat < obstacles["marketbis"][1]) and (obstacles["marketbis"][2] < YNat < obstacles["marketbis"][3]+10))):
                    YNat -= vitesse

            elif MapPart5 == True:
                if (not((obstacles["arbre1part5"][0] < XNat < obstacles["arbre1part5"][1]) and (obstacles["arbre1part5"][2] < YNat < obstacles["arbre1part5"][3]+10))) and (not((obstacles["arbre2part5"][0] < XNat < obstacles["arbre2part5"][1]) and (obstacles["arbre2part5"][2] < YNat < obstacles["arbre2part5"][3]+9))) and (not((obstacles["GrandArbreHautpart5"][0] < XNat < obstacles["GrandArbreHautpart5"][1]) and (obstacles["GrandArbreHautpart5"][2] < YNat < obstacles["GrandArbreHautpart5"][3]+9))) and (not((obstacles["GrandArbreTroncpart5"][0] < XNat < obstacles["GrandArbreTroncpart5"][1]) and (obstacles["GrandArbreTroncpart5"][2] < YNat < obstacles["GrandArbreTroncpart5"][3]+10))) and (not((obstacles["arbre3part5"][0] < XNat < obstacles["arbre3part5"][1]) and (obstacles["arbre3part5"][2] < YNat < obstacles["arbre3part5"][3]+9))) and (not((obstacles["arbre4part5"][0] < XNat < obstacles["arbre4part5"][1]) and (obstacles["arbre4part5"][2] < YNat < obstacles["arbre4part5"][3]+9))):
                    YNat -= vitesse

            elif MapPart6 == True:
                if (not((obstacles["arbre1part6"][0] < XNat < obstacles["arbre1part6"][1]) and (obstacles["arbre1part6"][2] < YNat < obstacles["arbre1part6"][3]+9))) and (not((obstacles["arbre2part6"][0] < XNat < obstacles["arbre2part6"][1]) and (obstacles["arbre2part6"][2] < YNat < obstacles["arbre2part6"][3]+9))) and (not((obstacles["arbre3part6"][0] < XNat < obstacles["arbre3part6"][1]) and (obstacles["arbre3part6"][2] < YNat < obstacles["arbre3part6"][3]+10))) and (not((obstacles["arbre4part6"][0] < XNat < obstacles["arbre4part6"][1]) and (obstacles["arbre4part6"][2] < YNat < obstacles["arbre4part6"][3]+9))) and (not((obstacles["arbre5part6"][0] < XNat < obstacles["arbre5part6"][1]) and (obstacles["arbre5part6"][2] < YNat < obstacles["arbre5part6"][3]+9))):
                    YNat -= vitesse

            elif LAB:
                if screenwidth-vitesse-20 > XNat > 15+vitesse and YNat > 357 and not((0<XNat<485) and (screenheight-40-vitesse<YNat<screenheight)) and not((690-vitesse<XNat<screenwidth) and (screenheight-40-vitesse < YNat < screenheight)) and not((0<XNat<284+vitesse) and (438-vitesse < YNat < 632+vitesse)) and not((900-vitesse<XNat<screenwidth) and (0 < YNat < 532+vitesse)) and not((110-vitesse<XNat<200+vitesse) and (350 < YNat < 410+vitesse)):
                    YNat-= vitesse

            else:
                YNat-= vitesse



            self.rect.center = (XNat, YNat)
        if Statik:      #quand le personnage n'avance pas, les images ne defilent pas
            if LAB:
                self.current_sprite = 4
            else:
                self.current_sprite = 0


        self.image = self.sprites[int(self.current_sprite)]


class NATHANOVERB(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        global WidthNatB
        global HeightNatB

        for j in range (2):         #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
            num27 = 0
            for i in range (1, 5):
                num27 += 1

                name27 = str('HerosOverworldBas-' + str(num27) + '.png')

                frame27 = pygame.image.load(name27)
                frame27 = pygame.transform.scale(frame27,( WidthNatB, HeightNatB))

                self.sprites.append(frame27)

            WidthNatB = (int((3/100)*screenwidth))+30
            HeightNatB = (int((6/100)*screenheight))+40

        global currentSprite
        self.current_sprite = currentSprite
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)

    def update(self):

        global LAB
        if LAB:
            if self.current_sprite < 4:
                self.current_sprite = 4
            self.current_sprite += spriteplus
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 4
        else:
            self.current_sprite += spriteplus

            if self.current_sprite >= (len(self.sprites)-4):
                self.current_sprite = 0

        global XNat
        global YNat
        global Statik


        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:             #en fonction de la partie de map, la classe va verifier si le joueur n'est pas dans une zone d'obstacle, alors il peut avancer ou pas

            if MapPart5 == True:
                if (YNat < screenheight - vitesse - 45) and (not((obstacles["arbre1part5"][0] < XNat < obstacles["arbre1part5"][1]) and (obstacles["arbre1part5"][2]-10 < YNat < obstacles["arbre1part5"][3]))) and (not((obstacles["arbre2part5"][0] < XNat < obstacles["arbre2part5"][1]) and (obstacles["arbre2part5"][2]-10 < YNat < obstacles["arbre2part5"][3]))) and (not((obstacles["GrandArbreHautpart5"][0] < XNat < obstacles["GrandArbreHautpart5"][1]) and (obstacles["GrandArbreHautpart5"][2]-10 < YNat < obstacles["GrandArbreHautpart5"][3]))) and (not((obstacles["GrandArbreTroncpart5"][0] < XNat < obstacles["GrandArbreTroncpart5"][1]) and (obstacles["GrandArbreTroncpart5"][2]-10 < YNat < obstacles["GrandArbreTroncpart5"][3]))) and (not((obstacles["arbre3part5"][0] < XNat < obstacles["arbre3part5"][1]) and (obstacles["arbre3part5"][2]-10 < YNat < obstacles["arbre3part5"][3]))) and (not((obstacles["arbre4part5"][0] < XNat < obstacles["arbre4part5"][1]) and (obstacles["arbre4part5"][2]-10 < YNat < obstacles["arbre4part5"][3]))):
                    YNat +=vitesse

            elif MapPart6 == True:
                if (YNat < screenheight - vitesse - 45) and (not((obstacles["arbre1part6"][0] < XNat < obstacles["arbre1part6"][1]) and (obstacles["arbre1part6"][2]-10 < YNat < obstacles["arbre1part6"][3]))) and (not((obstacles["arbre2part6"][0] < XNat < obstacles["arbre2part6"][1]) and (obstacles["arbre2part6"][2]-10 < YNat < obstacles["arbre2part6"][3]))) and (not((obstacles["arbre3part6"][0] < XNat < obstacles["arbre3part6"][1]) and (obstacles["arbre3part6"][2]-10 < YNat < obstacles["arbre3part6"][3]))) and (not((obstacles["arbre4part6"][0] < XNat < obstacles["arbre4part6"][1]) and (obstacles["arbre4part6"][2]-10 < YNat < obstacles["arbre4part6"][3]))) and (not((obstacles["arbre5part6"][0] < XNat < obstacles["arbre5part6"][1]) and (obstacles["arbre5part6"][2]-10 < YNat < obstacles["arbre5part6"][3]))):
                    YNat += vitesse

            elif MapPart1 == True:
                if (not((obstacles["arbre1part1"][0] < XNat < obstacles["arbre1part1"][1]) and (obstacles["arbre1part1"][2]-9 < YNat < obstacles["arbre1part1"][3]))) and (not((obstacles["house1.1part1"][0] < XNat < obstacles["house1.1part1"][1]) and (obstacles["house1.1part1"][2]-9 < YNat < obstacles["house1.1part1"][3]))) and (not((obstacles["house1.2part1"][0] < XNat < obstacles["house1.2part1"][1]) and (obstacles["house1.2part1"][2]-9 < YNat < obstacles["house1.2part1"][3]))) and (not((obstacles["arbre2part1"][0] < XNat < obstacles["arbre2part1"][1]) and (obstacles["arbre2part1"][2]-9 < YNat < obstacles["arbre2part1"][3]))) and (not((obstacles["arbre3part1"][0] < XNat < obstacles["arbre3part1"][1]) and (obstacles["arbre3part1"][2]-9 < YNat < obstacles["arbre3part1"][3]))) and (not((obstacles["arbre4part1"][0] < XNat < obstacles["arbre4part1"][1]) and (obstacles["arbre4part1"][2]-9 < YNat < obstacles["arbre4part1"][3]))) and (not((obstacles["arbre5part1"][0] < XNat < obstacles["arbre5part1"][1]) and (obstacles["arbre5part1"][2]-9 < YNat < obstacles["arbre5part1"][3]))) and (not((obstacles["Centrepokemon"][0] < XNat < obstacles["Centrepokemon"][1]) and (obstacles["Centrepokemon"][2]-9 < YNat < obstacles["Centrepokemon"][3])))and (not((obstacles["Hautarbrepart1"][0] < XNat < obstacles["Hautarbrepart1"][1]) and (obstacles["Hautarbrepart1"][2]-9 < YNat < obstacles["Hautarbrepart1"][3]))) and (not((obstacles["barriere1part1"][0] < XNat < obstacles["barriere1part1"][1]) and (obstacles["barriere1part1"][2]-9 < YNat < obstacles["barriere1part1"][3]))) and (not((obstacles["barriere2part1"][0] < XNat < obstacles["barriere2part1"][1]) and (obstacles["barriere2part1"][2]-9 < YNat < obstacles["barriere2part1"][3]))) and (not((obstacles["barriere3part1"][0] < XNat < obstacles["barriere3part1"][1]) and (obstacles["barriere3part1"][2]-9 < YNat < obstacles["barriere3part1"][3]))):
                    YNat +=vitesse

            elif MapPart2 == True:
                if (not((obstacles["Hautarbrepart2"][0] < XNat < obstacles["Hautarbrepart2"][1]) and (obstacles["Hautarbrepart2"][2]-5 < YNat < obstacles["Hautarbrepart2"][3]))) and (not((obstacles["Droitearbrepart2"][0] < XNat < obstacles["Droitearbrepart2"][1]) and (obstacles["Droitearbrepart2"][2]-5 < YNat < obstacles["Droitearbrepart2"][3]))) and (not((obstacles["barriere1part2"][0] < XNat < obstacles["barriere1part2"][1]) and (obstacles["barriere1part2"][2]-10 < YNat < obstacles["barriere1part2"][3]))) and (not((obstacles["barriere2part2"][0] < XNat < obstacles["barriere2part2"][1]) and (obstacles["barriere2part2"][2]-10 < YNat < obstacles["barriere2part2"][3]))) and (not((obstacles["barriere3part2"][0] < XNat < obstacles["barriere3part2"][1]) and (obstacles["barriere3part2"][2]-10 < YNat < obstacles["barriere3part2"][3]))) and (not((obstacles["barriere4part2"][0] < XNat < obstacles["barriere4part2"][1]) and (obstacles["barriere4part2"][2]-10 < YNat < obstacles["barriere4part2"][3]))) and (not((obstacles["arbre1part2"][0] < XNat < obstacles["arbre1part2"][1]) and (obstacles["arbre1part2"][2]-10 < YNat < obstacles["arbre1part2"][3]))) and (not((obstacles["arbre2part2"][0] < XNat < obstacles["arbre2part2"][1]) and (obstacles["arbre2part2"][2]-10 < YNat < obstacles["arbre2part2"][3]))):
                    YNat += vitesse

            elif MapPart3 == True:
                if (not((obstacles["house1"][0] < XNat < obstacles["house1"][1]) and (obstacles["house1"][2]-10 < YNat < obstacles["house1"][3]))) and (not((obstacles["house2"][0] < XNat < obstacles["house2"][1]) and (obstacles["house2"][2] < YNat < obstacles["house2"][3]))) and (not((obstacles["bushligne"][0] < XNat < obstacles["bushligne"][1]) and (obstacles["bushligne"][2]-10 < YNat < obstacles["bushligne"][3]))) and (not((obstacles["barriere1"][0] < XNat < obstacles["barriere1"][1]) and (obstacles["barriere1"][2] < YNat < obstacles["barriere1"][3]))) and (not((obstacles["barriere2"][0] < XNat < obstacles["barriere2"][1]) and (obstacles["barriere2"][2]-5 < YNat < obstacles["barriere2"][3]))) and (not((obstacles["barriere3"][0] < XNat < obstacles["barriere3"][1]) and (obstacles["barriere3"][2]-5 < YNat < obstacles["barriere3"][3]))) and (not((obstacles["house3"][0] < XNat < obstacles["house3"][1]) and (obstacles["house3"][2]-10 < YNat < obstacles["house3"][3]))) and (not((obstacles["3bush1"][0] < XNat < obstacles["3bush1"][1]) and (obstacles["3bush1"][2]-10 < YNat < obstacles["3bush1"][3]))) and (not((obstacles["3bush2"][0] < XNat < obstacles["3bush2"][1]) and (obstacles["3bush2"][2]-10 < YNat < obstacles["3bush2"][3]))) and (not((obstacles["3bush3"][0] < XNat < obstacles["3bush3"][1]) and (obstacles["3bush3"][2]-10 < YNat < obstacles["3bush3"][3]))) and (not((obstacles["3bush4"][0] < XNat < obstacles["3bush4"][1]) and (obstacles["3bush4"][2]-10 < YNat < obstacles["3bush4"][3]))) and (not((obstacles["3bush5"][0] < XNat < obstacles["3bush5"][1]) and (obstacles["3bush5"][2]-10 < YNat < obstacles["3bush5"][3]))) and (not((obstacles["3bush6"][0] < XNat < obstacles["3bush6"][1]) and (obstacles["3bush6"][2]-10 < YNat < obstacles["3bush6"][3]))):
                    YNat += vitesse

            elif MapPart4 == True:
                if not((obstacles["barriere4"][0] < XNat < obstacles["barriere4"][1]) and (obstacles["barriere4"][2]-9 < YNat < obstacles["barriere4"][3])) and (not((obstacles["house3bis"][0] < XNat < obstacles["house3bis"][1]) and (obstacles["house3bis"][2]-10 < YNat < obstacles["house3bis"][3]))) and (not((obstacles["house4"][0] < XNat < obstacles["house4"][1]) and (obstacles["house4"][2]-10 < YNat < obstacles["house4"][3]))) and (not((obstacles["house5"][0] < XNat < obstacles["house5"][1]) and (obstacles["house5"][2]-10 < YNat < obstacles["house5"][3]))) and (not((obstacles["house5bis"][0] < XNat < obstacles["house5bis"][1]) and (obstacles["house5bis"][2]-10 < YNat < obstacles["house5bis"][3]))) and (not((obstacles["marketbis"][0] < XNat < obstacles["marketbis"][1]) and (obstacles["marketbis"][2] < YNat < obstacles["marketbis"][3]))):
                    YNat += vitesse

            elif LAB:
                if screenwidth-vitesse-20 > XNat > 15+vitesse and YNat > 350 and not((0<XNat<485) and (screenheight-45-vitesse<YNat<screenheight)) and not((690-vitesse<XNat<screenwidth) and (screenheight-45-vitesse < YNat < screenheight)) and not((0<XNat<284+vitesse) and (432-vitesse < YNat < 625+vitesse)) and not((900-vitesse<XNat<screenwidth) and (0 < YNat < 525+vitesse)) and not((110-vitesse<XNat<200+vitesse) and (350 < YNat < 405+vitesse)):
                    YNat+= vitesse

            else:
                YNat+= vitesse



            self.rect.center = (XNat, YNat)
        if Statik:
            if LAB:
                self.current_sprite = 4
            else:
                self.current_sprite = 0


        self.image = self.sprites[int(self.current_sprite)]

class NATHANOVERD(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        global WidthNatD
        global HeightNatD

        for j in range(2):
            num28 = 0
            for i in range (1, 5):      #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
                num28 += 1

                name28 = str('HerosOverworldDroite-' + str(num28) + '.png')

                frame28 = pygame.image.load(name28)
                frame28 = pygame.transform.scale(frame28, (WidthNatD, HeightNatD))

                self.sprites.append(frame28)

            WidthNatD = (int((3/100)*screenwidth))+30
            HeightNatD = (int((6/100)*screenheight))+40



        global currentSprite
        self.current_sprite = currentSprite
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)

    def update(self):

        global LAB
        if LAB:
            if self.current_sprite < 4:
                self.current_sprite = 4
            self.current_sprite += spriteplus
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 4
        else:
            self.current_sprite += spriteplus

            if self.current_sprite >= (len(self.sprites)-4):
                self.current_sprite = 0

        global XNat
        global YNat
        global Statik


        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:        #en fonction de la partie de map, la classe va verifier si le joueur n'est pas dans une zone d'obstacle, alors il peut avancer ou pas

            if MapPart6 == True:
                if (XNat < screenwidth - vitesse - 50) and (not((obstacles["arbre1part6"][0]-10 < XNat < obstacles["arbre1part6"][1]) and (obstacles["arbre1part6"][2] < YNat < obstacles["arbre1part6"][3]))) and (not((obstacles["arbre2part6"][0]-10 < XNat < obstacles["arbre2part6"][1]) and (obstacles["arbre2part6"][2] < YNat < obstacles["arbre2part6"][3]))) and (not((obstacles["arbre3part6"][0]-10 < XNat < obstacles["arbre3part6"][1]) and (obstacles["arbre3part6"][2] < YNat < obstacles["arbre3part6"][3]))) and (not((obstacles["arbre4part6"][0]-10 < XNat < obstacles["arbre4part6"][1]) and (obstacles["arbre4part6"][2] < YNat < obstacles["arbre4part6"][3]))) and (not((obstacles["arbre5part6"][0]-10 < XNat < obstacles["arbre5part6"][1]) and (obstacles["arbre5part6"][2] < YNat < obstacles["arbre5part6"][3]))):
                    XNat += vitesse

            elif MapPart1 == True:
                if (not((obstacles["arbre1part1"][0]-9 < XNat < obstacles["arbre1part1"][1]) and (obstacles["arbre1part1"][2] < YNat < obstacles["arbre1part1"][3]))) and (not((obstacles["house1.1part1"][0]-9 < XNat < obstacles["house1.1part1"][1]) and (obstacles["house1.1part1"][2] < YNat < obstacles["house1.1part1"][3]))) and (not((obstacles["house1.2part1"][0]-9 < XNat < obstacles["house1.2part1"][1]) and (obstacles["house1.2part1"][2] < YNat < obstacles["house1.2part1"][3]))) and (not((obstacles["arbre2part1"][0]-9 < XNat < obstacles["arbre2part1"][1]) and (obstacles["arbre2part1"][2] < YNat < obstacles["arbre2part1"][3]))) and (not((obstacles["arbre3part1"][0]-9 < XNat < obstacles["arbre3part1"][1]) and (obstacles["arbre3part1"][2] < YNat < obstacles["arbre3part1"][3]))) and (not((obstacles["arbre4part1"][0]-9 < XNat < obstacles["arbre4part1"][1]) and (obstacles["arbre4part1"][2] < YNat < obstacles["arbre4part1"][3]))) and (not((obstacles["arbre5part1"][0]-9 < XNat < obstacles["arbre5part1"][1]) and (obstacles["arbre5part1"][2] < YNat < obstacles["arbre5part1"][3]))) and (not((obstacles["Centrepokemon"][0]-9 < XNat < obstacles["Centrepokemon"][1]) and (obstacles["Centrepokemon"][2] < YNat < obstacles["Centrepokemon"][3])))and (not((obstacles["Hautarbrepart1"][0]-9 < XNat < obstacles["Hautarbrepart1"][1]) and (obstacles["Hautarbrepart1"][2] < YNat < obstacles["Hautarbrepart1"][3]))) and (not((obstacles["barriere1part1"][0]-9 < XNat < obstacles["barriere1part1"][1]) and (obstacles["barriere1part1"][2] < YNat < obstacles["barriere1part1"][3]))) and (not((obstacles["barriere2part1"][0]-9 < XNat < obstacles["barriere2part1"][1]) and (obstacles["barriere2part1"][2] < YNat < obstacles["barriere2part1"][3]))) and (not((obstacles["barriere3part1"][0]-9 < XNat < obstacles["barriere3part1"][1]) and (obstacles["barriere3part1"][2] < YNat < obstacles["barriere3part1"][3]))):
                    XNat += vitesse

            elif MapPart2 == True:
                if (XNat < screenwidth - vitesse - 50) and (not((obstacles["Hautarbrepart2"][0]-5 < XNat < obstacles["Hautarbrepart2"][1]) and (obstacles["Hautarbrepart2"][2] < YNat < obstacles["Hautarbrepart2"][3]))) and (not((obstacles["Droitearbrepart2"][0]-5 < XNat < obstacles["Droitearbrepart2"][1]) and (obstacles["Droitearbrepart2"][2] < YNat < obstacles["Droitearbrepart2"][3]+5))) and (not((obstacles["barriere1part2"][0] < XNat < obstacles["barriere1part2"][1]) and (obstacles["barriere1part2"][2] < YNat < obstacles["barriere1part2"][3]))) and (not((obstacles["barriere2part2"][0]-5 < XNat < obstacles["barriere2part2"][1]) and (obstacles["barriere2part2"][2] < YNat < obstacles["barriere2part2"][3]))) and (not((obstacles["barriere3part2"][0]-10 < XNat < obstacles["barriere3part2"][1]) and (obstacles["barriere3part2"][2] < YNat < obstacles["barriere3part2"][3]))) and (not((obstacles["barriere4part2"][0]-10 < XNat < obstacles["barriere4part2"][1]) and (obstacles["barriere4part2"][2] < YNat < obstacles["barriere4part2"][3]))) and (not((obstacles["arbre1part2"][0]-10 < XNat < obstacles["arbre1part2"][1]) and (obstacles["arbre1part2"][2] < YNat < obstacles["arbre1part2"][3]))) and (not((obstacles["arbre2part2"][0]-10 < XNat < obstacles["arbre2part2"][1]) and (obstacles["arbre2part2"][2] < YNat < obstacles["arbre2part2"][3]))):
                    XNat += vitesse

            elif MapPart3 == True:
                if (not((obstacles["house1"][0]-10 < XNat < obstacles["house1"][1]) and (obstacles["house1"][2] < YNat < obstacles["house1"][3]))) and (not((obstacles["house2"][0]-10 < XNat < obstacles["house2"][1]) and (obstacles["house2"][2] < YNat < obstacles["house2"][3]))) and (not((screenwidth-vitesse-20 < XNat) and (25-vitesse < YNat < 362+vitesse))) and (not((obstacles["bushligne"][0]-10 < XNat < obstacles["bushligne"][1]) and (obstacles["bushligne"][2] < YNat < obstacles["bushligne"][3]))) and (not((obstacles["barriere1"][0]-10 < XNat < obstacles["barriere1"][1]) and (obstacles["barriere1"][2] < YNat < obstacles["barriere1"][3]))) and (not((obstacles["barriere2"][0]-5 < XNat < obstacles["barriere2"][1]) and (obstacles["barriere2"][2] < YNat < obstacles["barriere2"][3]))) and (not((obstacles["barriere3"][0]-5 < XNat < obstacles["barriere3"][1]) and (obstacles["barriere3"][2] < YNat < obstacles["barriere3"][3]))) and (not((obstacles["house3"][0]-10< XNat < obstacles["house3"][1]) and (obstacles["house3"][2] < YNat < obstacles["house3"][3]))) and (not((obstacles["3bush1"][0]-10< XNat < obstacles["3bush1"][1]) and (obstacles["3bush1"][2] < YNat < obstacles["3bush1"][3]))) and (not((obstacles["3bush2"][0]-10< XNat < obstacles["3bush2"][1]) and (obstacles["3bush2"][2] < YNat < obstacles["3bush2"][3]))) and (not((obstacles["3bush3"][0]-10< XNat < obstacles["3bush3"][1]) and (obstacles["3bush3"][2] < YNat < obstacles["3bush3"][3]))) and (not((obstacles["3bush4"][0]-10< XNat < obstacles["3bush4"][1]) and (obstacles["3bush4"][2] < YNat < obstacles["3bush4"][3]))) and (not((obstacles["3bush5"][0]-10< XNat < obstacles["3bush5"][1]) and (obstacles["3bush5"][2] < YNat < obstacles["3bush5"][3]))) and (not((obstacles["3bush6"][0]-10< XNat < obstacles["3bush6"][1]) and (obstacles["3bush6"][2] < YNat < obstacles["3bush6"][3]))):
                    XNat += vitesse

            elif MapPart4 == True:
                if (XNat < screenwidth - vitesse - 50) and (not((obstacles["barriere4"][0] < XNat < obstacles["barriere4"][1]) and (obstacles["barriere4"][2] < YNat < obstacles["barriere4"][3]))) and (not((obstacles["house3bis"][0]< XNat < obstacles["house3bis"][1]) and (obstacles["house3bis"][2] < YNat < obstacles["house3bis"][3]))) and (not((obstacles["house4"][0]-10< XNat < obstacles["house4"][1]) and (obstacles["house4"][2] < YNat < obstacles["house4"][3]))) and (not((obstacles["house5"][0]-10< XNat < obstacles["house5"][1]) and (obstacles["house5"][2] < YNat < obstacles["house5"][3]))) and (not((obstacles["house5bis"][0]-10< XNat < obstacles["house5bis"][1]) and (obstacles["house5bis"][2] < YNat < obstacles["house5bis"][3]))) and (not((obstacles["marketbis"][0]-10< XNat < obstacles["marketbis"][1]) and (obstacles["marketbis"][2] < YNat < obstacles["marketbis"][3]))):
                    XNat += vitesse

            elif LAB:
                if screenwidth-vitesse-35 > XNat > 15+vitesse and YNat > 350 and not((0<XNat<485) and (screenheight-40-vitesse<YNat<screenheight)) and not((690-vitesse<XNat<screenwidth) and (screenheight-40-vitesse < YNat < screenheight)) and not((0<XNat<284+vitesse) and (438-vitesse < YNat < 625+vitesse)) and not((895-vitesse<XNat<screenwidth) and (0 < YNat < 525+vitesse)) and not((100-vitesse<XNat<200+vitesse) and (350 < YNat < 405+vitesse)):
                    XNat+= vitesse

            else:
                XNat+= vitesse





            self.rect.center = (XNat, YNat)
        if Statik:
            if LAB:
                self.current_sprite = 4
            else:
                self.current_sprite = 0


        self.image = self.sprites[int(self.current_sprite)]

class NATHANOVERG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        global WidthNatG
        global HeightNatG


        for j in range (2):
            num29 = 0
            for i in range (1, 5):      #grace a une boucle on appelle chaque image de l'animation dans une liste, dans l'update de la classe qui va constamment s'actualiser tant que la classe est active on va alors afficher ces images une par une à la suite, donnant un effet d'animation fluide
                num29 += 1

                name29 = str('HerosOverworldGauche-' + str(num29) + '.png')

                frame29 = pygame.image.load(name29)
                frame29 = pygame.transform.scale(frame29, (WidthNatG, HeightNatG))

                self.sprites.append(frame29)

            WidthNatG = (int((3/100)*screenwidth))+30
            HeightNatG = (int((6/100)*screenheight))+40


        global currentSprite
        self.current_sprite = currentSprite
        self.image = self.sprites[self.current_sprite]



        self.rect = self.image.get_rect()
        self.rect.center = (XNat,YNat)

    def update(self):

        global LAB
        if LAB:
            if self.current_sprite < 4:
                self.current_sprite = 4
            self.current_sprite += spriteplus
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 4
        else:
            self.current_sprite += spriteplus

            if self.current_sprite >= (len(self.sprites)-4):
                self.current_sprite = 0

        global XNat
        global YNat
        global Statik



        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:     #en fonction de la partie de map, la classe va verifier si le joueur n'est pas dans une zone d'obstacle, alors il peut avancer ou pas
            if MapPart5 == True:
                if (XNat > vitesse+50) and (not((obstacles["arbre1part5"][0] < XNat < obstacles["arbre1part5"][1]+10) and (obstacles["arbre1part5"][2] < YNat < obstacles["arbre1part5"][3]))) and (not((obstacles["arbre2part5"][0] < XNat < obstacles["arbre2part5"][1]+10) and (obstacles["arbre2part5"][2] < YNat < obstacles["arbre2part5"][3]))) and (not((obstacles["GrandArbreHautpart5"][0] < XNat < obstacles["GrandArbreHautpart5"][1]+10) and (obstacles["GrandArbreHautpart5"][2] < YNat < obstacles["GrandArbreHautpart5"][3]))) and (not((obstacles["GrandArbreTroncpart5"][0] < XNat < obstacles["GrandArbreTroncpart5"][1]+10) and (obstacles["GrandArbreTroncpart5"][2] < YNat < obstacles["GrandArbreTroncpart5"][3]))) and (not((obstacles["arbre3part5"][0] < XNat < obstacles["arbre3part5"][1]+10) and (obstacles["arbre3part5"][2] < YNat < obstacles["arbre3part5"][3]))) and (not((obstacles["arbre4part5"][0] < XNat < obstacles["arbre4part5"][1]+10) and (obstacles["arbre4part5"][2] < YNat < obstacles["arbre4part5"][3]))):
                    XNat-= vitesse

            elif MapPart1 == True:
                if (XNat > vitesse+50) and (not((obstacles["arbre1part1"][0] < XNat < obstacles["arbre1part1"][1]+9) and (obstacles["arbre1part1"][2] < YNat < obstacles["arbre1part1"][3]))) and (not((obstacles["house1.1part1"][0] < XNat < obstacles["house1.1part1"][1]+9) and (obstacles["house1.1part1"][2] < YNat < obstacles["house1.1part1"][3]))) and (not((obstacles["house1.2part1"][0] < XNat < obstacles["house1.2part1"][1]+9) and (obstacles["house1.2part1"][2] < YNat < obstacles["house1.2part1"][3]))) and (not((obstacles["arbre2part1"][0] < XNat < obstacles["arbre2part1"][1]+9) and (obstacles["arbre2part1"][2] < YNat < obstacles["arbre2part1"][3]))) and (not((obstacles["arbre3part1"][0] < XNat < obstacles["arbre3part1"][1]+9) and (obstacles["arbre3part1"][2] < YNat < obstacles["arbre3part1"][3]))) and (not((obstacles["arbre4part1"][0] < XNat < obstacles["arbre4part1"][1]+9) and (obstacles["arbre4part1"][2] < YNat < obstacles["arbre4part1"][3]))) and (not((obstacles["arbre5part1"][0] < XNat < obstacles["arbre5part1"][1]+9) and (obstacles["arbre5part1"][2] < YNat < obstacles["arbre5part1"][3]))) and (not((obstacles["Centrepokemon"][0] < XNat < obstacles["Centrepokemon"][1]+9) and (obstacles["Centrepokemon"][2] < YNat < obstacles["Centrepokemon"][3])))and (not((obstacles["Hautarbrepart1"][0] < XNat < obstacles["Hautarbrepart1"][1]+9) and (obstacles["Hautarbrepart1"][2] < YNat < obstacles["Hautarbrepart1"][3]))) and (not((obstacles["barriere1part1"][0] < XNat < obstacles["barriere1part1"][1]+5) and (obstacles["barriere1part1"][2] < YNat < obstacles["barriere1part1"][3]))) and (not((obstacles["barriere2part1"][0] < XNat < obstacles["barriere2part1"][1]+9) and (obstacles["barriere2part1"][2] < YNat < obstacles["barriere2part1"][3]))) and (not((obstacles["barriere3part1"][0] < XNat < obstacles["barriere3part1"][1]+5) and (obstacles["barriere3part1"][2] < YNat < obstacles["barriere3part1"][3]))):
                    XNat-=vitesse

            elif MapPart2 == True:
                if (not((obstacles["Hautarbrepart2"][0] < XNat < obstacles["Hautarbrepart2"][1]+5) and (obstacles["Hautarbrepart2"][2] < YNat < obstacles["Hautarbrepart2"][3]))) and (not((obstacles["Droitearbrepart2"][0] < XNat < obstacles["Droitearbrepart2"][1]+10) and (obstacles["Droitearbrepart2"][2] < YNat < obstacles["Droitearbrepart2"][3]))) and (not((obstacles["barriere1part2"][0] < XNat < obstacles["barriere1part2"][1]+5) and (obstacles["barriere1part2"][2] < YNat < obstacles["barriere1part2"][3]))) and (not((obstacles["barriere2part2"][0] < XNat < obstacles["barriere2part2"][1]+10) and (obstacles["barriere2part2"][2] < YNat < obstacles["barriere2part2"][3]))) and (not((obstacles["barriere3part2"][0] < XNat < obstacles["barriere3part2"][1]+10) and (obstacles["barriere3part2"][2] < YNat < obstacles["barriere3part2"][3]))) and (not((obstacles["barriere4part2"][0] < XNat < obstacles["barriere4part2"][1]+10) and (obstacles["barriere4part2"][2] < YNat < obstacles["barriere4part2"][3]))) and (not((obstacles["arbre1part2"][0] < XNat < obstacles["arbre1part2"][1]+10) and (obstacles["arbre1part2"][2] < YNat < obstacles["arbre1part2"][3]))) and (not((obstacles["arbre2part2"][0] < XNat < obstacles["arbre2part2"][1]+10) and (obstacles["arbre2part2"][2] < YNat < obstacles["arbre2part2"][3]))):
                    XNat -= vitesse

            elif MapPart3 == True:                          #House1
                if XNat > vitesse + 50 and (not((obstacles["house1"][0] < XNat < obstacles["house1"][1]+5) and (obstacles["house1"][2] < YNat < obstacles["house1"][3]))) and (not((obstacles["house2"][0] < XNat < obstacles["house2"][1]) and (obstacles["house2"][2] < YNat < obstacles["house2"][3]))) and (not((obstacles["bushligne"][0] < XNat < obstacles["bushligne"][1]) and (obstacles["bushligne"][2] < YNat < obstacles["bushligne"][3]))) and (not((obstacles["barriere1"][0] < XNat < obstacles["barriere1"][1]+10) and (obstacles["barriere1"][2] < YNat < obstacles["barriere1"][3]))) and (not((obstacles["barriere2"][0] < XNat < obstacles["barriere2"][1]+10) and (obstacles["barriere2"][2] < YNat < obstacles["barriere2"][3]))) and (not((obstacles["barriere3"][0] < XNat < obstacles["barriere3"][1]) and (obstacles["barriere3"][2] < YNat < obstacles["barriere3"][3]))) and (not((obstacles["house3"][0] < XNat < obstacles["house3"][1]) and (obstacles["house3"][2] < YNat < obstacles["house3"][3]))) and (not((obstacles["3bush1"][0] < XNat < obstacles["3bush1"][1]+10) and (obstacles["3bush1"][2] < YNat < obstacles["3bush1"][3]))) and (not((obstacles["3bush2"][0] < XNat < obstacles["3bush2"][1]+10) and (obstacles["3bush2"][2] < YNat < obstacles["3bush2"][3]))) and (not((obstacles["3bush3"][0] < XNat < obstacles["3bush3"][1]+10) and (obstacles["3bush3"][2] < YNat < obstacles["3bush3"][3]))) and (not((obstacles["3bush4"][0] < XNat < obstacles["3bush4"][1]+10) and (obstacles["3bush4"][2] < YNat < obstacles["3bush4"][3]))) and (not((obstacles["3bush5"][0] < XNat < obstacles["3bush5"][1]+10) and (obstacles["3bush5"][2] < YNat < obstacles["3bush5"][3]))) and (not((obstacles["3bush6"][0] < XNat < obstacles["3bush6"][1]+10) and (obstacles["3bush6"][2] < YNat < obstacles["3bush6"][3]))):
                    XNat -= vitesse

            elif MapPart4 == True:
                if not((obstacles["barriere4"][0] < XNat < obstacles["barriere4"][1]+9) and (obstacles["barriere4"][2] < YNat < obstacles["barriere4"][3])) and (not((obstacles["house3bis"][0] < XNat < obstacles["house3bis"][1]+10) and (obstacles["house3bis"][2] < YNat < obstacles["house3bis"][3]))) and (not((obstacles["house4"][0] < XNat < obstacles["house4"][1]+10) and (obstacles["house4"][2] < YNat < obstacles["house4"][3]))) and (not((obstacles["house5"][0] < XNat < obstacles["house5"][1]+10) and (obstacles["house5"][2] < YNat < obstacles["house5"][3]))) and (not((obstacles["house5bis"][0] < XNat < obstacles["house5bis"][1]+10) and (obstacles["house5bis"][2] < YNat < obstacles["house5bis"][3]))) and (not((obstacles["marketbis"][0] < XNat < obstacles["marketbis"][1]+10) and (obstacles["marketbis"][2] < YNat < obstacles["marketbis"][3]))):
                    XNat -= vitesse

            elif MapPart6 == True:
                if (not((obstacles["arbre1part6"][0] < XNat < obstacles["arbre1part6"][1]+10) and (obstacles["arbre1part6"][2] < YNat < obstacles["arbre1part6"][3]))) and (not((obstacles["arbre2part6"][0] < XNat < obstacles["arbre2part6"][1]+10) and (obstacles["arbre2part6"][2] < YNat < obstacles["arbre2part6"][3]))) and (not((obstacles["arbre3part6"][0] < XNat < obstacles["arbre3part6"][1]+10) and (obstacles["arbre3part6"][2] < YNat < obstacles["arbre3part6"][3]))) and (not((obstacles["arbre4part6"][0] < XNat < obstacles["arbre4part6"][1]+10) and (obstacles["arbre4part6"][2] < YNat < obstacles["arbre4part6"][3]))) and (not((obstacles["arbre5part6"][0] < XNat < obstacles["arbre5part6"][1]+10) and (obstacles["arbre5part6"][2] < YNat < obstacles["arbre5part6"][3]))):
                    XNat -= vitesse

            elif LAB:
                if screenwidth-vitesse-20 > XNat > 40+vitesse and YNat > 350 and not((0<XNat<485) and (screenheight-40-vitesse<YNat<screenheight)) and not((690-vitesse<XNat<screenwidth) and (screenheight-40-vitesse < YNat < screenheight)) and not((0<XNat<290+vitesse) and (438-vitesse < YNat < 625+vitesse)) and not((900-vitesse<XNat<screenwidth) and (0 < YNat < 525+vitesse)) and not((110-vitesse<XNat<210+vitesse) and (350 < YNat < 405+vitesse)):
                    XNat-= vitesse

            else:
                XNat -= vitesse





            self.rect.center = (XNat, YNat)


        if Statik:
            if LAB:
                self.current_sprite = 4
            else:
                self.current_sprite = 0




        self.image = self.sprites[int(self.current_sprite)]



#on ajoute tout ca a des groupes
all_spritesNOH = pygame.sprite.Group()
Nathanoverh=NATHANOVERH()
all_spritesNOH.add(Nathanoverh)
all_spritesNOB = pygame.sprite.Group()
Nathanoverb=NATHANOVERB()
all_spritesNOB.add(Nathanoverb)
all_spritesNOD = pygame.sprite.Group()
Nathanoverd=NATHANOVERD()
all_spritesNOD.add(Nathanoverd)
all_spritesNOG = pygame.sprite.Group()
Nathanoverg=NATHANOVERG()
all_spritesNOG.add(Nathanoverg)

#on importe la carte avec chaque partie de map qui est un zoom sur la carte
background1Img = pygame.image.load('MapPokemon4.png')
background1Img = pygame.transform.scale(background1Img, (2400, int((1800/1000)*screenwidth)))
background1X = 0
background1Y = 0

background2Img = pygame.image.load('MapPokemon4.png')
background2Img = pygame.transform.scale(background2Img, (2400, int((1800/1000)*screenwidth)))
background2X = -1200
background2Y = 0

background3Img = pygame.image.load('MapPokemon4.png')
background3Img = pygame.transform.scale(background3Img, (2400, int((1800/1000)*screenwidth)))
background3X = 0
background3Y = -730

Barretexte = pygame.image.load('barretexte.png')
Barretexte = pygame.transform.scale(Barretexte,(int((100/100)*screenwidth),int((75/100)*screenheight)))
BarretexteX= (0/100)*screenwidth
BarretexteY= (30/100)*screenheight

DialogueRival = pygame.image.load('KalTalks.png')
DialogueRival = pygame.transform.scale(DialogueRival,(int((30/100)*screenwidth),int((27/100)*screenheight)))
DialogueRivalX= (0/100)*screenwidth
DialogueRivalY= (73/100)*screenheight

background4Img = pygame.image.load('MapPokemon4.png')
background4Img = pygame.transform.scale(background4Img, (2400, int((1800/1000)*screenwidth)))
background4X = -1200
background4Y = -730

background5Img = pygame.image.load('MapPokemon4.png')
background5Img = pygame.transform.scale(background5Img, (2400, int((1800/1000)*screenwidth)))
background5X = 0
background5Y = -1425

background6Img = pygame.image.load('MapPokemon4.png')
background6Img = pygame.transform.scale(background6Img, (2400, int((1800/1000)*screenwidth)))
background6X = -1200
background6Y = -1425

HerosStatique = pygame.image.load('HerosOverworldBas-1.png')
HerosStatique = pygame.transform.scale(HerosStatique, (int((3.6/100)*screenwidth), int((7.2/100)*screenheight)))
HerosStatiqueX = 40
HerosStatiqueY = 60

Labo = pygame.image.load('LabCourmTrue.png')
Labo = pygame.transform.scale(Labo, (1200, int((620/1000)*screenwidth)))
LaboX = 0
LaboY = 0



#encore des fonction qui vont afficher des trucs à l'ecran, mais pour la map
def background1():
    screen.blit(background1Img, (background1X, background1Y))

def background2():
    screen.blit(background2Img, (background2X, background2Y))

def background3():
    screen.blit(background3Img, (background3X, background3Y))

def background4():
    screen.blit(background4Img, (background4X, background4Y))

def background5():
    screen.blit(background5Img, (background5X, background5Y))

def background6():
    screen.blit(background6Img, (background6X, background6Y))

def Heros():
    screen.blit(HerosStatique, (HerosStatiqueX, HerosStatiqueY))

def barretexte():
    screen.blit(Barretexte, (BarretexteX, BarretexteY))

def KalDialogue():
    screen.blit(DialogueRival, (DialogueRivalX, DialogueRivalY))

def txtchallengeKal():
    screen.blit(textchallengeKal, (int((50/100)*screenwidth), int((86/100)*screenheight)))

def txtchallengeKal2():
    screen.blit(textchallengeKal2, (int((40/100)*screenwidth), int((92/100)*screenheight)))

def Laboratoire():
    screen.blit(Labo, (LaboX, LaboY))

MapPart1=False   #les booleens qui gerent les parties de map actives
MapPart2=False
MapPart3=False
MapPart4=False
MapPart5=True
MapPart6=False
Rivalfight=False
txtChallengeKal=False
Haut = True
Bas = False
Gauche = False
Droite = False
Statik = True
Startpos = True

#de nouvelles polices et textes
policearialdialogue = pygame.font.Font("Pokemon.ttf", 30)
policearialdialogue2 = pygame.font.Font("Pokemon.ttf", 20)
textchallengeKal = policearialdialogue.render("Tu es prêt ?", 1, white)
textchallengeKal2 = policearialdialogue2.render("(cliquer sur espace pour commencer)", 1, white)


LAB = False



#fonction qui facilite l'actualisation de l'ecran en continu en fonction de la direction du personnage
def UpdateScreen():

        keys = pygame.key.get_pressed()
        global spriteplus
        global currentSprite
        global Startpos

        if Droite:
            all_spritesNOD.add(Nathanoverd)
            all_spritesNOD.update()
            all_spritesNOD.draw(screen)
            all_spritesNOB.remove(Nathanoverb)
            all_spritesNOG.remove(Nathanoverg)
            all_spritesNOH.remove(Nathanoverh)
            Startpos = False
        elif Gauche:
            all_spritesNOG.add(Nathanoverg)
            all_spritesNOG.update()
            all_spritesNOG.draw(screen)
            all_spritesNOB.remove(Nathanoverb)
            all_spritesNOD.remove(Nathanoverd)
            all_spritesNOH.remove(Nathanoverh)
            Startpos = False
        elif Bas:
            all_spritesNOB.add(Nathanoverb)
            all_spritesNOB.update()
            all_spritesNOB.draw(screen)
            all_spritesNOD.remove(Nathanoverd)
            all_spritesNOG.remove(Nathanoverg)
            all_spritesNOH.remove(Nathanoverh)
            Startpos = False
        elif Haut:
            all_spritesNOH.add(Nathanoverh)
            all_spritesNOH.update()
            all_spritesNOH.draw(screen)
            all_spritesNOB.remove(Nathanoverb)
            all_spritesNOG.remove(Nathanoverg)
            all_spritesNOD.remove(Nathanoverd)
            Startpos = False

        elif Startpos:
            all_spritesNOB.remove(Nathanoverb)
            all_spritesNOG.remove(Nathanoverg)
            all_spritesNOD.remove(Nathanoverd)
            all_spritesNOH.update()


        else:
            spriteplus = 0
            currentSprite = 0
            all_spritesNOH.update()
            all_spritesNOH.draw(screen)
            all_spritesNOB.update()
            all_spritesNOB.draw(screen)
            all_spritesNOG.update()
            all_spritesNOG.draw(screen)
            all_spritesNOD.update()
            all_spritesNOD.draw(screen)
            Statik = True





############################################################################################# Map Pokemon

############################################################################################# Boucle Map

running = True
while running:  #boucle principale du jeu


    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()


    if txtChallengeKal == False:


        if Startpos:
            UpdateScreen()

        if MapPart1==True:      #verifie dans  quelle partie de map on se trouve et affiche en continu la bonne
            background1()


        if XNat>=screenwidth and MapPart1 ==True:
            MapPart2=True
            MapPart1=False
            XNat-=1180
            UpdateScreen()

        if MapPart2==True:
            background2()

        if MapPart3==True:
            background3()

        if MapPart4==True:
            background4()

        if MapPart5==True:
            background5()

        if MapPart6==True:
            background6()

        if LAB == True:
            Laboratoire()



        if XNat<=0 and MapPart2==True:   #change les valeurs de MapPart en fonction de la ou on se trouve
            MapPart2=False
            MapPart1=True
            XNat+=1180
            UpdateScreen()

        if YNat >=screenheight and MapPart1==True:
            MapPart1=False
            MapPart3=True
            YNat-= 721
            UpdateScreen()

        if YNat<=0 and MapPart3==True:
            MapPart3=False
            MapPart1=True
            YNat+=715
            UpdateScreen()

        if YNat>=screenheight and MapPart2==True:
            MapPart2=False
            MapPart4=True
            YNat-=715
            UpdateScreen()

        if YNat<=0 and MapPart4==True:
            MapPart4=False
            MapPart2=True
            YNat+=715
            UpdateScreen()

        if XNat<=0 and MapPart4==True:
            MapPart4=False
            MapPart3=True
            XNat+=1180
            UpdateScreen()

        if XNat>=screenwidth and MapPart3==True:
            MapPart3=False
            MapPart4=True
            XNat-=1180
            UpdateScreen()

        if YNat>=screenheight and MapPart3==True:
            MapPart3=False
            MapPart5=True
            YNat-=715
            UpdateScreen()

        if YNat<=0 and MapPart5==True:
            MapPart5=False
            MapPart3=True
            YNat+=715
            UpdateScreen()

        if XNat>=screenwidth and MapPart5==True:
            MapPart5=False
            MapPart6=True
            XNat-=1200
            UpdateScreen()

        if XNat<=0 and MapPart6==True:
            MapPart6=False
            MapPart5=True
            XNat+=1180
            UpdateScreen()

        if YNat>=screenheight and MapPart4==True:
            MapPart4=False
            MapPart6=True
            YNat-=715
            UpdateScreen()

        if YNat<=0 and MapPart6==True:
            MapPart6=False
            MapPart4=True
            YNat+=715
            UpdateScreen()


        if 1025<XNat<1075 and 250<YNat<260 and MapPart3==True and Haut == True:   #partie du labo dans lequel on peut rentrer
            MapPart3=False
            LAB=True
            WidthNat = int((5/100)*screenwidth)
            HeightNat = int((12/100)*screenheight)
            XNat-=430
            YNat+=430

        if 500<XNat<700 and YNat>=screenheight and LAB==True:  #on sort du labo
            LAB=False
            MapPart3=True
            WidthNat = int((3/100)*screenwidth)
            HeightNat = int((6/100)*screenheight)
            XNat=1050
            YNat=260


        keys = pygame.key.get_pressed()


        if 1000<XNat<1060 and 200<YNat<250 and MapPart2==True:   #emplacement de l'adversaire à qui on peut parler et lancer un combat
                barretexte()
                KalDialogue()
                txtchallengeKal()
                txtchallengeKal2()
                if keys[pygame.K_SPACE]:
                    txtChallengeKal=True
                    musicplaycombat = True











        if keys[pygame.K_RCTRL]:    #lorsque l'on clique sur controle de droite, le perso court
            if LAB:
                vitesse = 5
                if Statik == False:
                    spriteplus = 0.1
            else:
                vitesse = 8
                if Statik == False:
                    spriteplus = 0.4
        else:
            if LAB:
                vitesse = 5
                if Statik == False:
                    spriteplus = 0.1
            else:
                vitesse=4
                if Statik == False:
                    spriteplus = 0.2


        UpdateScreen()








            ########################################################################################### Boucle Map

            ########################################################################################### Boucle Combat

    if txtChallengeKal == True:   #un combat se lance si on va voir le dresseur ennemi


        #on appelle les fonctions pour afficher un objet, ici on lance l'animation de debut de combat

        background()

        if AnimationDebut == True:
            VSwait += 0.4
            Opposant()

        if VSwait > 25:
            DebutCombatY -= 8

        if VSwait > 20:
            HerosApparition = True
            HerosApparition2 = True
            HerosApparition3 = True
            Dresseur1 = True
            Dresseur2 = True

        if VSwait > 50:
            AnimationDebut = False
            VSwait = 0

        if Dresseur1 == True:
            RivalSurTerrain()

        if Dresseur2 == True:
            RivalSurTerrain2()
            Ennemy2X -= 4
            EnnemyX -= 4

        if Ennemy2X < 940:
            Dresseur2 = False
            all_spritesPokeball.update()
            all_spritesPokeball.draw(screen)
            KalWait += 0.4

        if KalWait >= 18:
            POKE1 = True

        if KalWait >= 28:
            EnnemyX += 4
            Ennemy2X += 4
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
            Heros1X += 2
            Heros2X += 2
            Heros3X += 2



        if Heros1X >= 0:
            HerosApparition = False
            all_spritesPokeballAll.update()
            all_spritesPokeballAll.draw(screen)
            NatWait += 0.4


        if NatWait >= 12:
            Heros1X -= 2
            Heros2X -= 2
            Heros3X -= 2
            POKE2 = True


        if Heros3X < -200:
            HerosApparition2 = False
            NatWait = 0
            StartFight=True

        if POKE2 == True:
            all_spritesFeuillosaure.update()
            all_spritesFeuillosaure.draw(screen)
            all_spritesPokemonOuvertureAllié.update()
            all_spritesPokemonOuvertureAllié.draw(screen)



        if StartFight==True:  #l'animation se termine, le combat se lance et toutes les images s'affichent
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


        #on enleve le pokemon du screen lorsqu'il est mort et quitte l'ecran
        if Xennemy >= screenwidth+100:
            all_spritesGuépardent.remove(guépardent)

        if Xallie <= -150:
            all_spritesFeuillosaure.remove(feuillosaure)



        #SAC ET POTION (on gere l'utilisation de la potion et l'ouverture du sac)
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
            current_tour += 0.6

            healornot = random.randint(1,3)
            whatattack = random.randint(1,3)
            precision = random.randint(1, 3)


            if int(current_tour) == 20 and barwidth2 <= 40 and healornot < 3 and nbpotion2 > 0: #le pokemon se soigne...
                barwidth2 += 40
                NbdePVEnnemy = policearialpv.render(str(barwidth2), 1, black)
                soundhealennemy.play()
                missennemy = False
                nbpotion2 -= 1
                nbpotiontxt2 = policearialpt.render(str(nbpotion2), 1, white)
                attack = False

            else: #...sinon, il attaque

                if whatattack > 2:    #sa premiere attaque qui peut rater mais qui est puissante
                    if precision > 1:   #possibilité de rater l'attaque
                        if int(current_tour) == 20 and barwidth > 0:
                            missennemi = False
                            attackanimationennemy = True  #on lance l'animation de l'attaque
                            attackValue2 = random.randint(int((16/100)*barwidthOG), int((16/100)*barwidthOG))

                            if abri == True:   #si le pokemon allié se protege, l'attaque ne vaut rien
                                attackValue2 = 0

                            if barwidth > int((50/100)*barwidthOG):    #actualise la couleur de la barre de vie
                                colorHPbar = green

                            if barwidth <= int((50/100)*barwidthOG):
                                colorHPbar = yellow

                            if barwidth <= int((18/100)*barwidthOG):
                                colorHPbar = red

                            if attackValue2 >= barwidth:   #inflige les degats
                                attackValue2 = barwidth
                                barwidth -= attackValue2
                                deathallie = True  #le pokemon meurt
                                sounddeath.play()
                                NbdePV = policearialpv.render(str(barwidth), 1, black)

                            else:    #si il ne meurt pas, il se prend l'attaque et continue le combat
                                barwidth -= attackValue2
                                sound2ndattack.play()
                                NbdePV = policearialpv.render(str(barwidth), 1, black)   #son nombre de points de vie s'actualise

                        if attackValue2 >= barwidth2:
                            attackValue2 = barwidth2


                        if current_tour >= 40:   #au bout d'un certain temps, le tour passe à l'autre
                            attack = False

                        if current_tour >= 3:    #current tour gere la temporalité de l'attaque en retour ennemie
                            attackanimationallie = False

                    elif int(current_tour) == 20:
                        missennemi = True
                        soundmissed.play()

                else:    #l'autre attaque, qui ne rate jamais mais qui est moins puissante, de meme que pour l'autre attaque...
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


            if missennemi == False and 20 < current_tour < 40 and abri == True:    #affiche le texte d'abri
                TXTabri()

            if miss == True and current_tour <= 20:    #affiche texte de raté
                txtmiss()
            if miss == False and current_tour <= 20 and attaqueplus == False:   #texte de changement de tour
                Tour2()
            elif attaqueplus == True and miss == False and current_tour <= 20:    #texte d'augmentation d'attaque
                TXTattaquebonus()

            if missennemi == True and 20 < current_tour < 40:    #texte de raté ennemi
                txtmissennemi()

            if current_tour >= 3:
                attackanimationallie = False
            if current_tour >= 23:
                attackanimationennemy = False


        elif deathennemy == True:     #le pokemon ennemi meurt, on attend un peu et on quitte le combat
            txtdeathennemy()
            current_tour+=1
            if current_tour >= 150:
                txtChallengeKal = False
                current_tour = 0
                musicplaymap = True



        elif deathallie == True:  #de meme, si l'allie meurt on quitte le combat
            txtdeathallie()
            current_tour+=1
            #print(current_tour)
            if current_tour >= 150:
                txtChallengeKal = False
                current_tour = 0
                musicplaymap = True



        else:    #si personne ne meurt, le combat continue!
            current_tour = 0
            if StartFight==True:
                Tour()
                attaqueplus = False




        if SacOuvert==True:  #le sac est ouvert, on affiche l'image du sac et de la potion qui est maintenant cliquable
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


        #####################################################################  Boucle Combat

        #####################################################################  For event Global

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

                ##############################################################   For event Map

        if txtChallengeKal == False:     #si on est pas en combat, c'est la carte!

            if musicplaymap:
                pygame.mixer_music.load("BourgCourmomble2.wav")
                pygame.mixer_music.set_volume(0.4)
                pygame.mixer.music.play(loops=-1, fade_ms=2)
                musicplaymap = False


            #print("X: "+ str(XNat))
            #print("Y: "+str(YNat))

            if keys[pygame.K_RIGHT]:      #en fonction de la fleche sur laquelle on clique, la direction du perso change
                Gauche = False
                Droite = True
                Haut = False
                Bas = False
                Statik = False



            elif keys[pygame.K_LEFT]:
                Gauche = True
                Droite = False
                Haut = False
                Bas = False
                Statik = False



            elif keys[pygame.K_UP]:
                Gauche = False
                Droite = False
                Haut = True
                Bas = False
                Statik = False



            elif keys[pygame.K_DOWN]:
                Gauche = False
                Droite = False
                Haut = False
                Bas = True
                Statik = False



            else:    #si on clique sur rien, le perso est statik
                Gauche = False
                Droite = False
                Haut = False
                Bas = False
                Statik = True





                ####################################################################    For event Combat

        if txtChallengeKal == True:    #on est de nouveau en combat!

            if musicplaycombat:   #la musique du combat se lance 1 fois dans le for event pour ne pas se repeter et etre inaudible
                pygame.mixer_music.load("RivalFight.wav")
                pygame.mixer_music.set_volume(0.5)
                pygame.mixer.music.play(loops=-1, fade_ms=2)
                musicplaycombat = False


            if attack == False and deathallie == False and StartFight==True:     #ouverture du sac si on clique dessus, avec son petit bruit
                if SacButtonX <= mouse[0] <= SacButtonX+widthB and SacButtonY <= mouse[1] <= SacButtonY+heightB:
                    if click[0] == 1:
                        if SacOuvert == False:
                            sacopen.play()
                            SacOuvert=True
                        else:
                            SacOuvert = False
                            sacclose.play()





            #si la souris est sur le button d'abris et clique
            if attack == False and deathallie == False and StartFight==True:
                if button1X <= mouse[0] <= button1X+widthB and button1Y <= mouse[1] <= button1Y+heightB:
                    if click[0] == 1:

                        tourabri -= 1  #on ne peut pas utiliser abris deux fois de suite
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



                            #sinon on attaque (ici c'est abri donc on attaque pas vraiment)
                            else:
                                barwidth2 -= attackValue
                                sound.play()
                                NbdePVEnnemy = policearialpv.render(str(barwidth2), 1,black,)







            #si la souris est sur le button attaque puissante et clique
            if attack == False and deathallie == False and StartFight==True:
                if B2buttonX <= mouse[0] <= B2buttonX+widthB and B2buttonY <= mouse[1] <= B2buttonY+heightB:
                    if click[0] == 1:
                        precision = random.randint(1, 3)

                        tourabri -= 1
                        if tourabri <= 0:
                            abri = False


                        #defini les couleurs de la barre de vie en fonction de sa taille/valeur
                        attack = True
                        if precision > 1:   #on peut rater l'attaque
                            miss = False
                            attackanimationallie = True
                            if barwidth2 > 0:

                                attackValue = random.randint(int((15/100)*barwidthOG), int((15/100)*barwidthOG))
                                attackValue += attaquebonus

                                if barwidth2 > int((30/100)*barwidthOG):    #tout ce systeme a deja ete commenté plus haut :)
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




            #2si on clique sur le bouton attaque + l'attaque du pokemon augmente
            if attack == False and deathallie == False and StartFight==True:
                if AttackButtonX <= mouse[0] <= AttackButtonX + int((15/100)*screenwidth) and AttackButtonY <= mouse[1] <= AttackButtonY + int((10/100)*screenheight):
                    if click[0] == 1:

                        attack = True
                        miss = False
                        attaquebonus += 3
                        attaqueplus = True









    #rafraichi en continu

    pygame.display.update()
    clock.tick(60)






